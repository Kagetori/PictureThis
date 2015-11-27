// This file defines hooks that is called by ServerCaller

function hooks(obj) {

    // Hook for Login Token
    if (obj.hasOwnProperty('login_token')) {
        var login_token = obj.login_token;
        setLoginToken(login_token);
    }

    // Hook for Bank
    if (obj.hasOwnProperty('bank_account')) {
        var bank_account = obj.bank_account;
        setBankInfo(bank_account);
    }

    // Hook for Score
    if (obj.hasOwnProperty('score')){
        var score_account = obj.score;
        setScoreInfo(score_account);
    }

    // Hook for Friends
    if (obj.hasOwnProperty('friends')) {
        var friendList = [];

        for (var i = 0; i < obj.friends.length; i++) {
            var object = obj.friends[i];

            var friend_username = object.username;
            var friend_id = object.user_id;
            var active_game = object.has_active_game;
            var is_turn = object.is_turn;
            var is_photographer = object.is_photographer;

            var friendListObject = new FriendListObject(friend_username, friend_id, active_game, is_turn, is_photographer);

            friendList.push(friendListObject);
        }

        setFriendListObjects(friendList);
    }

}
