var HintParser = function(result) {
    debugAlert("Called HintParser!");
    var obj = JSON.parse(result);

    if (typeof obj.exception === "undefined") {
        var word_class = obj.word_class;
        var word_category = obj.word_category;
        debugAlert(word_class);
        debugAlert(word_category);
    } else {
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};