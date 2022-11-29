#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w >= 0 && typeof h === 'number' && h >= 0) {
    this.w = w;
    this.h = h;
    }
  }
}
module.exports = Rectangle;
