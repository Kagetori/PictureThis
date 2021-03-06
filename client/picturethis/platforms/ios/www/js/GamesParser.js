// parses all games in list and saves it in games field in user
var GamesParser = function(obj) {
    debugAlert("Called GamesParser!");

    var user = getUser();

    var parsedGames = [];
    var games = obj.games;

    for (var i = 0; i < games.length; i++) {
        var game = games[i];
        var newGame = makeGame(game);
        parsedGames.push(newGame);
    }

    user.games = parsedGames;
 };

// parses one game and adds it to the games field in user
 var GameParser = function(obj) {
    debugAlert("Called GameParser!");

    var game = makeGame(obj);

    window.localStorage.removeItem('activeGame');
    window.localStorage.setItem('activeGame',JSON.stringify(game));
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

    if (obj.hasOwnProperty('is_turn')) {
        game.is_turn = obj.is_turn;
    }

    if (obj.hasOwnProperty('curr_word')) {
        game.curr_word = obj.curr_word;
    }

    if (obj.hasOwnProperty('is_photographer')) {
        game.is_photographer = obj.is_photographer;
    }

    return game;
};
