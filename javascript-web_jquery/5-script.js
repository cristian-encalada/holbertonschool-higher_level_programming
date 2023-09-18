// Add a <li> element to a list when the user clicks on the tag DIV#add_item
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});
