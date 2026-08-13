// Drives Edge via DevTools Protocol to render at a TRUE mobile viewport.
// Usage: node scripts/cdp_shot.mjs <url> <width> <height> <outPng> [scrollY]
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { setTimeout as sleep } from 'node:timers/promises';

const [url, W, H, out, scrollY] = process.argv.slice(2);
const width = Number(W), height = Number(H);
const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PORT = 9200 + (width % 500);

const proc = spawn(EDGE, [
  '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
  `--remote-debugging-port=${PORT}`, '--user-data-dir=' + process.env.TEMP + '/edge-cdp-' + PORT,
  'about:blank',
], { stdio: 'ignore' });

async function cdpList() {
  const r = await fetch(`http://localhost:${PORT}/json`);
  return r.json();
}

try {
  // wait for the debug endpoint
  let targets;
  for (let i = 0; i < 40; i++) {
    try { targets = await cdpList(); if (targets.length) break; } catch {}
    await sleep(250);
  }
  const page = targets.find(t => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(res => ws.addEventListener('open', res, { once: true }));

  let id = 0; const pending = new Map();
  ws.addEventListener('message', ev => {
    const m = JSON.parse(ev.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  });
  const send = (method, params = {}) => new Promise(res => {
    const mid = ++id; pending.set(mid, res);
    ws.send(JSON.stringify({ id: mid, method, params }));
  });

  await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride',
    { width, height, deviceScaleFactor: 2, mobile: true });
  await send('Emulation.setTouchEmulationEnabled', { enabled: true });
  await send('Page.navigate', { url });
  await sleep(3500); // let fonts/poster settle

  if (scrollY) {
    await send('Runtime.evaluate', {
      expression: `window.scrollTo(0, ${Number(scrollY)}); window.dispatchEvent(new Event('scroll'));`,
    });
    await sleep(700); // let the reveal/scroll transitions play
  }

  const measure = await send('Runtime.evaluate', {
    expression: `JSON.stringify({cw:document.documentElement.clientWidth,sw:document.documentElement.scrollWidth,ov:document.documentElement.scrollWidth-document.documentElement.clientWidth})`,
    returnByValue: true,
  });
  console.log('MEASURE', measure.result.result.value);

  const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  writeFileSync(out, Buffer.from(shot.result.data, 'base64'));
  console.log('WROTE', out);
} finally {
  proc.kill();
}
