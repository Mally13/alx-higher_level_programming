$(document).ready(function () {
  const link = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(link, function (data) {
    $.each(data.results, function (k, v) {
      $('UL#list_movies').append(`<li>${v.title}</li>`);
    });
  });
});
