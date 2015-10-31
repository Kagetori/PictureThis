
var showAlert = function (message, title) {
    // change this to false if want all alerts to be disabled
    var ENABLE_ALERTS = true;

    if (ENABLE_ALERTS) {
        if (navigator.notification) {
            navigator.notification.alert(message, null, title, 'OK');
        } else {
            alert(title ? (title + ": " + message) : message);
        }
    }
};
