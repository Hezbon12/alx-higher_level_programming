$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('DIV#hello').text(data.name);
});
