var GuessView = function (service) {
	this.initialize = function () {
		// Define a div wrapper for the view (used to attach events)
		this.$el = $('<div/>');
		this.render();
	};
	
//	this.initialize();
	this.render = function() {
		this.$el.html(this.template());
		return this;
	};
	this.initialize();

	this.sendGuess = function(guess) {
		var currentGame = getActiveGame();
        var currentWord = currentGame.curr_word;
        console.log(currentWord);
        if (currentWord != guess) {
        	showAlert("Your guess is incorrect. Try again.");
        }
        else {
        	showAlert("Your guess is correct! Continue!");

			var user = getUser();
			var user_id = user.id;
			console.log(user_id);
			var game_id = currentGame.game_id;
			console.log(game_id);
			console.log(guess);
			var api = 'game/validate_guess';
			var params = 'user_id=' + encodeURIComponent(user_id) + '&game_id=' + encodeURIComponent(game_id) + '&guess=' + encodeURIComponent(guess);

			var picView = function(){
				var guessView = new GuessView();
				guessView.toPictureView();
			};

			var serverCaller = new ServerCaller(api,params,GameParser,picView);
        }
	}

	this.toPictureView = function() {
		window.location.reload();
	}
}