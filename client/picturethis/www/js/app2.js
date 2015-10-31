// We use an "Immediate Function" to initialize the application to avoid leaving anything behind in the global scope
(function () {

    /* ---------------------------------- Local Variables ---------------------------------- */
var service = new PictureThisService();

populateTable();

FriendListView.prototype.template = Handlebars.compile($("#friendlist-tpl").html());
AddFriendView.prototype.template = Handlebars.compile($("#add-friend-tpl").html());
service.initialize().done(function () {
//    renderLoginView();

	router.addRoute('', function () {
		$('body').html(new FriendListView(service).render().$el);
	});
	router.addRoute('add friend', function () {
		$('body').html(new AddFriendView(service).render().$el);
	});
	router.addRoute('main', function () {
    	$('body').html(new FriendListView(service).render().$el);
    });

	router.start();

});

    /* --------------------------------- Event Registration -------------------------------- */
// note: it may be easier to make nagivator.notification a seperate function
		document.addEventListener('deviceready', function () {
			if (navigator.notification) { // Override default HTML alert with native dialog
				window.alert = function (message) {
					navigator.notification.alert(
						message,    // message
						null,       // callback
						"Workshop", // title
						'OK'        // buttonName
					);
				};
			}
		}, false);

    /* ---------------------------------- Local Functions ---------------------------------- */

console.log(getFriends());

function populateTable() {
	var friends = getFriends();
	var friendlist = document.getElementById("friendlist-tpl");
		if (friends.length != 0) {
		var tableul = document.createElement('ul');
		tableul.className = "table-view";
			for (i = 0; i < friends.length; i++) {
				var tableli = document.createElement("LI");
				tableli.className = "table-view-cell";
				friendUserName = friends[i].username;
				var tabletext = document.createTextNode(friendUserName);
				var tablebutton = document.createElement("BUTTON");
				tablebutton.className = "btn btn-primary";

				//have to use username for now since id is undefined
				var friendId = friends[i].user_id;
				tablebutton.setAttribute("onClick", "play("+friendId.toString()+");");
				var buttontext = document.createTextNode("PLAY");
				tablebutton.appendChild(buttontext);
				tableli.appendChild(tabletext);
				tableli.appendChild(tablebutton);
				tableul.appendChild(tableli);
}
}
friendlist.appendChild(tableul);
console.log($("#friendlist-tpl").html());
}

function getFriends(){
	var user = getUser();
    return user.friends;
}

}());

