var AddFriendView = function (service) {
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

    //queries server with friend username. Adds as friend if username found, throws exception otherwise
    this.findFriend = function(username) {
        debugAlert("got to findFriend!");
        debugAlert("username: " + username);
        var user = getUser();
        var user_id = user.id;
        var api = 'search/find_user';
        var params = new Array();
        params['user_id'] = user_id;
        params['username'] = username;

        var searchParser = function(obj) {
            if (typeof obj.exception === "undefined") {
                var friendUsername = obj.username;
                var friend_id = obj.user_id;
                //asks if they want to add the user
                function onConfirm(buttonIndex) {
                    if(buttonIndex === 1) {
                        var addFriendView = new AddFriendView();
                        addFriendView.addFriend(friend_id);
                    } else {
                        setSpinnerVisibility(false);
                    }
                }
                showNotification("Would you like to add " + friendUsername + " as a friend?",onConfirm,
                friendUsername + " has been found!",['Yes','No']);

            } else {
                //shows exception message
                showAlert(obj.exception);
                setSpinnerVisibility(false);
            }
        };

        serverCaller(api, params, searchParser, null, null);

    };

    //queries server with self id and friend id. Updates friends field for user(?)
    this.addFriend = function(friend_id) {
        var user = getUser();
        var user_id = user.id;
        var api = 'friend/add_friend';
        var params = new Array();
        params['user_id'] = user_id;
        params['friend_id'] = friend_id;

        var addFriendParser = function(obj) {
            if (typeof obj.exception === "undefined") {
                setFriends(obj.friends);
                showAlert("Friend added!");
                document.getElementById("friend_search").value = "";
                setSpinnerVisibility(false);
            } else {
                //shows exception message
                showAlert(obj.exception);
                setSpinnerVisibility(false);
            }
        };

        serverCaller(api, params, addFriendParser, null, null);

    };

    this.backToMain = function() {
        window.location.reload();
        window.location="friends.html";
    }

    this.initialize();
}