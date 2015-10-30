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
};

//checks if there's an ongoing game with the friend. Continues game if there is, else starts a new game.
function playGame(friendId){
	showAlert(friendId);

    if (hasOngoingGame(friendId)) {
	//TODO: continue current game (go to appropriate screen)
	    continueGame(friendId);
	} else {
	    startNewGame(friendId);
	}
};

// returns true if there is an ongoing game with a friend (also saves game to localStorage), false otherwise
function hasOngoingGame(friendId) {
	var user = getUser();
	var userGames = user.games;
	for (var game in userGames) {
	    if(game.friend_id === friendId && game.active) {
	        window.localStorage.removeItem('activeGame');
            window.localStorage.setItem('activeGame',JSON.stringify(game));
            return true;
	    }
	}
	return false;
};

// figures out which screen to go to based on is_photographer and is_turn, then goes to screen
function continueGame(friendId) {

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
