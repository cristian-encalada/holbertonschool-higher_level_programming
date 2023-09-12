// Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello
// Note: Fetching data from a remote server is an asynchronous operation

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Async function to fetch and display value of hello
const fetchHello = async () => {
  const response = await fetch(url);
  const data = await response.json();
  const hello = data.hello;

  document.getElementById('hello').innerHTML = hello;
};
// Call the function to initiate the data retrieval
fetchHello();
