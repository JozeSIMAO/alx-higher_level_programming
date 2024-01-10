document.addEventListener('DOMContentLoaded', function () {
  const characterDiv = $('#character');
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    characterDiv.text(data.name);
  });
});
