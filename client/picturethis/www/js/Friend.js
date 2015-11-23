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
        if (typeof obj.exception === "undefined") {
            var friendUsername = obj.username;
            var friend_id = obj.user_id;
            //asks if they want to add the user
            function onConfirm(buttonIndex) {
                if(buttonIndex === 1) {
                    addFriend(friend_id);
                } else {
                    setSpinnerVisibility(false);
                }
            }
            showNotification("Would you like to add " + friendUsername + " as a friend?",onConfirm,
            friendUsername + " has been found!",['Yes','No']);

        } else {
            //shows exception message
            showAlert(obj.exception);
            setSpinnerVisibility(false);
        }
    };

    serverCaller(api, params, searchParser, null, null);

};

//parses friend list and updates friends field for user
var friendParser = function(obj) {
    if (typeof obj.exception === "undefined") {
        setFriends(obj.friends);
        showAlert("Friend added!");
        document.getElementById("friend_search").value = "";
        setSpinnerVisibility(false);
    } else {
        //shows exception message
        showAlert(obj.exception);
        setSpinnerVisibility(false);
    }
};

//adds a friend
function addFriend(friend_id) {
    var user = getUser();
    var user_id = user.id;
    var api = 'friend/add_friend';
    var params = new Array();
    params['user_id'] = user_id;
    params['friend_id'] = friend_id;

    serverCaller(api, params, friendParser, null, null);
};

//blocks a friend
function blockFriend(friend_id) {
    var user = getUser();
    var user_id = user.id;
    var api = 'friend/block_friend';
    var params = new Array();
    params['user_id'] = user_id;
    params['friend_id'] = friend_id;

    serverCaller(api, params, friendParser, null, null);
};

//removes a friend
function removeFriend(friend_id) {
    var user = getUser();
    var user_id = user.id;
    var api = 'friend/remove_friend';
    var params = new Array();
    params['user_id'] = user_id;
    params['friend_id'] = friend_id;

    serverCaller(api, params, friendParser, null, null);
};

