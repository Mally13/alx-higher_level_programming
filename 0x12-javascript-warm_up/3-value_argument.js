#!/usr/bin/node

const {argv} = process;

if (argv.length === 2)
	console.log('No argument');
else
{
	argv.forEach((val, index) => {
		if (index !== 0 && index !== 1)
			console.log(val);
	});
}
