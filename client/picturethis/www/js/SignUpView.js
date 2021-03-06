var SignUpView = function (service) {
    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };

    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    //creates new account with username and password
    this.createAccount = function(username, password) {
        window.localStorage.clear();

        var api = 'login/create_user';
        var params = new Array();
        params['username'] = username;
        params['password'] = password;

        var create = function() {
            var signUpView = new SignUpView();
            signUpView.LoginFriendView(username);
        };
        serverCaller(api, params, UserParser, create, null);
    };

    this.LoginFriendView = function(username) {
        var user = getUser();
        if (user.username == username) {
            window.location="friends.html";
        } else {
            showAlert("Try again");
        }
    }

    this.backToLogin = function() {
        router.load('#log in');
    }

    this.initialize();
}
