var TakePictureView = function (word) {

	this.initialize = function () {
		// Define a div wrapper for the view (used to attach events)
		this.$el = $('<div/>');
		this.render();
	};
	
//	this.initialize();
	this.render = function() {
		this.$el.html(this.template(word));
		return this;
	};

	this.initialize();

	this.sendPicture = function() {
		var game = getActiveGame();
		var user_id = game.user_id;
		var game_id = game.game_id;
		debugAlert("User&Friend IDs: " + user_id + " " + game_id);

		var api = 'game/send_picture';
		var params = 'user_id=' + encodeURIComponent(user_id) + '&game_id=' + encodeURIComponent(game_id);
		var serverCaller = new ServerCaller(api,params,GameParser);
	};
}

function takePicture() {

	document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.camera);
    }

	if (!navigator.camera) {
          showAlert("Camera API not supported", "Error");
          return;
      }

	navigator.camera.getPicture(onSuccess, onFail, {
		quality: 50,
        destinationType: Camera.DestinationType.FILE_URI
    });

    function onSuccess(imageData) {
        var image = document.getElementById('myImage');
        image.src = "data:image/jpeg;base64," + imageData;
    }

    function onFail(message) {
        debugAlert('Failed because: ' + message);
    }
};
