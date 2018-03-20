function script(){
  var span = document.getElementById('nombre');
  while( span.firstChild ) {
    span.removeChild( span.firstChild );
  }
  span.appendChild( document.createTextNode("Xpersonaje") );
}
