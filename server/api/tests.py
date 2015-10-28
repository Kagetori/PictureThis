from django.test import TestCase

from models import User, Game, WordPrompt

from interface.exception import RemoteException

import login, search, game

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

        # Test duplicate logging in

class SearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            login.create_user(username=username, password=password)
        return

    def testFindUser(self):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            
            user = User.objects.get(name=username)
            user_view = search.find_user(username=username)

            self.assertEqual(user_view.username, user.name)
            self.assertEqual(user_view.user_id, user.obfuscated_id)
        try:
            search.find_user(username='nonexistent')
        except RemoteException:
            pass # TODO check error message too

class GameTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(3):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            login.create_user(username=username, password=password)
        # populate the word database with six words (=number of rounds)
        WordPrompt.objects.create(word='apple')
        WordPrompt.objects.create(word='banana')
        WordPrompt.objects.create(word='orange')
        WordPrompt.objects.create(word='avocado')
        WordPrompt.objects.create(word='grapes')
        WordPrompt.objects.create(word='watermelon')
        return

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

        self.assertEqual(game_remote.curr_round, 0)
        self.assertEqual(game_model.curr_round, 0)

        try:
            game.start_new_game(user_id=user1_id, friend_id=user1_id)
        except RemoteException:
            pass

    def testStartNewRound(self):
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id

        game.start_new_game(user_id=user1_id, friend_id=user2_id)

        game_model = Game.objects.get(user_id1=user1_id, user_id2=user2_id)
        game_id = game_model.id

        game_remote = game.start_new_round(user_id=user1_id, game_id=game_id)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(len(game_remote.words_seen), 0)
        self.assertEqual(game_remote.user_id, user1_id)
        self.assertEqual(game_remote.friend_id, user2_id)

        game_remote = game.start_new_round(user_id=user2_id, game_id=game_id)

        self.assertTrue(game_remote.curr_round, 2)
        self.assertEqual(len(game_remote.words_seen), 1)
        self.assertEqual(game_remote.user_id, user2_id)
        self.assertEqual(game_remote.friend_id, user1_id)



