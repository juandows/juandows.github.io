function script(){
    loadJSON('data/champions.json', function(response) {
        // Parse JSON string into object
        var champions = JSON.parse(response)["champions"];
        console.log(champions);
        var html = '';
        for (var i = 0, len = champions.length; i < len; i++) {
            html = '<div id="champion'+champions[i]['id']+'" class="champion"></div>';
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
        callback(champion["id"], '<p>' + champion["id"]+' '+championData["name"]+ '</p>');
    });
}
