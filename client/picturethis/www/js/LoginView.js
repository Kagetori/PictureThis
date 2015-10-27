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
	    var login = function() {
	    	var loginView = new LoginView();
	    	loginView.LoginFriendView(username);
	    };
        var serverCaller = new ServerCaller(url,UserParser,login);
       };

    this.LoginFriendView = function(username) {
    	var user = getUser();
        if (user.username == username) {
        	window.location="index2.html";
            } else {
            showAlert("Login failed, username and/or password don't match.")}
    }

	this.initialize();
}