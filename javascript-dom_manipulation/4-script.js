// Adds a li element to a list when the user clicks on the element with id add_item
const addItem = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
