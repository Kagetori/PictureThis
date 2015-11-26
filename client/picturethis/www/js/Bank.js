var Bank = function(stars) {
    this.stars = stars;
};

var getBankInfo = function() {
    return JSON.parse(window.localStorage.getItem('bank'));
};

var getStars = function() {
    return getBankInfo().stars;
};

var setBankInfo = function(bank) {
    console.log("Updating bank.");
    window.localStorage.removeItem('bank');
    window.localStorage.setItem('bank',JSON.stringify(bank));
};
