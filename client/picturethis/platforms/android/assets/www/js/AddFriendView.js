var AddFriendView = function (service) {
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

	//queries server with friend username. Adds as friend if username found, throws exception otherwise
	this.findFriend = function(username) {
		debugAlert("got to findFriend!");
		debugAlert("username: " + username);
		var user = getUser();
		var user_id = user.id;
		var api = 'search/find_user';
        var params = 'user_id=' + encodeURIComponent(user_id) + '&username=' + encodeURIComponent(username);

		var searchParser = function(result) {
		   var obj = JSON.parse(result);
	   		if (typeof obj.exception === "undefined") {
				var friendUsername = obj.username;
				var friend_id = obj.user_id;
				//call add friend - they currently don't have a choice
				showAlert("Your friend " + friendUsername + " has been found!");
				var addFriendView = new AddFriendView();
				addFriendView.addFriend(friend_id);

			} else {
				//shows exception message
				showAlert(obj.exception);
                setSpinnerVisibility(false);
			}
		};

		var serverCaller = new ServerCaller(api,params,searchParser);

	};

	//queries server with self id and friend id. Updates friends field for user(?)
	this.addFriend = function(friend_id) {
		var user = getUser();
		var user_id = user.id;
		var api = 'friend/add_friend';
        var params = 'user_id=' + encodeURIComponent(user_id) + '&friend_id=' + encodeURIComponent(friend_id);
		var addFriendParser = function(result) {
			var obj = JSON.parse(result);
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

		var serverCaller = new ServerCaller(api,params,addFriendParser);

	};

	this.backToMain = function() {
		window.location.reload();
		window.location="friends.html";
    }

	this.initialize();
}