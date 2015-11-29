var LoginView = function (service) {
    this.myService = service;

    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };
    
    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    //logs user in
    this.userLogin = function(username,password) {
        window.localStorage.clear();

        var api = 'login/login';
        var params = new Array();
        params['username'] = username;
        params['password'] = password;

        serverCaller(api, params, UserParser, function() {
            window.location="friends.html";
        }, function() {
            showAlert("Login failed, username and/or password don't match.");
            setSpinnerVisibility(false);
        });
    };

    this.initialize();
}
