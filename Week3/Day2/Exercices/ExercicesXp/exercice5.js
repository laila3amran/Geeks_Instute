// Retrieve the div
const div = document.getElementById("container");
console.log(div);

// Change Pete to Richard
document.querySelectorAll(".list li")[1].textContent = "Richard";

document.querySelectorAll(".list")[1].children[1].remove();


document.querySelectorAll(".list").forEach(ul => {
  ul.firstElementChild.textContent = "Imran"; // your name
});

// Add classes
document.querySelectorAll(".list").forEach(ul => ul.classList.add("student_list"));
document.querySelector(".list").classList.add("university", "attendance");


div.style.background = "lightblue";
div.style.padding = "20px";


let allLis = document.querySelectorAll("li");
allLis.forEach(li => {
  if (li.textContent === "Dan") li.style.display = "none";
});


allLis.forEach(li => {
  if (li.textContent === "Richard") li.style.border = "2px solid black";
});


document.body.style.fontSize = "20px";

// Bonus
if (div.style.background === "lightblue") {
  let users = Array.from(document.querySelectorAll(".list:first-child li")).map(li => li.textContent);
  alert(`Hello ${users[0]} and ${users[1]}`);
}
