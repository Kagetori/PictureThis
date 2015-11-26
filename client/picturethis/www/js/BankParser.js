var BankParser = function(obj) {
    debugAlert("Called BankParser!");

    var stars = obj.stars;
    console.log("BankParser: " + stars + " stars");

    window.localStorage.removeItem('bank');
    window.localStorage.setItem('bank',JSON.stringify(stars));
};
