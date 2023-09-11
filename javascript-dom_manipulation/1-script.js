const header = document.getElementById('red_header');
header.addEventListener('click', function onClick (event) {
  // Change text color for the clicked element only
  event.target.style.color = '#FF0000';
});
