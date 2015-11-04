//Takes return of server call and either parses&stores user in localStorage or shows an alert(exception)
var UserParser = function(result) {
   debugAlert("Called UserParser!");
   var obj = JSON.parse(result);

   if (typeof obj.exception === "undefined") {
        var myUser = new User();
        myUser.username = obj.username;
        myUser.id = obj.user_id;
        myUser.friends = obj.friends;
        myUser.auth_token = obj.auth_token;
        myUser.games = [];

        if (typeof obj.games != "undefined") {
            var parsedGames = [];
            var games = obj.games;

            for (var i = 0; i < games.length; i++) {
                var game = games[i];
                var newGame = makeGame(game);
                parsedGames.push(newGame);
            }
        }

        window.localStorage.clear();
        window.localStorage.setItem('userObject', JSON.stringify(myUser));

    } else {
        //shows exception message
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
}
