var LoginView = function (service) {
    this.myService = service;

    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };
    
//  this.initialize();
    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    //logs user in
    this.userLogin = function(username,password) {
        var api = 'login/login';
        var params = new Array();
        params['username'] = username;
        params['password'] = password;

        var login = function() {
            var loginView = new LoginView();
            loginView.LoginFriendView(username);
        };
        serverCaller(api, params, UserParser, login, null);
    };

    this.LoginFriendView = function(username) {
        var user = getUser();
        if (user.username == username) {
            window.location="friends.html";
        } else {
            showAlert("Login failed, username and/or password don't match.");
            setSpinnerVisibility(false);
        }
    }

    this.initialize();
}
