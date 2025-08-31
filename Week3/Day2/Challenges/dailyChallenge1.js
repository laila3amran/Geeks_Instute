// Array of planets with their colors and moons
const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "orange", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "brown", moons: 79 },
  { name: "Saturn", color: "goldenrod", moons: 83 },
  { name: "Uranus", color: "lightblue", moons: 27 },
  { name: "Neptune", color: "darkblue", moons: 14 }
];

// Select the section
const section = document.querySelector(".listPlanets");

// Loop through each planet
planets.forEach(planet => {
  // Create planet div
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planet.color;
  planetDiv.textContent = planet.name; // optional: add planet name

  // Add moons
  for (let i = 0; i < planet.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");
    // Position moons around the planet randomly
    moon.style.top = `${Math.random() * 80}px`;
    moon.style.left = `${Math.random() * 80}px`;
    planetDiv.appendChild(moon);
  }

  // Append planet to the section
  section.appendChild(planetDiv);
});
