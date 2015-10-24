var LoginView = function (service) {
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

	this.userLogin = function(username,password) {
        var xmlhttp;
        if (window.XMLHttpRequest){
            xmlhttp = new XMLHttpRequest();
        }
        else {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.open('GET', 'http://picturethis.brianchau.ca/api/login/login?username=' + username + '&password=' + password, true);
        xmlhttp.send();
        console.log(xmlhttp);
        console.log(xmlhttp.responseText);
        if (xmlhttp.responseText != "undefined"){
            var obj = JSON.parse(xmlhttp.responseText);
            showAlert(obj);
        }
	};

	this.initialize();
}