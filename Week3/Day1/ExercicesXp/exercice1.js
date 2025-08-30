// Exercice1
//Part1

const people = ["Greg", "Mary", "Devon", "James"];

// 1. Remove “Greg”
people.shift();

// 2. Replace “James” with “Jason”
people[people.indexOf("James")] = "Jason";

// 3. Add your name
people.push("Imran");

// 4. Log Mary’s index
console.log(people.indexOf("Mary"));  // → 0

// 5. Make a copy without Mary and your name
const peopleCopy = people.slice(1, people.length - 1);
console.log(peopleCopy); // ["Devon", "Jason"]

// 6. Index of "Foo"
console.log(people.indexOf("Foo")); // → -1
// Explanation: -1 means "Foo" is not found in the array.

// 7. Variable last = last element
let last = people[people.length - 1];
console.log(last); // "Imran"

console.log(people);

//part2
// 1. Loop and log each person
for (let person of people) {
  console.log(person);
}

// 2. Stop after “Devon”
for (let person of people) {
  console.log(person);
  if (person === "Devon") break;
}



