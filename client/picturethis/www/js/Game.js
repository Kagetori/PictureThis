// definition of the Game class
var Game = function(game_id, user_id, friend_id, active, is_photographer, is_turn, curr_round, curr_word, words_seen) {
    this.game_id = game_id;
    this.user_id = user_id;
    this.friend_id = friend_id;
    this.active = active;
    this.is_photographer = is_photographer;
    this.is_turn = is_turn;
    this.curr_round = curr_round;
    this.curr_word = curr_word;
    this.words_seen = words_seen;
}

//checks if there's an ongoing game with the friend. Continues game if there is, else starts a new game.
function playGame(friendId){
	showAlert(friendId);
	//TODO: check for ongoing game (query server for most recent results?)
	//TODO: continue current game (go to appropriate screen)
	//TODO: else start a new game
	startNewGame(friendId);
};

// queries server to get new game object. Then parses game and add to list of games in user
function startNewGame(friendId) {
    var user = getUser();
    var userId = user.id;
    var url = 'http://picturethis.brianchau.ca/api/game/start_new_game?user_id=' + userId + '&friend_id=' + friendId;
    var serverCaller = new ServerCaller(url,GameParser,callback);
    // gets the game that was just started, goes to photographer screen, displays word on screen
    // Note: Yuki, definitely feel free to rename this function
    var callback = function() {
        var activeGame = getActiveGame();
        var currentWord = activeGame.curr_word; //here's the word to display
    };
};

//gets the active game with the selected friend from localstorage and returns an game object
var getActiveGame = function(){
    var retrievedGame =  window.localStorage.getItem('activeGame');
    var parsedGame = JSON.parse(retrievedGame);
    return parsedGame;
};
