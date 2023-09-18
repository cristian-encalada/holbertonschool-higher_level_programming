// Fetch and list the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
$(document).ready(function () {
  // AJAX GET request to the SWAPI API
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    // Loop to extract the titles
    data.results.forEach(function (movie) {
      const title = movie.title;
      // Create and append a new <li> for each title
      $('<li>').text(title).appendTo('#list_movies');
    });
  });
});
