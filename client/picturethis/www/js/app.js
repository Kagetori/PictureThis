// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
var service = new PictureThisService();
var loginTpl = Handlebars.compile($("#login-tpl").html());
service.initialize().done(function () {
    renderLoginView();
});

    /* --------------------------------- Event Registration -------------------------------- */
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
	
function renderLoginView() {
    $('body').html(loginTpl());
}

}());