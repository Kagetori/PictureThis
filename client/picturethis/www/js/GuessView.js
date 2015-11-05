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
        if (currentWord != guess) {
            showAlert("Your guess is incorrect. Try again.");
        } else {
            showAlert("Your guess is correct! Continue!");

            var user = getUser();
            var user_id = user.id;
            console.log(user_id);
            var game_id = currentGame.game_id;
            console.log(game_id);
            console.log(guess);
            var api = 'game/validate_guess';
            var params = new Array();
            params['user_id'] = user_id;
            params['game_id'] = game_id;
            params['guess'] = guess;

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
            showAlert("Game Finished!" + '\n' + "(You can start another game from the main page)");
            window.location="friends.html";
        }
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
