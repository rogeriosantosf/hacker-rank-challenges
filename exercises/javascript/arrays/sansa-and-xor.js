/*
 * Complete the 'sansaXor' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
function sansaXor(arr) {
  let result;

  // if an array has an even number of elements
  // applying XOR to the elements and the contiguos subarrays will result in 0
  if (arr.length % 2 === 0) return 0;

  // if an array has an odd number of elements
  // each element in an odd index appears an even number of times,
  // therefore producing 0
  // each element in an even index appears an odd number of times,
  // and are the only ones that need to be computed

  // loop over the even indexes
  for (let x = 0; x < arr.length; x += 2) {
    result ^= arr[x];
  }
  return result;
}
