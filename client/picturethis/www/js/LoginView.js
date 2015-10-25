var LoginView = function (service) {
	this.myService = service;
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

    //logs user in
	this.userLogin = function(username,password) {
	    var url = 'http://picturethis.brianchau.ca/api/login/login?username=' + username + '&password=' + password;
        var serverCaller = new ServerCaller(url,UserParser);
        };

	this.initialize();
}