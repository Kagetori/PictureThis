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
                tableul.className = "table-view";

			if (activeFriends.length != 0) {
                for (i = 0; i < activeFriends.length; i++) {
                    var tableli = document.createElement("LI");
                    tableli.className = "table-view-cell";
                    friendUserName = activeFriends[i].friend_username;
                    var tabletext = document.createTextNode(friendUserName);
                    var tablebutton = document.createElement("BUTTON");
                    tablebutton.className = "btn btn-primary";

                    var friendId = activeFriends[i].friend_id;
                    tablebutton.setAttribute("onClick", "play("+friendId.toString()+");");
                    var buttontext;
                    if (activeFriends[i].is_photographer == true) {
                        buttontext = document.createTextNode("PICTURE!");
                    }
                    else if (activeFriends[i].is_photographer == false && activeFriends[i].is_turn == true) {
                        buttontext = document.createTextNode("GUESS!");
                    }
                    else {
                        buttontext = document.createTextNode("WAITING");
                    }
                    tablebutton.appendChild(buttontext);
                    tableli.appendChild(tabletext);
                    tableli.appendChild(tablebutton);
                    tableul.appendChild(tableli);
                }
            }
            if (inactiveFriends.length != 0) {
                for (i = 0; i < inactiveFriends.length; i++) {
                    var tableli = document.createElement("LI");
                    tableli.className = "table-view-cell";
                    friendUserName = inactiveFriends[i].friend_username;
                    var tabletext = document.createTextNode(friendUserName);
                    var tablebutton = document.createElement("BUTTON");
                    tablebutton.className = "btn btn-primary";

                    var friendId = inactiveFriends[i].friend_id;
                    tablebutton.setAttribute("onClick", "play("+friendId.toString()+");");
                    var buttontext = document.createTextNode("START");
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