function script(){
  var span = document.getElementById('nombre');
  while( span.firstChild ) {
    span.removeChild( span.firstChild );
  }
  var id = findGetParameter("id");
  span.appendChild( document.createTextNode(id+"personaje") );
}
