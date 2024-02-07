$(document).ready(function () {
  const link = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(link, function (data) {
    $('DIV#hello').html(data.hello);
  });
});
