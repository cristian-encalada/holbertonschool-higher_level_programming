// Fetch and prints how to say “Hello” depending on the language
// Use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate
// The translation of “Hello” must be displayed in the HTML tag DIV#hello

$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();
    // Make a GET request to the HelloSalut API
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      // Ensure that any special characters are properly decodified
      const decodified = $('<div></div>').html(data.hello).text();
      $('#hello').text(decodified);
    });
  });
});
