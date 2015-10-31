//definition of the User class
var User = function(username, password, id, friends, games, auth_token) {
    this.username = username;       //string
    this.password = password;       //string
    this.id = id;                   //int
    this.friends = friends;         //list of user
    this.games = games;             //list of games
    this.auth_token = auth_token;   //string
};

//gets the user from localstorage and returns an user object
var getUser = function(){
    var retrievedUser =  window.localStorage.getItem('userObject');
    var parsedUser = JSON.parse(retrievedUser);
    return parsedUser;
};

var setFriends = function(friends){
    var parsedUser = JSON.parse(window.localStorage.getItem('userObject'));
    parsedUser.friends = friends;
    //window.localStorage.removeItem('userObject');
    window.localStorage.setItem('userObject', JSON.stringify(parsedUser));
}
