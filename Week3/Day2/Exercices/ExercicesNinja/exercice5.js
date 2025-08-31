function uniqueElements(arr) {
  return [...new Set(arr)];
}


console.log(uniqueElements([1, 2, 3, 3, 3, 3, 4, 5])); 
console.log(uniqueElements(['a', 'b', 'a', 'c', 'b'])); 
