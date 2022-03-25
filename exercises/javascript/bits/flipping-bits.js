/*
 * Complete the 'flippingBits' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */
function flippingBits(n) {
  /**
   * using the ~ (NOT) operator, we get the invert 32 bit sequence
   * and then we apply the fill right shift to add the necessary zeros to the left
   */
  return ~n >>> 0;
}

module.exports = flippingBits;