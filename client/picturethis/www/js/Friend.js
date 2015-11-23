//This is the Friend class

function findFriend(username) {
    console.log("got to findFriend!");
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

//queries server with self id and friend id. Updates friends field for user(?)
function addFriend(friend_id) {
    console.log("got to addFriend!");
    var user = getUser();
    var user_id = user.id;
    var api = 'friend/add_friend';
    var params = new Array();
    params['user_id'] = user_id;
    params['friend_id'] = friend_id;

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

    serverCaller(api, params, friendParser, null, null);


};