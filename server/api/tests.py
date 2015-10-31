from django.test import TestCase

from models import User, Game, WordPrompt, Turn

from interface.exception import RemoteException
from interface.success import SuccessPacket
from interface.packets import GamePacket

import config, login, friend, search, game

# Create your tests here.

class LoginTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up
        return

    def testCreateUser(self):
        # Make a few users to test making

        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            user_view = login.create_user(username=username, password=password)

            user = User.objects.get(name=username)

            self.assertEqual(user_view.username, user.name)
            self.assertEqual(user_view.user_id, user.obfuscated_id)

        # Test duplicate create user failing
        self.assertRaises(RemoteException, login.create_user, username='user1', password='pw1')

    def testLogin(self):
        # Make a few users first
        usernames = []
        passwords = []

        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            usernames.append(username)
            passwords.append(password)

            login.create_user(username=username, password=password)

        # Try loggin them in
        for i in range(5):
            username = usernames[i]
            password = passwords[i]

            # Try logging in with incorrect or empty password
            self.assertRaises(RemoteException, login.login, username=username, password='asdf')
            self.assertRaises(RemoteException, login.login, username=username, password=None)

            user_view = login.login(username=username, password=password)

            user = User.objects.get(name=username)

            self.assertEqual(user_view.username, user.name)
            self.assertEqual(user_view.user_id, user.obfuscated_id)


class FriendTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            login.create_user(username=username, password=password)

    def testFriendApi(self):
        user0 = User.objects.get(name='user0')
        user0_id = user0.obfuscated_id

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.add_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

        user0_friends = friend.get_user_friends(user_id=user0_id)

        self.assertEqual(len(user0_friends.friends), 4)

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.remove_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_REMOVED)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_REMOVED)


class SearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(6):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            login.create_user(username=username, password=password)
        return

    def testFindUser(self):
        my_user = User.objects.get(name='user5')
        user_id = my_user.obfuscated_id

        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            
            user = User.objects.get(name=username)
            user_view = search.find_user(user_id=user_id, username=username)

            self.assertEqual(user_view.username, user.name)
            self.assertEqual(user_view.user_id, user.obfuscated_id)

        self.assertRaises(RemoteException, search.find_user, username='nonexistent')

class GameTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            login.create_user(username=username, password=password)

        WordPrompt.objects.create(word='apple')
        WordPrompt.objects.create(word='banana')
        WordPrompt.objects.create(word='orange')
        WordPrompt.objects.create(word='avocado')
        WordPrompt.objects.create(word='grapes')
        WordPrompt.objects.create(word='watermelon')

    def testStartNewGame(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        game_remote = game.start_new_game(user_id=user1_id, friend_id=user2_id)

        try:
            game_model = Game.objects.get(user_id1=user1_id, user_id2=user2_id)
        except Game.DoesNotExist:
            self.fail("Game not found")

        self.assertTrue(game_remote.active)
        self.assertTrue(game_model.active)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(game_model.curr_round, 1)

        self.assertEqual(game_remote.is_photographer, 1)
        self.assertEqual(game_remote.is_turn, 1)

        self.assertRaises(RemoteException, game.start_new_game, user_id=user1_id, friend_id=user1_id)
        self.assertRaises(RemoteException, game.start_new_game, user_id=user1_id, friend_id=user2_id)
        self.assertRaises(RemoteException, game.start_new_game, user_id=user2_id, friend_id=user1_id)

    def testSendPicture(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        game_remote = game.start_new_game(user_id=user1_id, friend_id=user2_id)

        self.assertTrue(game_remote.active)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(game_remote.is_photographer, 1)
        self.assertEqual(game_remote.is_turn, 1)

        game_remote_friend = game.get_user_games(user_id=user2_id).games[0]

        self.assertEqual(game_remote_friend.curr_round, 1)
        self.assertEqual(game_remote_friend.is_photographer, 0)
        self.assertEqual(game_remote_friend.is_turn, 0)

        game_remote = game.send_picture(user_id=user1_id, game_id=game_remote.game_id)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(game_remote.is_photographer, 1)
        self.assertEqual(game_remote.is_turn, 0)

        game_remote_friend = game.get_user_games(user_id=user2_id).games[0]

        self.assertEqual(game_remote_friend.curr_round, 1)
        self.assertEqual(game_remote_friend.is_photographer, 0)
        self.assertEqual(game_remote_friend.is_turn, 1)


    def testEndGame(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        game.start_new_game(user_id=user1_id, friend_id=user2_id)
        game_id = Game.objects.get(user_id1=user1_id, user_id2=user2_id).id

        game_remote = game.end_game(user_id=user1_id, game_id=game_id)
        self.assertFalse(game_remote.active)
        self.assertFalse(Game.objects.get(id=game_id).active)

    def testValidateGuess(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id

        game.start_new_game(user_id=user1_id, friend_id=user2_id)

        game_id = Game.objects.get(user_id1=user1_id, user_id2=user2_id).id

        game_remote_1 = game.send_picture(user_id=user1_id, game_id=game_id)

        self.assertRaises(RemoteException, game.validate_guess, user_id=user2_id, game_id=game_id, guess='pear')
        self.assertRaises(RemoteException, game.validate_guess, user_id=user1_id, game_id=game_id, guess=game_remote_1.curr_word)

        game_remote_2 = game.validate_guess(user_id=user2_id, game_id=game_id, guess=game_remote_1.curr_word)

        self.assertTrue(game_remote_2.active)
        self.assertEqual(game_remote_2.curr_round, 2)
        self.assertNotEqual(game_remote_1.curr_word, game_remote_2.curr_word)

    def testGetUserGames(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        user3_id = User.objects.get(name='user3').obfuscated_id
        user4_id = User.objects.get(name='user4').obfuscated_id
        user0_id = User.objects.get(name='user0').obfuscated_id

        game1 = game.start_new_game(user_id=user1_id, friend_id=user2_id)
        game2 = game.start_new_game(user_id=user1_id, friend_id=user3_id)
        game3 = game.start_new_game(user_id=user4_id, friend_id=user1_id)

        user1_games = game.get_user_games(user_id=user1_id)
        user0_games = game.get_user_games(user_id=user0_id)

        self.assertEqual(len(user1_games.games), 3)
        self.assertEqual(len(user0_games.games), 0)

        game.end_game(user_id=user1_id, game_id=game1.game_id)
        game.end_game(user_id=user1_id, game_id=game2.game_id)
        game.end_game(user_id=user1_id, game_id=game3.game_id)

        user1_games = game.get_user_games(user_id=user1_id)
        self.assertEqual(len(user1_games.games), 0)
