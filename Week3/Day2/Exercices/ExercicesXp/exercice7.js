let allBooks = [
  {
    title: "Clean Code",
    author: "Robert C. Martin",
    image: "https://m.media-amazon.com/images/I/41xShlnTZTL._SX374_BO1,204,203,200_.jpg",
    alreadyRead: true
  },
  {
    title: "The Pragmatic Programmer",
    author: "Andrew Hunt",
    image: "https://m.media-amazon.com/images/I/518FqJvR9aL._SX377_BO1,204,203,200_.jpg",
    alreadyRead: false
  }
];

let section = document.querySelector(".listBooks");

allBooks.forEach(book => {
  let div = document.createElement("div");

  let p = document.createElement("p");
  p.textContent = `${book.title} written by ${book.author}`;
  if (book.alreadyRead) p.style.color = "red";

  let img = document.createElement("img");
  img.src = book.image;
  img.style.width = "100px";

  div.appendChild(p);
  div.appendChild(img);
  section.appendChild(div);
});
