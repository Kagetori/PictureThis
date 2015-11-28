//This is the Friend class

function findFriend(username) {
    var user = getUser();
    var user_id = user.id;
    console.log("friend username: " + username);
    console.log("user id: " + user_id);
    var api = 'search/find_user';
    var params = new Array();
    params['user_id'] = user_id;
    params['username'] = username;

    var searchParser = function(obj) {
        var friendUsername = obj.username;
        var friend_id = obj.user_id;
        //asks if they want to add the user
        var onConfirm = function(buttonIndex) {
            if (buttonIndex === 1) {
                addFriend(friend_id);
            } else {
                setSpinnerVisibility(false);
            }
        };
        showNotification("Would you like to add " + friendUsername + " as a friend?", onConfirm,
        friendUsername + " has been found!",['Yes','No']);
    };

    serverCaller(api, params, searchParser, null, null);
};

//adds a friend
function addFriend(friend_id) {
    friendService(friend_id,'add_friend');
    showAlert("Friend added!");

    document.getElementById("friend_search").value = "";
};

//blocks a friend
function blockFriend(friend_id) {
    friendService(friend_id,'block_friend');
    showAlert("Friend blocked!");
};

//removes a friend
function removeFriend(friend_id) {
    friendService(friend_id,'remove_friend');
    showAlert("Friend removed!");
};

//general method for doing stuff to friend. Takes friend id and an action (ex. 'add_friend')
function friendService(friend_id, action) {
    var user = getUser();
    var user_id = user.id;
    var api = 'friend/' + action;
    var params = new Array();
    params['user_id'] = user_id;
    params['friend_id'] = friend_id;

    var updateRemoveTable = function() {
        if(action != 'add_friend') {
            serverCaller("poll/update", params, null, function() {
                populateRemoveTable();
            }, null);
        }
    }

    serverCaller(api, params, friendParser, updateRemoveTable, null);


};

//parses friend list and updates friends field for user
// TODO?
var friendParser = function(obj) {
    setSpinnerVisibility(false);
};
