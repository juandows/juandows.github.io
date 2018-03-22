function script(){
    loadJSON('data/champions.json', function(response) {
        // Parse JSON string into object
        var champions = JSON.parse(response);
        console.log(champions);
    });
}
