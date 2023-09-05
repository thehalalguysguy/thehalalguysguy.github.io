// Get all the table cells in the specified columns
const cells = document.querySelectorAll('.ratings-table table tbody tr td:nth-child(5), \
                                         .ratings-table table tbody tr td:nth-child(6), \
                                         .ratings-table table tbody tr td:nth-child(7), \
                                         .ratings-table table tbody tr td:nth-child(8), \
                                         .ratings-table table tbody tr td:nth-child(9)');

// Define the color scale
const colorScale = d3.scaleLinear()
  .domain([1, 10]) // Define the range of values
  .range(['white', 'darkgreen']); // Define the corresponding colors

// Loop through each cell
cells.forEach(cell => {
    const value = parseInt(cell.textContent);
    // Center text
    cell.style.textAlign = 'center';    
    // Apply conditional formatting based on the cell value
    cell.style.backgroundColor = colorScale(value);
    // If background is dark make font color light
    if (value >= 5) {
        cell.style.color = 'white';
        }
    
});