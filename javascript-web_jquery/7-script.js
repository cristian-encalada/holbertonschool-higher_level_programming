// Fetch the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
$(document).ready(function () {
  // AJAX GET request to the SWAPI API
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    // Extract the character name
    const characterName = data.name;
    // Display the character name
    $('#character').text(characterName);
  });
});
