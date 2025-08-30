const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let societyName = names.map(name => name[0]).sort().join("");
console.log(societyName); // "ABJKPS"
