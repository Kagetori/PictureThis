var FriendListView = function (service) {

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

	this.logout = function() {
//		var nullUser = new User("","","","","","");
//		window.localStorage.setItem('userObject', nullUser);
		window.localStorage.clear();
		window.location="login.html";
	}

	this.initialize();
}
// returns parsed friendListObjects
var getFriendListObjects = function(){
	debugAlert("got to getFriendListObjects");
	var user = getUser();
	var api = 'poll/update';
	var params = new Array();
	params['user_id'] = user.id;

	var friendListObjectParser = function(result) {
		debugAlert("got to PARSER!");
		console.log(result);
		var obj = JSON.parse(result);
		console.log(obj);
		if (typeof obj.exception === "undefined") {
		//loop
			var friendList = [];
			var objects = obj.polls;

			for (var i = 0; i < objects.length; i++) {
                        var friendListObject = new FriendListObject();
                        var object = objects[i];

						friendListObject.friend_username = object.friend_username;
						friendListObject.friend_id = object.friend_id;
						friendListObject.active_game = object.active_game;
						friendListObject.is_turn = object.is_turn;
						friendListObject.is_photographer = object.is_photographer;

                        friendList.push(friendListObject);
                    }
			return friendList;

		} else {
			//shows exception message
			showAlert(obj.exception);
			setSpinnerVisibility(false);
		}
	};
	serverCaller(api, params, friendListObjectParser, null, null);
}