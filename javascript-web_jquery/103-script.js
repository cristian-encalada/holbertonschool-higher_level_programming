$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation () {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();

    // Make a GET request to the HelloSalut API
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      // Ensure that any special characters are properly decoded
      const decoded = $('<div></div>').html(data.hello).text();
      $('#hello').text(decoded);
    });
  }

  // Click event for the Translate button
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Enter key event for the language code input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
