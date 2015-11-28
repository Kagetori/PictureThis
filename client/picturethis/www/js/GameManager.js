// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
    var service = new PictureThisService();

	var user_score = getScore();
	var user_stars = getStars();
	console.log(user_score);
    console.log(user_stars);

    var game = getActiveGame();

    var isPhotographer = game.is_photographer;
    var isTurn = game.is_turn;
    var currentWord = game.curr_word; //here's the word to display

    TakePictureView.prototype.template = Handlebars.compile($("#takepicture-tpl").html());
    WaitingView.prototype.template = Handlebars.compile($("#waiting-tpl").html());
    GuessView.prototype.template = Handlebars.compile($("#guess-tpl").html());

    var score_stars = {score: user_score, stars: user_stars};
    var score_stars_word = ({score: user_score, stars: user_stars, word: currentWord});

    service.initialize().done(function () {
    	if (isPhotographer && isTurn){
    //		$('#main_page').html(new TakePictureView(word).render().$el); //for no routing
    			router.addRoute('', function () {
            		$('#main_page').html(new TakePictureView(score_stars_word).render().$el);
            	});
            	router.addRoute('wait view', function () {
            		$('#main_page').html(new WaitingView(score_stars).render().$el);
            	});
            	router.start();
    	} else if (!isTurn) {
    		$('#main_page').html(new WaitingView(score_stars).render().$el);
    	} else if (!isPhotographer && isTurn){
    		$('#main_page').html(new GuessView(score_stars).render().$el);
    		addLetters();
            getGuessImage();
            populateGuessBlocks(currentWord);
            numStars();
    	}
    });

    /* --------------------------------- Event Registration -------------------------------- */
    // note: it may be easier to make nagivator.notification a seperate function
		document.addEventListener('deviceready', function () {
			if (navigator.notification) { // Override default HTML alert with native dialog
				window.alert = function (message) {
					navigator.notification.alert(
						message,    // message
						null,       // callback
						"Workshop", // title
						'OK'        // buttonName
					);
				};
			}
		}, false);

    /* ---------------------------------- Local Functions ---------------------------------- */

}());