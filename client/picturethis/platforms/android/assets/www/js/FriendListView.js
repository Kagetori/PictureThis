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