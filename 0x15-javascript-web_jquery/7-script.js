$(document).ready(function () {
  const link = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(link, function (data) {
    $('DIV#character').html(data.name);
  });
});
