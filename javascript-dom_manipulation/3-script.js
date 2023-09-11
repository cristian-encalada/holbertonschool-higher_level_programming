// Toggles the class of the header element when the user clicks on the tag id toggle_header
let header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', function onClick (event) {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
});
