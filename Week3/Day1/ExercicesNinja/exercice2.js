//Exercice 2
function findAvg(gradesList) {
  let sum = 0;

  for (let i = 0; i < gradesList.length; i++) {
    sum += gradesList[i];
  }

  let avg = sum / gradesList.length;
  console.log("Average:", avg);

  if (avg >= 65) {
    console.log("You passed the course ");
  } else {
    console.log("You failed the course You must repeat.");
  }
}


findAvg([80, 70, 60, 90]); 
findAvg([40, 55, 50]);     


// Function to calculate average
function calcAverage(gradesList) {
  let sum = 0;
  for (let i = 0; i < gradesList.length; i++) {
    sum += gradesList[i];
  }
  return sum / gradesList.length;
}

function findAvg(gradesList) {
  let avg = calcAverage(gradesList);
  console.log("Average:", avg);

  if (avg >= 65) {
    console.log("You passed the course ");
  } else {
    console.log("You failed the course  You must repeat.");
  }
}


findAvg([80, 90, 70, 60]); 
findAvg([50, 40, 60]);    
