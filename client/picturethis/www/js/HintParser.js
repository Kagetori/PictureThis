var HintParser = function(obj) {
    debugAlert("Called HintParser!");

    if (typeof obj.exception === "undefined") {
        var wordClass = obj.word_class;
        var wordCategory = obj.word_category;

        window.localStorage.removeItem('wordClass');
        window.localStorage.setItem('wordClass', JSON.stringify(wordClass));

        window.localStorage.removeItem('wordCategory');
        window.localStorage.setItem('wordCategory', JSON.stringify(wordCategory));
    } else {
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};