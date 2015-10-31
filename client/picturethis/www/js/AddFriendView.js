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
		showAlert("got to findFriend!");
		showAlert("username: " + username);
		var url = 'http://picturethis.brianchau.ca/api/search/find_user?username=' + username;

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
					};
			};

		var serverCaller = new ServerCaller(url,searchParser);

	};

	//queries server with self id and friend id. Updates friends field for user(?)
	this.addFriend = function(friend_id) {
    		var user = getUser();
    		var user_id = user.id;
    		var url = 'http://picturethis.brianchau.ca/api/friend/add_friend?user_id=' + user_id + '&friend_id=' + friend_id;
    		var addFriendParser = function(result) {
    			var obj = JSON.parse(result);
    			   if (typeof obj.exception === "undefined") {
    					user.friends = obj.friends;
    					showAlert("Friend added!");

    				} else {
    					//shows exception message
    					showAlert(obj.exception);
    					};
    		};

    		var serverCaller = new ServerCaller(url,addFriendParser);

    	};

	this.backToMain = function() {
		window.location.reload();
		window.location="index2.html";
    	}

	this.initialize();
}