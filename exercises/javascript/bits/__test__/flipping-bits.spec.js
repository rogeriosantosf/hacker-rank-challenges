const flippingBits = require("../flipping-bits");

test("flip the bits of the number 9", () => {
  expect(flippingBits(9)).toEqual(4294967286);
});
