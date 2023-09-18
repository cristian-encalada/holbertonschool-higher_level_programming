// Add, remove and clear LI elements from a list when the user clicks:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list

$(document).ready(function () {
  $('#add_item').click(function () {
    // When the user clicks on DIV#add_item: a new element is added to the list
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  $('#remove_item').click(function () {
    // When the user clicks on DIV#remove_item: the last element is removed from the list
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    // When the user clicks on DIV#clear_list: all elements of the list are removed
    $('ul.my_list').empty();
  });
});
