#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }
      console.log(myVar);
    }
  }

  rotate () {
    this.width = h;
    this.height = w;
  }

  double () {
    this.width = w * 2;
    this.height = h * 2;
  }
}
module.exports = Rectangle;
