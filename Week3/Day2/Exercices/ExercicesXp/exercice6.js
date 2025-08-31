// Change id
document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

// Add Logout
let newLi = document.createElement("li");
let text = document.createTextNode("Logout");
newLi.appendChild(text);
document.querySelector("#socialNetworkNavigation ul").appendChild(newLi);


let ul = document.querySelector("#socialNetworkNavigation ul");
console.log("First:", ul.firstElementChild.textContent);
console.log("Last:", ul.lastElementChild.textContent);
