// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
var service = new PictureThisService();

FriendListView.prototype.template = Handlebars.compile($("#friendlist-tpl").html());
AddFriendView.prototype.template = Handlebars.compile($("#add-friend-tpl").html());
service.initialize().done(function () {
//    renderLoginView();

	router.addRoute('', function () {
		$('body').html(new FriendListView(service).render().$el);
	});
	router.addRoute('add friend', function () {
		$('body').html(new AddFriendView(service).render().$el);
	});

	router.start();

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
	
//function renderLoginView() {
//    $('body').html(loginTpl());
//}


}());