// Generate random number between 1 and 100
let randomNum = Math.floor(Math.random() * 100) + 1;
console.log("Random number:", randomNum);


for (let i = 0; i <= randomNum; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}
