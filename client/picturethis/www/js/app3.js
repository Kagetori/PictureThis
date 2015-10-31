// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
var service = new PictureThisService();

var retrievedGame =  window.localStorage.getItem('activeGame');
var parsedGame = JSON.parse(retrievedGame);

var isPhotographer = parsedGame.is_photographer;
var isTurn = parsedGame.is_turn;
var currentWord = parsedGame.curr_word; //here's the word to display

TakePictureView.prototype.template = Handlebars.compile($("#takepicture-tpl").html());
WaitingView.prototype.template = Handlebars.compile($("#waiting-tpl").html());
GuessView.prototype.template = Handlebars.compile($("#guess-tpl").html());
var word = ({word: currentWord});
service.initialize().done(function () {
	if (isPhotographer && isTurn){
		$('body').html(new TakePictureView(word).render().$el);
	} else if (!isTurn) {
		$('body').html(new WaitingView(service).render().$el);
	} else if (!isPhotographer && isTurn){
		$('body').html(new GuessView(service).render().$el);
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