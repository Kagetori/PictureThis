var GamesParser = function(result) {
   showAlert("Called GamesParser!");
   var obj = JSON.parse(result);
   if (typeof obj.exception === "undefined") {
        // iterate over each object of array
   } else {
         showAlert(obj.exception);
         };
 };

 var GameParser = function(result) {
    showAlert("Called GameParser!");
    var obj = JSON.parse(result);
    if (typeof obj.exception === "undefined") {
         var game = new Game();
         game.game_id = obj.game_id;
         game.user_id = obj.user_id;
         game.friend_id = obj.friend_id;
         game.active = obj.active;
         game.curr_round = obj.curr_round;
         game.words_seen = obj.words_seen;

         if (typeof obj.curr_word != "undefined") {
            game.curr_word = obj.curr_word;
         };

          if (typeof obj.my_round != "undefined") {
             game.my_round = obj.my_round;
          };
    } else {
          showAlert(obj.exception);
          };
  };

