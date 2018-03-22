function script(){
    loadJSON('data/champions.json', function(response) {
        // Parse JSON string into object
        var champions = JSON.parse(response)["champions"];
        console.log(champions);
        var html = '';
        for (var i = 0, len = champions.length; i < len; i++) {
            html = '<a href="personaje.html?id='+champions[i]['id']+'"><div id="champion'+champions[i]['id']+'" class="champion"></div></a>';
            addHtml('champions', html);
            getChampionHtml(champions[i], function(id, htmlChampion){
                showHtml('champion'+id, htmlChampion);
            });
        }

    });
}

function getChampionHtml(champion, callback){
    loadJSON('data/champion'+champion["id"]+'.json', function(response) {
        var championData = JSON.parse(response);
        console.log(championData);
        var html = '<div><img src="http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/'+championData["image"]["full"]+'"></div>';
        html += '<div>' + champion["id"]+'</div><div>'+championData["name"]+ '</div>';
        callback(champion["id"], html);
    });
}
