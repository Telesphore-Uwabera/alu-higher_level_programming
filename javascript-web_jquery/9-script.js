document.addEventListener('DOMContentLoaded', function() {
  fetch('https://fourtonfish.com/hellosalut/?lang=fr')
    .then(response => response.json())
    .then(data => {
      var helloDiv = document.getElementById('hello');
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.log('Error:', error);
    });
});
