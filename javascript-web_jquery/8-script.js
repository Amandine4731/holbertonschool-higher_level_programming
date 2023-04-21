$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  $.each(data.results, function(index, movie) {
    $('#list_movies').append($('<li></li>').text(movie.title));
  });
});