function changeEnough(itemPrice, amountOfChange) {
  let [quarters, dimes, nickels, pennies] = amountOfChange;
  let total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01);

  return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); 
console.log(changeEnough(14.11, [2,100,0,0]));   
console.log(changeEnough(0.75, [0,0,20,5]));     
