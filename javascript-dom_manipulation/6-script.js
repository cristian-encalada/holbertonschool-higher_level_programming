// Note: Fetching data from a remote server is an asynchronous operation

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Async function to fetch and display the character name
const fetchCharacterName = async () => {
  const response = await fetch(url);
  const data = await response.json();
  const characterName = data.name;

  document.getElementById('character').innerHTML = characterName;
};
// Call the function to initiate the data retrieval
fetchCharacterName();
