//Takes return of server call and either parses&stores user in localStorage or shows an alert(exception)
var UserParser = function(result) {
   showAlert("Called UserParser!");
   var obj = JSON.parse(result);
   if (typeof obj.exception === "undefined") {
        showAlert("there's a user!");

        var myUser = new User();
        myUser.username = obj.username;
        myUser.id = obj.user_id;
        myUser.friends = obj.friends;
        myUser.auth_token = obj.auth_token;

        window.localStorage.clear();
        window.localStorage.setItem('userObject', JSON.stringify(myUser));

        if (typeof obj.games != "undefined") {
            var gamesParser = new GamesParser(JSON.stringify(obj.games));
        };

        } else {
        //shows exception message
        showAlert(obj.exception);
        };
}