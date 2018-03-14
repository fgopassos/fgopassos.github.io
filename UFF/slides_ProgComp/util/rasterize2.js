const puppeteer = require('puppeteer');

var baseOutput = '/tmp/pdf-out/';

(async () => {
	const browser = await puppeteer.launch({args: ['--disable-web-security']});
	const page = await browser.newPage();

	await page.setViewport({width: 908, height: 681});
	await page.goto('file:///home/diego/Dropbox/Compartilhamento/Slides/aula1/slides.html', {waitUntil: 'networkidle2'});
	await page.emulateMedia('screen');

	var i, total;

	total = await page.evaluate('slideshow.getSlideCount();');
	await page.evaluate('slideshow.gotoFirstSlide();');

	for (i = 0; i < total; i++) {

		await page.pdf({path: baseOutput + i + '.pdf', width: 908, height: 681, margin: {top: 0, bottom: 0, left: 0, right: 0}, printBackground: true});
		await page.evaluate('slideshow.gotoNextSlide();');
	}

	await browser.close();
})();
