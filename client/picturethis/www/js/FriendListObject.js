//definition of a friend list object
var FriendListObject = function(friend_username, friend_id, active_game, is_turn, is_photographer) {
    this.friend_username = friend_username;
    this.friend_id = friend_id;
    this.active_game = active_game;
    this.is_turn = is_turn;
    this.is_photographer = is_photographer;
};

var getFriendListObjects = function() {
    return JSON.parse(window.localStorage.getItem('friends'));
}

var setFriendListObjects = function(friends) {
    console.log("Updating friends.");
    window.localStorage.removeItem('friends');
    window.localStorage.setItem('friends', JSON.stringify(friends));
}
