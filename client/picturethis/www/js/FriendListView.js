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
	//I'm not exactly sure what we need for this page but I assume we need a list of friends
	this.getFriends = function(){
		var user = getUser();
        //friends is the list of the user's friends
        var friends = user.friends;
	}

	this.initialize();
}