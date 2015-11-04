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
    var callback = function(ongoing) {
        if (ongoing) {
            continueGame(friendId);
        } else {
            startNewGame(friendId);
        }
    };

    hasOngoingGame(friendId, callback);
};

// returns true if there is an ongoing game with a friend (also saves game to localStorage), false otherwise
function hasOngoingGame(friendId, callback) {
    var user = getUser();
    var userId = user.id;
    var api = 'game/get_game_status';
    var params = 'user_id=' + encodeURIComponent(userId) + '&friend_id=' + encodeURIComponent(friendId);

    var checkParser = function(result) {
        debugAlert("Called GameParser!");
        var obj = JSON.parse(result);
        if (typeof obj.exception === "undefined") {
            var game = makeGame(obj);
            var user = getUser();
            var userGames = user.games;
            userGames.push(game);
            user.games = userGames;

            window.localStorage.removeItem('activeGame');
            window.localStorage.setItem('activeGame',JSON.stringify(game));

            callback(true);
        } else {
            callback(false);
        }
    };

    var serverCaller = new ServerCaller(api,params,checkParser);

};

// figures out which screen to go to based on is_photographer and is_turn, then goes to screen
function continueGame(friendId) {
    //go to view
    toGameView();
};

// queries server to get new game object. Then parses game and add to list of games in user
function startNewGame(friendId) {
    var user = getUser();
    var userId = user.id;
    var api = 'game/start_new_game';
    var params = 'user_id=' + encodeURIComponent(userId) + '&friend_id=' + encodeURIComponent(friendId);
    var callGameView = function() {
        toGameView();
    };
    var serverCaller = new ServerCaller(api,params,GameParser,callGameView);
};

function toGameView() {
    window.location="game.html";
}

// gets the game that was just started, goes to photographer screen, displays word on screen
// Note: Yuki, definitely feel free to rename this function
var displayWord = function() {
    var activeGame = getActiveGame();
    var currentWord = activeGame.curr_word; //here's the word to display
    showAlert(currentWord); // TODO change this to debugAlert later
    return currentWord;
};

//gets the active game with the selected friend from localstorage and returns an game object
var getActiveGame = function(){
    var retrievedGame =  window.localStorage.getItem('activeGame');
    var parsedGame = JSON.parse(retrievedGame);
    return parsedGame;
};
