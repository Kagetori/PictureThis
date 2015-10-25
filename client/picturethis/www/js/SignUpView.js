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

	//creates new account with username and password
	this.createAccount = function(username, password) {
		var url = 'http://picturethis.brianchau.ca/api/login/create_user?username=' + username + '&password=' + password;
		var serverCaller = new ServerCaller(url,UserParser);
		};

	this.initialize();
}