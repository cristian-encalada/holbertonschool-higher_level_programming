// Note: Fetching data from a remote server is an asynchronous operation
// Fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Async function to fetch all movie titles
const fetchMovies = async () => {
  const response = await fetch(url);
  const data = await response.json();
  const movies = data.results;

  for (const movie of movies) {
    const li = document.createElement('li');
    li.textContent = movie.title;
    document.getElementById('list_movies').appendChild(li);
  }
};
// Call the function to initiate the data retrieval
fetchMovies();
