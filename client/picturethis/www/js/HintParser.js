var HintParser = function(result) {
    debugAlert("called HintParser!");
    var obj = JSON.parse(result);

    if (typeof obj.exception === "undefined") {
        var hint = obj.hint;
        debugAlert(hint);
    } else {
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};