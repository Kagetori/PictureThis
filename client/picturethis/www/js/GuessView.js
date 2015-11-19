var GuessView = function (service) {
    this.initialize = function () {
        // Define a div wrapper for the view (used to attach events)
        console.log("Initialized GuessView");
        this.$el = $('<div/>');
        this.render();

    };

    this.render = function() {
        this.$el.html(this.template());
        return this;
    };

    this.sendGuess = function() {
        var currentGame = getActiveGame();
        var currentWord = currentGame.curr_word;
        console.log(currentWord);
        var guess = parseGuess();
        var cleanGuess = guess.trim().toLowerCase();
        if (currentWord != cleanGuess) {
            showAlert("Your guess is incorrect. Try again.");
        } else {
            showAlert("Your guess is correct! Continue!");

            var user = getUser();
            var user_id = user.id;
            console.log(user_id);
            var game_id = currentGame.game_id;
            console.log(game_id);
            console.log(cleanGuess);
            var api = 'game/validate_guess';
            var params = new Array();
            params['user_id'] = user_id;
            params['game_id'] = game_id;
            params['guess'] = cleanGuess;

            var picView = function(){
                var guessView = new GuessView();
                guessView.toPictureView();
            };

            serverCaller(api, params, GameParser, picView, null);
        }
    }

    this.toPictureView = function() {
        var currentGame = getActiveGame();
        if (currentGame.active) {
            window.location.reload();
        } else {
            var game = getActiveGame();
            var friend_id = game.friend_id;

            function onConfirm(buttonIndex) {
                if(buttonIndex === 1) {
                    startNewGame(friend_id);
                } else {
                    window.location="friends.html";
                }
            };

            showNotification('Would you like to start a new game?',onConfirm,'Game Finished!',['Yes','No']);
        }
    }

    this.getHint = function() {
        var currentGame = getActiveGame();
        var currentWord = currentGame.curr_word;
        var params = new Array();
        var api = 'word_prompt/get_word_prompt';
        params['word'] = currentWord;

        serverCaller(api, params, HintParser, null, null);
    }

    this.initialize();
}

function addLetters() {
    console.log("got to AddLetters");
    var totalLetters = 12;
    var currentGame = getActiveGame();
    var currentWord = currentGame.curr_word;
    var extraLetters = randomLetters(totalLetters-currentWord.length);
    var wordScramble = shuffleLetters(currentWord + extraLetters);

    for(i = 0; i < totalLetters; i++) {
        var letter = wordScramble.charAt(i);
        document.getElementById(i).innerHTML = letter.toUpperCase();
    }


}

//returns guess as a string
function parseGuess() {
    console.log("parsing guess");
    var guess = "";
    var i = 1;
    do{
        if(document.getElementById("G" + i).innerHTML != "_") {
            guess = guess + document.getElementById("G" + i).innerHTML;
            i++;
        } else {
            i++;
        }
    }
    while(document.getElementById("G" + i) != null)

    console.log(guess);
    return guess;
}

function getGuessImage() {
    var user = getUser();
    var user_id = user.id;
    var currentGame = getActiveGame();
    var game_id = currentGame.game_id;
    var params = new Array();
    params['user_id'] = user_id;
    params['game_id'] = game_id;

    serverCaller('game/get_picture', params, function(result) {
        document.getElementById('guess_img').src = result;
    }, null, null);
}

function populateGuessBlocks(word) {
    console.log("populating guess blocks for " + word);
    var blocksList = document.getElementById("guess_blocks")

    if (word.length != 0) {
        var tableul = document.createElement('ul');
        tableul.className = "blocks_list";

        for (i=0; i<word.length; i++) {
            var block = document.createElement("li");
            block.className = "guess_box";
            block.id = "G" + String(i+1);
            tableul.appendChild(block);
        }
        blocksList.appendChild(tableul);
    }
    console.log($("#guess_blocks").html());
}

function randomLetters(numLetters)
{
    var letters = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (var i=0; i<numLetters; i++)
        letters += possible.charAt(Math.floor(Math.random() * possible.length));

    return letters;
}

function shuffleLetters(text)
{
    var textArray = text.split("");
    for (var i=text.length-1; i>0; i--) {
        var j = Math.floor(Math.random() * (i+1));
        var tmp = textArray[i];
        textArray[i] = textArray[j];
        textArray[j] = tmp;
    }
    return textArray.join("");
}

//score starts at 200 when user enters the guessView. Have to save score either in local storage or in server
var score = 200;

var counter = setInterval(countdown, 500);

function countdown()
{
    score = score - 1;
    if (score < 50)
    {
        clearInterval(counter);
        return;
    }
    document.getElementById("countdown").innerHTML="Score: "+score;
}