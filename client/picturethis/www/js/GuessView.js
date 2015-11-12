var GuessView = function (service) {
    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };

    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    this.sendGuess = function(guess) {
        var currentGame = getActiveGame();
        var currentWord = currentGame.curr_word;
        console.log(currentWord);
        var cleanGuess = guess.trim().toLowerCase();
        if (currentWord != cleanGuess) {
            showAlert("Your guess is incorrect. Try again.");
        } else {
            showAlert("Your guess is correct! Continue!");

            var user = getUser();
            var user_id = user.id;
            console.log(user_id);
            var game_id = currentGame.game_id;
            console.log(game_id);
            console.log(cleanGuess);
            var api = 'game/validate_guess';
            var params = new Array();
            params['user_id'] = user_id;
            params['game_id'] = game_id;
            params['guess'] = cleanGuess;

            var picView = function(){
                var guessView = new GuessView();
                guessView.toPictureView();
            };

            serverCaller(api, params, GameParser, picView, null);
        }
    }

    this.toPictureView = function() {
        var currentGame = getActiveGame();
        if (currentGame.active) {
            window.location.reload();
        } else {
            var game = getActiveGame();
            var friend_id = game.friend_id;

            function onConfirm(buttonIndex) {
                if(buttonIndex === 1) {
                    startNewGame(friend_id);
                } else {
                    window.location="friends.html";
                }
            };

            showNotification('Would you like to start a new game?',onConfirm,'Game Finished!',['Yes','No']);
        }
    }

    this.getHint = function() {
        var currentGame = getActiveGame();
        var currentWord = currentGame.curr_word;
        var params = new Array();
        var api = 'word_prompt/get_word_prompt';
        params['word'] = currentWord;

        serverCaller(api, params, HintParser, null, null);
    }

    this.initialize();
}

function getGuessImage() {
    var user = getUser();
    var user_id = user.id;
    var currentGame = getActiveGame();
    var game_id = currentGame.game_id;
    var params = new Array();
    params['user_id'] = user_id;
    params['game_id'] = game_id;

    serverCaller('game/get_picture', params, function(result) {
        document.getElementById('guess_img').src = result;
    }, null, null);
}
