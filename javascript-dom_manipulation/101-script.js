// Script that fetches and prints how to say “Hello” depending on the language
document.addEventListener('DOMContentLoaded', function () {
  const btnTranslateId = document.getElementById('btn_translate');
  const languageCodeId = document.getElementById('language_code');
  const helloId = document.getElementById('hello');

  btnTranslateId.addEventListener('click', () => {
    const languageCode = languageCodeId.value;
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        helloId.textContent = data.hello;
      });
  });
});
