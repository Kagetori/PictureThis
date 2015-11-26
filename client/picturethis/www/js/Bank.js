var Bank = function(stars) {
    this.stars = stars;
};

var getBankInfo = function() {
    var retrievedBank = window.localStorage.getItem('bank');
    return retrievedBank;
};