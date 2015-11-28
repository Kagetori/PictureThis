// beforeEach(function () {
//   var store = {};

//   spyOn(localStorage, 'getItem').andCallFake(function (key) {
//     return store[key];
//   });
//   spyOn(localStorage, 'setItem').andCallFake(function (key, value) {
//     return store[key] = value + '';
//   });
//   spyOn(localStorage, 'clear').andCallFake(function () {
//       store = {};
//   });
// });

describe ('parsers calling localStorage', function() {
  beforeEach( function() {
    spyOn(localStorage, 'setItem');
    spyOn(localStorage, 'removeItem');
  });

  describe('parsing hints', function() {
    beforeEach( function() {
      HintParser({"word_prompt": "dog", "wordClass": "noun", "word_category": "animal"});
    });

    it ("removeItem should have been called", function () {
      expect(localStorage.removeItem).toHaveBeenCalled();
    });

    it ("setItem should have been called", function () {
      expect(localStorage.setItem).toHaveBeenCalled();
    });

  });

  describe('parsing game', function() {
    beforeEach(function() {
      GameParser({"game_id": 123, "user_id": 456, "friend_id": 789, "active": true, "curr_round": 1, "words_seen": ["dog"] });
    });
    it ("removeItem should have been called", function () {
      expect(localStorage.removeItem).toHaveBeenCalled();
    });

    it ("setItem should have been called", function () {
      expect(localStorage.setItem).toHaveBeenCalled();
    });
  });

  describe('parsing user', function() {
    beforeEach(function() {
      UserParser({"username": "me", "user_id": 456, "friend_id": [], "auth_token": "XYZRST"});
    });
    it ("removeItem should have been called", function () {
      expect(localStorage.removeItem).toHaveBeenCalled();
    });

    it ("setItem should have been called", function () {
      expect(localStorage.setItem).toHaveBeenCalled();
    });
  });
});

