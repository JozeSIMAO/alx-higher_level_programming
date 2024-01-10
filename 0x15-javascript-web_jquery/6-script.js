document.addEventListener('DOMContentLoaded', function () {
  const updateHeader = $('#update_header');
  updateHeader.click(function () {
    $('header').text('New Header!!!');
  });
});
