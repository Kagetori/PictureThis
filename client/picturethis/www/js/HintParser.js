var HintParser = function(obj) {
    debugAlert("Called HintParser!");

    var wordClass = obj.word_class;
    var wordCategory = obj.word_category;

    window.localStorage.removeItem('wordClass');
    window.localStorage.setItem('wordClass', JSON.stringify(wordClass));

    window.localStorage.removeItem('wordCategory');
    window.localStorage.setItem('wordCategory', JSON.stringify(wordCategory));
};
