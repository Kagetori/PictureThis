var ChangePasswordView = function (service) {
    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };
    
//  this.initialize();
    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    this.backToMain = function() {
        window.location.reload();
        window.location="friends.html";
    }

    this.updatePassword = function(user_id, old_password, new_password){
        console.log(user_id);
        console.log(old_password);
        console.log(new_password);
        var api = 'login/update_password';
        var params = new Array();
        params['username_id'] = user_id;
        params['old_password'] = old_password;
        params['new_password'] = new_password;
        var passwordUpdated = function(){
            showAlert('Your password has been changed successfully.', 'Password changed')
            backToMain();
        }
        serverCaller(api, params, UserParser, passwordUpdated, null);
    }

    this.initialize();
}