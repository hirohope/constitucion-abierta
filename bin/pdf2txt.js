var args = process.argv.slice(2);
if (args.length == 0) {
	console.log("Usage: node pdf2txt.js path/to/pdf");
	console.log("output: a .txt with the same name and folder");
	process.exit(1);
}
if (args.length > 1) {
	console.log("too many arguments!");
	process.exit(1);
}
var filename = args[0];

require('pdfjs-dist');
var fs = require('fs');

fs.readFile(filename, function (err, data) {
	if (err) {console.log(err); process.exit(1);}
	data = new Uint8Array(data);
	
	var textArray;
	PDFJS.getDocument(data).then(function (pdf) {
		textArray = new Array(pdf.numPages);
		
		var addPage = function (pageNum) {
			return pdf.getPage(pageNum).then(function (page) {
				return page.getTextContent().then(function (content) {
					var strings = content.items.map(function (item) {
						return item.str;
					});
					textArray[pageNum-1] = strings.join(' ');
				});
			});
		};
		
		var promiseChain = Promise.resolve();
		for (var i = 1; i <= pdf.numPages; ++i)
			promiseChain = promiseChain.then(addPage.bind(null, i));
		return promiseChain;
	})
	.then(function () {
		var output = textArray.join('\n');
		filename = filename.substr(0, filename.lastIndexOf('.')) + '.txt';
		fs.writeFile(filename, output, function (err) {
			if (err) {console.log(err); process.exit(1);}
			console.log("the file was saved!");
		});
	});
});