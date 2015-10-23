var LoginView = function (service) {
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

	this.userLogin = function(username,password) {
		showAlert("Name: " + username + " Pass: " + password, "Login");
	};

	this.initialize();
}