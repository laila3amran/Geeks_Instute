//Exercice 1
// Person objects
let person1 = {
  fullName: "John Doe",
  mass: 85,       // kg
  height: 1.8,    // meters
  calcBMI: function() {
    return this.mass / (this.height * this.height);
  }
};

let person2 = {
  fullName: "Jane Smith",
  mass: 68,
  height: 1.65,
  calcBMI: function() {
    return this.mass / (this.height * this.height);
  }
};

// Function to compare BMI
function compareBMI(p1, p2) {
  let bmi1 = p1.calcBMI();
  let bmi2 = p2.calcBMI();

  if (bmi1 > bmi2) {
    console.log(`${p1.fullName} has the larger BMI (${bmi1.toFixed(2)})`);
  } else if (bmi2 > bmi1) {
    console.log(`${p2.fullName} has the larger BMI (${bmi2.toFixed(2)})`);
  } else {
    console.log(`${p1.fullName} and ${p2.fullName} have the same BMI (${bmi1.toFixed(2)})`);
  }
}

// Run comparison
compareBMI(person1, person2);
