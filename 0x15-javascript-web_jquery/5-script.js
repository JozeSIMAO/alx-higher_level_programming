document.addEventListener('DOMContentLoaded', function () {
  const addItem = $('#add_item');
  addItem.click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});
