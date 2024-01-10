document.addEventListener('DOMContentLoaded', function () {
  const toggleHeader = $('#toggle_header');
  toggleHeader.click(function () {
    $('header').toggleClass('red green');
  });
});
