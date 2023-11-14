#!/usr/bin/node

module.exports.esrever = function (list) {
  const newList = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    newList.push(list[i]);
  }
  list = newList;
  return list;
};
