// Updates the text of the header element to 'New Header!!!' when the user clicks on the element with id update_header
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', function () {
  updateHeader.textContent = 'New Header!!!';
});
