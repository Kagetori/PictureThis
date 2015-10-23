//definition of the User class
var User = function(username, password, id, friends, auth_token) {
    this.username = username;       //string
    this.password = password;       //string
    this.id = id;                   //int
    this.friends = friends;         //list of user
    this.auth_token = auth_token;   //string
};