// Step 1: Create the sentence
let sentence = "The movie is not that bad, I like it";

// Step 2: Find positions of "not" and "bad"
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

// Step 3: Check conditions
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
 
  let result = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  console.log(result);
} else {
  
  console.log(sentence);
}


let s1 = "This dinner is not that bad ! You cook well";
let s2 = "This movie is not so bad !";
let s3 = "This dinner is bad !";


function checkSentence(sentence) {
  let wordNot = sentence.indexOf("not");
  let wordBad = sentence.indexOf("bad");

  if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    return sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  }
  return sentence;
}

console.log(checkSentence(s1));
console.log(checkSentence(s2)); 
console.log(checkSentence(s3)); 

