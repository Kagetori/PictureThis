//definition of the User class
var User = function(username, password, id, friends, games, auth_token, stars, score) {
    this.username = username;       //string
    this.password = password;       //string
    this.id = id;                   //int
    this.friends = friends;         //list of user
    this.games = games;             //list of games
    this.auth_token = auth_token;   //string
};

//gets the user from localStorage and returns an user object
var getUser = function(){
    var retrievedUser =  window.localStorage.getItem('userObject');
    var parsedUser = JSON.parse(retrievedUser);
    return parsedUser;
};

var setFriends = function(friends){
    var parsedUser = JSON.parse(window.localStorage.getItem('userObject'));
    parsedUser.friends = friends;
    window.localStorage.setItem('userObject', JSON.stringify(parsedUser));
}

var logout = function() {
//      var nullUser = new User("","","","","","");
//      window.localStorage.setItem('userObject', nullUser);
    setSpinnerVisibility(true);
    window.localStorage.clear();
    window.location="login.html";
}

var setLoginToken = function(loginToken) {
    window.localStorage.removeItem('login_token');
    window.localStorage.setItem('login_token', loginToken);
}

var getLoginToken = function() {
    return window.localStorage.getItem('login_token');
}
