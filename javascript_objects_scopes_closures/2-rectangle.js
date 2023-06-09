#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object if width or height is 0 or not a positive integer
      return {};
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
