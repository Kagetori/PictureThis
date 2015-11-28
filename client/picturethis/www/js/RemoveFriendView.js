var RemoveFriendView = function (service) {

    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        this.$el = $('<div/>');
        this.render();
    };
    
//  this.initialize();
    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    var test = document.getElementById("test");
    console.log(test);

    this.initialize();
}

function populateRemoveTable() {
    var friends = getFriendListObjects();
    var friendListRemoveWrapper = document.getElementById("remove_friend_wrapper");
    if (friends.length != 0) {
        var tableul = document.createElement('ul');
        tableul.className = "table col-xs-12";

        var removeHeader = document.createElement("li");
        removeHeader.className = "remove_header";
        var removeHeaderText = document.createTextNode("Block/Remove Friends");
        removeHeader.appendChild(removeHeaderText);
        tableul.appendChild(removeHeader);

        for (i = 0; i < friends.length; i++) {
            var tableli = document.createElement("li");
            tableli.className = "friend_element";
            friendUserName = friends[i].friend_username;
            var tabletext = document.createTextNode(friendUserName);
            var friendId = friends[i].friend_id;
            console.log(friendUserName);
            console.log(friendId);

            var removebutton = document.createElement("button");
            var removeSpan = document.createElement('span');
            removeSpan.className = "glyphicon glyphicon-remove";
            removebutton.className = "btn remove_button";
            removebutton.setAttribute("onClick", "removeF("+friendId.toString()+");");

            var blockbutton = document.createElement("button");
            var blockSpan = document.createElement('span');
            blockSpan.className = "glyphicon glyphicon-minus-sign";
            blockbutton.className = "btn block_button";
            blockbutton.setAttribute("onClick", "blockF("+friendId.toString()+");");

            removebutton.appendChild(removeSpan);
            blockbutton.appendChild(blockSpan);

            tableli.appendChild(tabletext);
            tableli.appendChild(removebutton);
            tableli.appendChild(blockbutton);
            tableul.appendChild(tableli);
        }
    }
    if (friendListRemoveWrapper.hasChildNodes()) {
        friendListRemoveWrapper.removeChild(friendListRemoveWrapper.childNodes[0]);
    }
    friendListRemoveWrapper.appendChild(tableul);
}

//// returns parsed friendListObjects
//var getFriendListObjectsToRemove = function(friendListRemoveWrapper, callback) {
//    var user = getUser();
//    var api = 'poll/update';
//    var params = new Array();
//    params['user_id'] = user.id;
//    var friendList = [];
//
//    var friendListObjectParser = function(obj) {
//
//        //var friendList = [];
//        var objects = obj.polls;
//
//        for (var i = 0; i < objects.length; i++) {
//            var friendListObject = new FriendListObject();
//            var object = objects[i];
//
//            friendListObject.friend_username = object.friend_username;
//            friendListObject.friend_id = object.friend_id;
//            friendListObject.active_game = object.active_game;
//            friendListObject.is_turn = object.is_turn;
//            friendListObject.is_photographer = object.is_photographer;
//
//            friendList.push(friendListObject);
//        }
//
//        //console.log(JSON.stringify(friendList));
//
//        if (friendList.length != 0) {
//            var tableul = document.createElement('ul');
//            tableul.className = "friends_list";
//
//            for (i = 0; i < friendList.length; i++) {
//                var tableli = document.createElement("li");
//                tableli.className = "friend_element";
//                friendUserName = friendList[i].friend_username;
//                var tabletext = document.createTextNode(friendUserName);
//                var friendId = friendList[i].friend_id;
//
//                var removebutton = document.createElement("button");
//                var removetext = document.createTextNode("Remove");
//                removebutton.setAttribute("onClick", "removeF("+friendId.toString()+");");
//
//                var blockbutton = document.createElement("button");
//                var blocktext = document.createTextNode("Block");
//                blockbutton.setAttribute("onClick", "blockF("+friendId.toString()+");");
//
//                removebutton.appendChild(removetext);
//                blockbutton.appendChild(blocktext);
//
//                tableli.appendChild(tabletext);
//                tableli.appendChild(removebutton);
//                tableli.appendChild(blockbutton);
//                tableul.appendChild(tableli);
//            }
//        }
//
//        if (friendListRemoveWrapper.hasChildNodes()) {
//            friendListRemoveWrapper.removeChild(friendListRemoveWrapper.childNodes[0]);
//        }
//
//        friendListRemoveWrapper.appendChild(tableul);
//
//    };
//
//    serverCaller(api, params, friendListObjectParser, callback, null);
//}
