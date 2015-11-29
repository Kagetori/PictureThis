var ScoreBank = function(score) {
    this.score = score;
};

var getScoreInfo = function() {
    return JSON.parse(window.localStorage.getItem('score_bank'));
};

var getScore = function() {
    return getScoreInfo().points;
};

var setScoreInfo = function(score_account) {
    console.log("Updating score.");
    window.localStorage.removeItem('score_bank');
    window.localStorage.setItem('score_bank',JSON.stringify(score_account));
};
