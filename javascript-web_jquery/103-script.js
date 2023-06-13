$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keydown(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
