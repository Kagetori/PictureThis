// definition of the Game class
var Game = function(game_id, user_id, friend_id, active, my_turn, is_photographer, curr_round, words_seen) {
    this.game_id = game_id;
    this.user_id = user_id;
    this.friend_id = friend_id;
    this.active = active;
    this.my_turn = my_turn;
    this.is_photographer = is_photographer;
    this.curr_round = curr_round;
    this.words_seen = words_seen;
}

//checks if there's an ongoing game with the friend. Continues game if there is, else starts a new game.
function playGame(friendId){
	showAlert(friendId);
	//TODO: check for ongoing game (query server for most recent results?)
	//TODO: continue current game (go to appropriate screen)
	//TODO: else start a new game
};
