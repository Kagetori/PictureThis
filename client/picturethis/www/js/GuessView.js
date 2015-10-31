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
		var retrievedGame =  window.localStorage.getItem('activeGame');
        var parsedGame = JSON.parse(retrievedGame);
        var currentWord = parsedGame.curr_word;
        console.log(currentWord);
        if (currentWord != guess) {
        	window.alert("Your guess is incorrect. Try again.");
        }
        else {
        	window.alert("Your guess is correct! Continue!");

			//implementation of sending guess to server, and retrieving updated game (with new word and updated turn) from server
			//need callback to toPictureView() function

			//not sure if this function will bring user to the photographer view with the new word
			this.toPictureView();
        }
	}

	this.toPictureView = function() {
		window.location.reload();
	}
}