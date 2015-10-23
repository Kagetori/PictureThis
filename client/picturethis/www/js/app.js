// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
var service = new PictureThisService();
//var loginTpl = Handlebars.compile($("#login-tpl").html());
LoginView.prototype.template = Handlebars.compile($("#login-tpl").html());
SignUpView.prototype.template = Handlebars.compile($("#signup-tpl").html());
service.initialize().done(function () {
//    renderLoginView();
	router.addRoute('', function() {
		$('body').html(new LoginView(service).render().$el);
	});
	router.addRoute('sign up', function () {
		$('body').html(new SignUpView(service).render().$el);
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