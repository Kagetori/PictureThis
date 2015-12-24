var AutoLoginView = function (service) {
    this.myService = service;

    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();

        // Auto login the user if possible
        if (getLoginToken()) {
            var api = 'login/token_login';
            var params = new Array();
            params['user_id'] = getUser().id;
            params['login_token'] = getLoginToken();
            console.log(params);
            serverCaller(api, params, UserParser, function() {
                window.location="friends.html";
            }, function() {
                router.load('#log in');
            });

        } else {
            router.load('#log in');
        }
    };
    
    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    this.initialize();
}
