function isPalindrome(str) {
  // Remove spaces/special characters and lowercase
  str = str.toLowerCase().replace(/[\W_]/g, '');
  return str === str.split('').reverse().join('');
}


console.log(isPalindrome("madam")); 
console.log(isPalindrome("kayak")); 
console.log(isPalindrome("hello")); 
