var ScoreBank = function(score) {
    this.score = score;
};

var getScoreInfo = function() {
    return JSON.parse(window.localStorage.getItem('score_bank'));
};

var getScore = function() {
    console.log(getScoreInfo().points);
    return getScoreInfo().points;
};

var setScoreInfo = function(score_account) {
    window.localStorage.removeItem('score_bank');
    window.localStorage.setItem('score_bank',JSON.stringify(score_account));
};
