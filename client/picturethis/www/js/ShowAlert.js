
var showAlert = function (message, title) {
    if (navigator.notification) {
        navigator.notification.alert(message, null, title, 'OK');
    } else {
        alert(title ? (title + ": " + message) : message);
    }
};

var debugAlert = function (message, title) {
    // change this to false if want all debug alerts to be disabled
    var ENABLE_DEBUG_ALERTS = false;

    if (ENABLE_DEBUG_ALERTS) {
        showAlert(message, title);
    }
};

var showNotification = function(message, callback, title, labels) {
    if (navigator.notification) {
        navigator.notification.confirm(
             message,   // message
             callback,  // callback to invoke with index of button pressed
             title,     // title
             labels     // buttonLabels
        )
    } else {
        alert("Notification Error");
    }
};
