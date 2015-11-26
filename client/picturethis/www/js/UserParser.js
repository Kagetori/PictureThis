//Takes return of server call and either parses&stores user in localStorage or shows an alert(exception)
var UserParser = function(obj) {
   debugAlert("Called UserParser!");

    var myUser = new User();
    myUser.username = obj.username;
    myUser.id = obj.user_id;
    myUser.friends = obj.friends;
    myUser.auth_token = obj.auth_token;

    window.localStorage.clear();
    window.localStorage.setItem('userObject', JSON.stringify(myUser));
}
