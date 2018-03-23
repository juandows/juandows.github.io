function script(){
  var id = findGetParameter("id");


  loadJSON('data/champion'+id+'.json', function(response) {
      var championData = JSON.parse(response);
      console.log(championData);
      showHtml('nombre', championData["name"]);
      var imagen = championData["image"]["full"];
      imagen = imagen.substr(0, imagen.length-4);
      showHtml('imagen', '<img src="http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'+imagen+'_0.jpg">');
  });

}
