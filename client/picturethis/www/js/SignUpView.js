var SignUpView = function (service) {
	this.initialize = function () {
		// Define a div wrapper for the view (used to attach events)
		this.$el = $('<div/>');
//		this.$el.on('keyup','.submit', this.createUser);
		this.render();
	};
	
//	this.initialize();
	this.render = function() {
		this.$el.html(this.template());
		return this;
	};

	this.createAccount = function(username, password) {
		showAlert("Username: " + username + "  Password: " + password, "Create");
	};

	this.initialize();
}