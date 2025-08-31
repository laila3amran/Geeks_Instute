function biggestNumberInArray(arrayNumber) {
  if (arrayNumber.length === 0) return 0;

  let max = -Infinity;
  for (let num of arrayNumber) {
    if (typeof num === "number" && num > max) {
      max = num;
    }
  }
  return max === -Infinity ? 0 : max;
}

// Tests
const array = [-1, 0, 3, 100, 99, 2, 99];
const array2 = ['a', 3, 4, 2];
const array3 = [];

console.log(biggestNumberInArray(array));  // 100
console.log(biggestNumberInArray(array2)); // 4
console.log(biggestNumberInArray(array3)); // 0
