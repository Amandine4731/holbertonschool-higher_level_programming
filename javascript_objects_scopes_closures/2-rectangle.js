#!/usr/bin/node

class Rectangle {
  #width = 0;
  #height = 0;
  constructor (w, h) {
    if ((w > 0) && (h > 0) ) {
      this.#width = w;
      this.#height = h;
    }
  }
}
module.exports = Rectangle;
