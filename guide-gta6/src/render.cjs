// Rendu PDF via Chromium : node src/render.js
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(root, 'build', 'guide.html'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const info = await page.evaluate(() => {
    const MM = 96 / 25.4;
    const pages = [...document.querySelectorAll('.page')];
    const overflow = [];
    pages.forEach((p, i) => { const c = p.querySelector('.content');
      if (c && c.scrollHeight > c.clientHeight + 2) overflow.push([i + 1, Math.round((c.scrollHeight - c.clientHeight) / MM)]); });
    const boxes = [...document.querySelectorAll('.cb[data-name]')].map((el, k) => {
      const pg = el.closest('.page'); const pr = pg.getBoundingClientRect(); const r = el.getBoundingClientRect();
      return { page: pages.indexOf(pg), x: (r.left - pr.left) / MM, y: (r.top - pr.top) / MM, w: r.width / MM, h: r.height / MM, name: 'cb' + k + '_' + el.dataset.name };
    });
    return { n: pages.length, overflow, boxes };
  });
  fs.writeFileSync(path.join(root, 'build', 'checkboxes.json'), JSON.stringify(info.boxes));
  console.log('pages', info.n, 'checkboxes', info.boxes.length);
  if (info.overflow.length) console.log('OVERFLOW (page, mm):', JSON.stringify(info.overflow));
  await page.pdf({ path: path.join(root, 'build', 'guide-raw.pdf'), width: '148mm', height: '210mm', printBackground: true,
                   preferCSSPageSize: true, outline: false, tagged: true });
  await browser.close();
})();
