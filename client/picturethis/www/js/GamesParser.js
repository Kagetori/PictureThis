// parses all games in list and saves it in games field in user
var GamesParser = function(result) {
   showAlert("Called GamesParser!");
   var obj = JSON.parse(result);

   if (typeof obj.exception === "undefined") {
        var user = getUser();

        var parsedGames = [];
        var games = obj.games;

        for (var i = 0; i < games.length; i++) {
            var game = games[i];
            var newGame = makeGame(game);
            parsedGames.push(newGame);
        };

        user.games = parsedGames;

   } else {
         showAlert(obj.exception);
                setSpinnerVisibility(false);
         };
 };

// parses one game and adds it to the games field in user
 var GameParser = function(result) {
    showAlert("Called GameParser!");
    var obj = JSON.parse(result);
    if (typeof obj.exception === "undefined") {
        var game = makeGame(obj);
        var user = getUser();
        var userGames = user.games;
        showAlert(userGames);
        userGames.push(game);
        user.games = userGames;

        window.localStorage.removeItem('activeGame');
        window.localStorage.setItem('activeGame',JSON.stringify(game));

    } else {
          showAlert(obj.exception);
                setSpinnerVisibility(false);
          };
  };

// returns a game object
var makeGame = function(obj) {
    var game = new Game();
     game.game_id = obj.game_id;
     game.user_id = obj.user_id;
     game.friend_id = obj.friend_id;
     game.active = obj.active;
     game.curr_round = obj.curr_round;
     game.words_seen = obj.words_seen;

     if (typeof obj.is_turn != "undefined") {
             game.is_turn = obj.is_turn;
          };

     if (typeof obj.curr_word != "undefined") {
        game.curr_word = obj.curr_word;
     };

    if (typeof obj.is_photographer != "undefined") {
        game.is_photographer = obj.is_photographer;
    };

    return game;
};

