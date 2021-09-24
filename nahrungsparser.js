const puppeteer = require('puppeteer');
 
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://siemens.cateringportal.io/menu/Erlangen%20S%20SP%206/Mittagessen');
  
  /*console.log("page opened, waiting for menu population");*/
  await page.waitForTimeout(3000);
 
  const wrappers = await page.$$(".product-wrapper");
 
  const texts = await Promise.all(wrappers.map(wrapper => page.evaluate(el => el.innerHTML, wrapper)));
  console.log(texts);  
 
  await browser.close();
})();