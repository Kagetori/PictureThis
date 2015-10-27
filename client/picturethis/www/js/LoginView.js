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

		setTimeout(this.LoginFriendView(username),100);
//		var retrievedUser =  window.localStorage.getItem('userObject');
//        var parsedUser = JSON.parse(retrievedUser);
//        if (parsedUser.username == username) {
//        	window.location="index2.html";
//        	} else {
//        	showAlert("Login failed, username and/or password don't match.")}
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