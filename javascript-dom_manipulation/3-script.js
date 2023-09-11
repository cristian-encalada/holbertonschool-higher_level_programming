// Toggles the class of the header element when the user clicks on the tag id toggle_header
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', function onClick (event) {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
