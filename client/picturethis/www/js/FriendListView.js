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
var getFriendListObjects = function(friendTpl){
	var user = getUser();
	var api = 'poll/update';
	var params = new Array();
	params['user_id'] = user.id;
	var friendList = [];

	var friendListObjectParser = function(result) {
		var obj = JSON.parse(result);
		if (typeof obj.exception === "undefined") {

			//var friendList = [];
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

			//console.log(JSON.stringify(friendList));

			var activeFriends = [];
            var inactiveFriends = [];

            if (friendList.length != 0) {
                for (i=0; i<friendList.length; i++) {
                    if (friendList[i].active_game==false) {
                        inactiveFriends.push(friendList[i]);
                    }
                    else {
                        activeFriends.push(friendList[i]);
                    }
                }
            }
			console.log(activeFriends.length);
			console.log(inactiveFriends.length);

			if (friendList.length != 0) {
                var tableul = document.createElement('ul');
                tableul.className = "friends_list";

			if (activeFriends.length != 0) {
                var activeHeader = document.createElement("li");
                activeHeader.className = "active_friends";
                var activeHeaderText = document.createTextNode("Active");
                activeHeader.appendChild(activeHeaderText);
                tableul.appendChild(activeHeader);
                for (i = 0; i < activeFriends.length; i++) {
                    var tableli = document.createElement("li");
                    tableli.className = "friend_element";
                    friendUserName = activeFriends[i].friend_username;
                    var tabletext = document.createTextNode(friendUserName);
                    var tablebutton = document.createElement("button");

                    var friendId = activeFriends[i].friend_id;
                    tablebutton.setAttribute("onClick", "play("+friendId.toString()+");");
                    var buttontext;
                    if (activeFriends[i].is_photographer == true) {
                        tablebutton.className = "play_button snap";
                        buttontext = document.createTextNode("Snap!");
                    }
                    else if (activeFriends[i].is_photographer == false && activeFriends[i].is_turn == true) {
                        tablebutton.className = "play_button guess";
                        buttontext = document.createTextNode("Guess!");
                    }
                    else {
                        tablebutton.className = "play_button waiting";
                        buttontext = document.createTextNode("Waiting...");
                    }
                    tablebutton.appendChild(buttontext);
                    tableli.appendChild(tabletext);
                    tableli.appendChild(tablebutton);
                    tableul.appendChild(tableli);
                }
            }
            if (inactiveFriends.length != 0) {
                var inactiveHeader = document.createElement("li");
                inactiveHeader.className = "inactive_friends";
                var inactiveHeaderText = document.createTextNode("Inactive");
                inactiveHeader.appendChild(inactiveHeaderText);
                tableul.appendChild(inactiveHeader);
                for (i = 0; i < inactiveFriends.length; i++) {
                    var tableli = document.createElement("li");
                    tableli.className = "friend_element";
                    friendUserName = inactiveFriends[i].friend_username;
                    var tabletext = document.createTextNode(friendUserName);
                    var tablebutton = document.createElement("button");
                    tablebutton.className = "play_button new_game";

                    var friendId = inactiveFriends[i].friend_id;
                    tablebutton.setAttribute("onClick", "play("+friendId.toString()+");");
                    var buttontext = document.createTextNode("Start!");
                    tablebutton.appendChild(buttontext);
                    tableli.appendChild(tabletext);
                    tableli.appendChild(tablebutton);
                    tableul.appendChild(tableli);
                    }
                }
             friendTpl.appendChild(tableul);
		}
		} else {
			//shows exception message
			showAlert(obj.exception);
			setSpinnerVisibility(false);
		}
	};

	serverCaller(api, params, friendListObjectParser, null, null);

}