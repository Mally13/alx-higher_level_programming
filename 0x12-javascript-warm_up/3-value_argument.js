#!/usr/bin/node

const {argv} = process;

argv.forEach((val, index) => {
	if (index === 1 && !argv[2])
		console.log('No argument');
	else if (index !== 0 && index !== 1)
		console.log(val);
});
