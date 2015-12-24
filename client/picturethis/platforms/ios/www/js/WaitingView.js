var WaitingView = function (score_stars) {
    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };

    this.render = function() {
        this.$el.html(this.template(score_stars));
        return this;
    };

    this.initialize();
}
