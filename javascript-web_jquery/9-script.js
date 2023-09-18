// Fetch from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
// The translation of “hello” must be displayed in the HTML tag DIV#hello
// The script must work when it is imported from the <head> tag
$(document).ready(function () {
  // AJAX GET request to the API
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract "hello" value from the response data
    const translation = data.hello;
    // Display the translation in the tag <div id="hello">
    $('#hello').text(translation);
  });
});
