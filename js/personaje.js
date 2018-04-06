function script(){
  var id = findGetParameter("id");


  loadJSON('data/champion'+id+'.json', function(response) {
      var championData = JSON.parse(response);
      console.log(championData);
      showHtml('nombre', championData["name"]);
      showHtml('titulo', championData["title"]);
      var imagen = championData["image"]["full"];
      imagen = imagen.substr(0, imagen.length-4);
      showHtml('imagen', '<img src="http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'+imagen+'_0.jpg">');
      showHtml('lore', championData["lore"]);
      var pasiva = "<div><h2>Pasiva, "+championData["passive"]["name"]+"</h2>"
          +'<img src="http://ddragon.leagueoflegends.com/cdn/6.24.1/img/passive/'
          +championData["passive"]["image"]["full"]
          +'">'+championData["passive"]["description"]+"</div>";
      var habilidades = pasiva;
      console.log(habilidades);
      showHtml('habilidades', habilidades);
  });

}
