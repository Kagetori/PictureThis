from django.test import TestCase

from models import User, Game

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

# class GameTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # for i in range(3):
#         #     username = 'user' + str(i)
#         #     password = 'pw' + str(i)

#         #     login.create_user(username=username, password=password)
#         # return
#         return

#     def testStartNewGame(self):
#         game_remote = game.start_new_game(user_id='1', friend_id='2')

#         #game_model = Game.objects.get(id=1)

#         #self.assertEqual(game_remote.user_id, game_model.user_id1)
#         #self.assertEqual(game_remote.friend_id, game_model.user_id2)

#         self.assertTrue(game_remote.active)
#         #self.assertTrue(game_model.active)

#         self.assertEqual(game_remote.curr_round, 0)
#         #self.assertEqual(game_model.curr_round, 0)


