#!/usr/bin/node

class Rectangle {
  #width = 0;
  #height;
  constructor (w, h) {
    if ((w > 0) && (h > 0) ) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height - 1; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
  