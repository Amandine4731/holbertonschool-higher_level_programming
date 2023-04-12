#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const i of list.flat()) {
    if (i === searchElement) {
      counter++;
    }
  }
  console.log(counter);
};
