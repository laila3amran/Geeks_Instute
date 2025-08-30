//Exercice 1
let numbers = [123, 8409, 100053, 333333333, 7];

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] % 3 === 0); 
  // → true or false
}

//Exercice 2
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
};

let studentName = prompt("What is your name?");

if (studentName.toLowerCase() in guestList) {
  console.log(`Hi! I'm ${studentName}, and I'm from ${guestList[studentName.toLowerCase()]}.`);
} else {
  console.log("Hi! I'm a guest.");
}

//Exercice 3

let age = [20, 5, 12, 43, 98, 55];

// 1. Sum of all numbers
let sum = 0;
for (let i = 0; i < age.length; i++) {
  sum += age[i];
}
console.log("Sum:", sum);

// 2. Highest age
let highest = age[0];
for (let i = 1; i < age.length; i++) {
  if (age[i] > highest) {
    highest = age[i];
  }
}
console.log("Highest:", highest);
