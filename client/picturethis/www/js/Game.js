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
            function onConfirm(buttonIndex) {
                if (buttonIndex === 1) {
                    startNewGame(friendId);
                } else {
                    setSpinnerVisibility(false);
                }
            }

            showNotification('Start a new game with your friend?',onConfirm,'New Game',['Yes','No']);
        }
    };

    hasOngoingGame(friendId, callback);
};

// returns true if there is an ongoing game with a friend (also saves game to localStorage), false otherwise
function hasOngoingGame(friendId, callback) {
    var user = getUser();
    var userId = user.id;
    var api = 'game/get_game_status';
    var params = new Array();
    params['user_id'] = userId;
    params['friend_id'] = friendId;

    var checkParser = function(obj) {
        debugAlert("Called checkParser!");
        var game = makeGame(obj);

        window.localStorage.removeItem('activeGame');
        window.localStorage.setItem('activeGame',JSON.stringify(game));

        callback(obj.active);
    };

    serverCaller(api, params, checkParser, null, function() {
        callback(false);
    });

};

// figures out which screen to go to based on is_photographer and is_turn, then goes to screen
function continueGame(friendId) {
    toGameView();
};

// queries server to get new game object. Then parses game and add to list of games in user
function startNewGame(friendId) {
    var user = getUser();
    var userId = user.id;
    var api = 'game/start_new_game';
    var params = new Array();
    params['user_id'] = userId;
    params['friend_id'] = friendId;

    var callGameView = function() {
        toGameView();
    };
    serverCaller(api, params, GameParser, callGameView, null);
};

function toGameView() {
    window.location="game.html";
}

// gets the game that was just started, goes to photographer screen, displays word on screen
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
