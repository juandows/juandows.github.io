function script(){
  var span = document.getElementById('nombre');
  while( span.firstChild ) {
    span.removeChild( span.firstChild );
  }
  var id = findGetParameter("id");
  span.appendChild( document.createTextNode(id+"personaje") );
}

function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}
