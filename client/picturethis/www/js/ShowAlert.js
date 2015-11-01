
var showAlert = function (message, title) {
    if (navigator.notification) {
        navigator.notification.alert(message, null, title, 'OK');
    } else {
        alert(title ? (title + ": " + message) : message);
    }
};

var debugAlert = function (message, title) {
    // change this to false if want all debug alerts to be disabled
    var ENABLE_DEBUG_ALERTS = true;

    if (ENABLE_DEBUG_ALERTS) {
        showAlert(message, title);
    }
};
