function wordsInFrame() {
  // 1. Ask user for input
  const input = prompt("Enter several words separated by commas: ");
  
  // 2. Convert to array and trim spaces
  const words = input.split(",").map(word => word.trim());

  // 3. Find the longest word
  const maxLength = Math.max(...words.map(word => word.length));

  // 4. Top border
  let border = "*".repeat(maxLength + 4);
  console.log(border);

  // 5. Each word inside the frame
  for (let word of words) {
    let spaces = " ".repeat(maxLength - word.length);
    console.log(`* ${word}${spaces} *`);
  }

  // 6. Bottom border
  console.log(border);
}

// Run the function
wordsInFrame();
