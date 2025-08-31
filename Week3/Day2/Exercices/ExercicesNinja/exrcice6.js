function createCalendar(year, month) {
  let mon = month - 1; // JavaScript months start at 0
  let d = new Date(year, mon);

  let table = '<table><tr><th>MO</th><th>TU</th><th>WE</th><th>TH</th><th>FR</th><th>SA</th><th>SU</th></tr><tr>';

  // Calculate the day of week (Monday = 0)
  let startDay = (d.getDay() + 6) % 7;

  // Empty cells before the first day
  for (let i = 0; i < startDay; i++) {
    table += '<td></td>';
  }

  while (d.getMonth() === mon) {
    table += '<td>' + d.getDate() + '</td>';

    if ((d.getDay() + 6) % 7 === 6) { // Sunday
      table += '</tr><tr>';
    }

    d.setDate(d.getDate() + 1);
  }

  // Fill the last row with empty cells
  let lastDay = (d.getDay() + 6) % 7;
  if (lastDay !== 0) {
    for (let i = lastDay; i < 7; i++) {
      table += '<td></td>';
    }
  }

  table += '</tr></table>';

  // Render the table inside body
  document.body.innerHTML = table;
}


createCalendar(2012, 9);
