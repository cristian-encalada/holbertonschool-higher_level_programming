// Script that adds, removes and clears li elements from a list when the user clicks

// DOMContentLoaded function added to avoid Uncaught TypeError: addItem is null
// If not, the JavaScript code runs before the HTML document is fully loaded

document.addEventListener('DOMContentLoaded', function () {
  const ul = document.querySelector('.my_list');

  const addItem = document.getElementById('add_item');
  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });

  const removeItem = document.getElementById('remove_item');
  removeItem.addEventListener('click', () => {
    const lastLi = ul.lastElementChild;
    if (lastLi) {
      ul.removeChild(lastLi);
    }
  });

  const clearList = document.getElementById('clear_list');
  clearList.addEventListener('click', () => {
    while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
    }
  });
});
