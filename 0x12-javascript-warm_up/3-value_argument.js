#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((val, index) => {
	if (index != 1 && index != 0)
		console.log(val);
	if (index == 1 && argv[2] == null)
		console.log("No argument");
});
