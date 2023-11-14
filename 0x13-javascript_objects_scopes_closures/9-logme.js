#!/usr/bin/node

let argsIndex = 0;
module.exports.logMe = function (item) {
  console.log(`${argsIndex}: ${item}`);
  argsIndex++;
};
