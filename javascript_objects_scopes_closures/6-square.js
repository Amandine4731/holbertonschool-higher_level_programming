#!/usr/bin/node

const Squareparent = require('./5-square');

class Square extends Squareparent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        if (c === 'C') {
          process.stdout.write(c);
        } else {
          process.stdout.write('X');
        }
      }
      console.log();
    }
  }
}
module.exports = Square;
