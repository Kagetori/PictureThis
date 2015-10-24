var LoginView = function (service) {
	this.myService = service;
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
            if ( typeof xmlhttp.overrideMimeType != 'undefined') { 
                xmlhttp.overrideMimeType('application/json'); 
            }
        }
        else {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.open('GET', 'http://picturethis.brianchau.ca/api/login/login?username=' + username + '&password=' + password, true);
        xmlhttp.send();

        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                // do something with the results
                if (xmlhttp.responseText != "undefined"){
                    showAlert(xmlhttp.responseText);

                    // This is the parsed JSON object
                    var obj = JSON.parse(xmlhttp.responseText);

                    if (typeof obj.exception === "undefined") {
                    	showAlert("there's a user!");
              			showAlert(myService.user);
                    	//myUser.username = obj.username;
                    	//showAlert(obj.username);

//                    	service.user.id = obj.user_id;
//                    	showAlert(service.user.id);
//
//                    	service.user.auth_token = obj.auth_token;
//                    	showAlert(service.user.auth_token);
//
//                    	service.user.friends = obj.friends;
//                    	showAlert(service.user.friends);
//
//                    	if (typeof obj.games != "undefined") {
//                    		service.user.games = obj.games;
//                    	}

                    	} else {
                    	showAlert(obj.exception);
                    	}
                }
            } else {
                // wait for the call to complete
            }
        };
        //call next page? -> if (username != null) blah

	};

	this.initialize();
}