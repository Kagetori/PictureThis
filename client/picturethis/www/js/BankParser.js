var BankParser = function(result) {
    debugAlert("Called BankParser!");
    var obj = JSON.parse(result);

    if (typeof obj.exception === "undefined") {
        var stars = obj.stars;
        debugAlert("You have " + stars + " stars");
    } else {
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};