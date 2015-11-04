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
	navigator.camera.getPicture(onSuccess, onFail, { quality: 50,
        destinationType: Camera.DestinationType.FILE_URI
    });

	document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.camera);
    }

	if (!navigator.camera) {
          showAlert("Camera API not supported", "Error");
          return;
      }

    function clearCache() {
        navigator.camera.cleanup();
    }

	navigator.camera.getPicture(onSuccess, onFail, {
		quality: 50,
        destinationType: Camera.DestinationType.FILE_URI,
        sourceType : Camera.PictureSourceType.CAMERA });

    function onSuccess(imageURI) {
        var myImage = document.getElementById('myImage');
        myImage.src = imageURI;
    }

    function onFail(message) {
        debugAlert('Failed because: ' + message);
    }
};
/*
var pictureSource;   // picture source
var destinationType; // sets the format of returned value
 
document.addEventListener("deviceready", onDeviceReady, false);
 
function onDeviceReady() {
    pictureSource = navigator.camera.PictureSourceType;
    destinationType = navigator.camera.DestinationType;
}
 
function clearCache() {
    navigator.camera.cleanup();
}
 
var retries = 0;
function onCapturePhoto(fileURI) {
    var win = function (r) {
        clearCache();
        retries = 0;
        alert('Done!');
    }
 
    var fail = function (error) {
        if (retries == 0) {
            retries ++
            setTimeout(function() {
                onCapturePhoto(fileURI)
            }, 1000)
        } else {
            retries = 0;
            clearCache();
            alert('Ups. Something wrong happens!');
        }
    }
 
    var options = new FileUploadOptions();
    options.fileKey = "file";
    options.fileName = fileURI.substr(fileURI.lastIndexOf('/') + 1);
    options.mimeType = "image/jpeg";
    options.params = {}; // if we need to send parameters to the server request
    var ft = new FileTransfer();
    ft.upload(fileURI, encodeURI("http://localhost/upload"), win, fail, options);
}
 
function capturePhoto() {
    navigator.camera.getPicture(onCapturePhoto, onFail, {
        quality: 100,
        destinationType: destinationType.FILE_URI
    });
}
 
function onFail(message) {
    alert('Failed because: ' + message);
}*/