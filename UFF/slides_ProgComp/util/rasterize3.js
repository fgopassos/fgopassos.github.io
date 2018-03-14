const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch({args: ['--disable-web-security']});
	const page = await browser.newPage();

	await page.setViewport({width: 908, height: 681});
	await page.goto('file:///home/diego/Dropbox/Compartilhamento/Slides/aula1/slides.html', {waitUntil: 'networkidle2'});

	await page.pdf({path: '/tmp/pdf-out/out.pdf', width: 908, height: 681, margin: {top: 0, bottom: 0, left: 0, right: 0}, printBackground: true});

	await browser.close();
})();
