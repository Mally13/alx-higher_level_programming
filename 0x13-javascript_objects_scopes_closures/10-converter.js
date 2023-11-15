#!/usr/bin/node
exports.converter = function converter (base) {
  return function (number) {
    return number.toString(base);
  };
};
