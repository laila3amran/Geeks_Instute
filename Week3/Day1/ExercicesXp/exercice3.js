let num = prompt("Enter a number:");

while (Number(num) < 10) {
  num = prompt("Enter a new number greater or equal to 10:");
}
console.log("You entered:", num);
