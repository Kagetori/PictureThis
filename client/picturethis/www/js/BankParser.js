var BankParser = function(obj) {
    debugAlert("Called BankParser!");

    if (typeof obj.exception === "undefined") {
        var stars = obj.stars;
        debugAlert("You have " + stars + " stars");
    } else {
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};