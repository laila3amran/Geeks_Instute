function hotelCost(nights) {
  return nights * 140;
}

function planeRideCost(destination) {
  destination = destination.toLowerCase();
  if (destination === "london") return 183;
  if (destination === "paris") return 220;
  return 300;
}

function rentalCarCost(days) {
  let cost = days * 40;
  if (days > 10) cost *= 0.95; 
  return cost;
}

function totalVacationCost() {
  let nights = Number(prompt("How many nights do you want to stay in the hotel?"));
  let destination = prompt("Where do you want to fly?");
  let days = Number(prompt("How many days do you want to rent a car?"));

  let hotel = hotelCost(nights);
  let plane = planeRideCost(destination);
  let car = rentalCarCost(days);

  console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}`);
  return car + hotel + plane;
}

totalVacationCost();
