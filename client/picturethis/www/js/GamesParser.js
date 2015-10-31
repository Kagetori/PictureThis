// parses all games in list and saves it in games field in user
var GamesParser = function(result) {
   showAlert("Called GamesParser!");
   var obj = JSON.parse(result);
   if (typeof obj.exception === "undefined") {
        var games = obj.games;
        var user = getUser();
        var parsedGames = {};
        for (var game in games) {
            makeGame(game);
            parsedGames.add(game);
        };
        user.games = parsedGames;
   } else {
         showAlert(obj.exception);
         };
   showAlert("Finished GamesParser!");
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
             game.is_turn = obj.curr_word;
          };

     if (typeof obj.curr_word != "undefined") {
        game.curr_word = obj.curr_word;
     };

    if (typeof obj.is_photographer != "undefined") {
        game.my_round = obj.is_photographer;
    };

    return game;
};
