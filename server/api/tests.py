from django.test import TestCase

from models import User, Game, WordPrompt, Turn, Bank, Score

from interface.exception import RemoteException
from interface.packets import GamePacket

import config, login, friend, search, game, poll, bank, score, word_prompt

import base64, time

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

            # Try logging in with login token

            user_view_2 = login.token_login(user_id=user_view.user_id, login_token=user_view.login_token)

            self.assertEqual(user_view_2.username, user.name)
            self.assertEqual(user_view_2.user_id, user.obfuscated_id)

            # Auth token should be different but login token should be the same
            self.assertEqual(user_view.login_token, user_view_2.login_token)
            self.assertNotEqual(user_view.auth_token, user_view_2.auth_token)

    def testChangePassword(self):
        # Make a few users first
        usernames = []
        passwords = []

        for i in range(3):
            username = 'user' + str(i)
            password = 'pw' + str(i)

            usernames.append(username)
            passwords.append(password)

            login.create_user(username=username, password=password)

        # Try loggin them in
        for i in range(3):
            username = usernames[i]
            password = passwords[i]
            new_password = 'pwx' + str(i)

            # Login first
            user_view_1 = login.login(username=username, password=password)

            # Change their password
            self.assertRaises(RemoteException, login.update_password, user_id=user_view_1.user_id, old_password='asdf', new_password=new_password)
            self.assertRaises(RemoteException, login.update_password, user_id=user_view_1.user_id, old_password=None, new_password=new_password)

            login.update_password(user_id=user_view_1.user_id, old_password=password, new_password=new_password)

            # Login with new pw (old pw doesnt work)
            self.assertRaises(RemoteException, login.login, username=username, password=password)
            user_view_2 = login.login(username=username, password=new_password)

            # Login token and auth token is different
            self.assertNotEqual(user_view_1.login_token, user_view_2.login_token)
            self.assertNotEqual(user_view_1.auth_token, user_view_2.auth_token)

class BankTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'user1'
        password = 'pw1'
        login.create_user(username=username, password=password)

    def testGetUserBank(self):
        user = User.objects.get(name='user1')
        bank_account = bank.get_user_bank(user_id=user.obfuscated_id)
        bank_object = Bank.objects.get(user_id=user.obfuscated_id)

        self.assertEqual(bank_object.stars, bank_account.stars)

    def testAddingAndRemovingStars(self):
        user = User.objects.get(name='user1')
        old_bank_account = bank.get_user_bank(user_id=user.obfuscated_id)

        # Add some stars
        bank_account = bank.add_to_bank(user_id=user.obfuscated_id, stars=config.DEFAULT_STARS)
        self.assertEqual(old_bank_account.stars + config.DEFAULT_STARS, bank_account.stars)

        # Remove some stars
        bank_account = bank.add_to_bank(user_id=user.obfuscated_id, stars=(-1 * config.DEFAULT_STARS))
        self.assertEqual(old_bank_account.stars, bank_account.stars)

        bank_account = bank.add_to_bank(user_id=user.obfuscated_id, stars=(-1 * config.DEFAULT_STARS))
        self.assertEqual(0, bank_account.stars)

        # Try removing more stars
        self.assertRaises(RemoteException, bank.add_to_bank, user_id=user.obfuscated_id, stars=-1)

        bank_account = bank.add_to_bank(user_id=user.obfuscated_id, stars=0)
        self.assertEqual(0, bank_account.stars)

        bank_account = bank.add_to_bank(user_id=user.obfuscated_id, stars=1)
        self.assertEqual(1, bank_account.stars)

        bank_account = bank.decrement_bank(user_id=user.obfuscated_id)
        self.assertEqual(0, bank_account.stars)

        self.assertRaises(RemoteException, bank.decrement_bank, user_id=user.obfuscated_id)

        # check still at 0
        bank_account = bank.get_user_bank(user_id=user.obfuscated_id)
        self.assertEqual(0, bank_account.stars)

class ScoreTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'user1'
        password = 'pw1'
        login.create_user(username=username, password=password)

    def testGetUserScore(self):
        user = User.objects.get(name='user1')
        score_account = score.get_user_score(user_id=user.obfuscated_id)
        score_object = Score.objects.get(user_id=user.obfuscated_id)

        self.assertEqual(score_object.points, score_account.points)

    def testAddingPoints(self):
        user = User.objects.get(name='user1')
        old_score_account = score.get_user_score(user_id=user.obfuscated_id)

        # Add some points
        score_account = score.add_to_score(user_id=user.obfuscated_id, points=1)
        self.assertEqual(old_score_account.points + 1, score_account.points)

        score_account = score.add_to_score(user_id=user.obfuscated_id, points=4)
        self.assertEqual(old_score_account.points + 5, score_account.points)

        score_account = score.add_to_score(user_id=user.obfuscated_id, points=995)
        self.assertEqual(old_score_account.points + 1000, score_account.points)

        score_account = score.add_to_score(user_id=user.obfuscated_id, points=0)
        self.assertEqual(old_score_account.points + 1000, score_account.points)

        # Try removing points
        self.assertRaises(RemoteException, score.add_to_score, user_id=user.obfuscated_id, points=-1)

        # Check that get_user_score still works
        score_account = score.get_user_score(user_id=user.obfuscated_id)
        self.assertEqual(old_score_account.points + 1000, score_account.points)

class FriendTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            login.create_user(username=username, password=password)

    def testAddFriends(self):
        user0 = User.objects.get(name='user0')
        user0_id = user0.obfuscated_id

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.add_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_FRIEND)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_FRIEND)

        user0_friends = friend.get_user_friends(user_id=user0_id)

        self.assertEqual(len(user0_friends.friends), 4)

    def testRemoveFriends(self):
        user0 = User.objects.get(name='user0')
        user0_id = user0.obfuscated_id

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.add_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_FRIEND)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_FRIEND)

        user0_friends = friend.get_user_friends(user_id=user0_id)

        self.assertEqual(len(user0_friends.friends), 4)

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.remove_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_REMOVED)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_REMOVED)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_REMOVED)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_REMOVED)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_REMOVED)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_REMOVED)

            # They can add each other as friends again
            friend.add_friend(user_id=user_id, friend_id=user0_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_FRIEND)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_FRIEND)

    def testBlockFriends(self):
        user0 = User.objects.get(name='user0')
        user0_id = user0.obfuscated_id

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.add_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_FRIEND)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_FRIEND)

        user0_friends = friend.get_user_friends(user_id=user0_id)

        self.assertEqual(len(user0_friends.friends), 4)

        for i in range(1, 5):
            username = 'user' + str(i)
            user_id = User.objects.get(name=username).obfuscated_id

            friend.block_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_BLOCKED)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_REMOVED)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_BLOCKED)
            # the other user should not know that the first user exists
            self.assertRaises(RemoteException, friend.get_friend_details, user_id=user_id, friend_id=user0_id)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_BLOCKED)
            # second user can't search for the first user
            self.assertRaises(RemoteException, search.find_user, user_id=user_id, username='user0')

            # second user can't add first user as a friend
            self.assertRaises(RemoteException, friend.add_friend, user_id=user_id, friend_id=user0_id)

            # but if first user adds second user as a friend, they're friends again
            friend.add_friend(user_id=user0_id, friend_id=user_id)

            self.assertEqual(friend.get_friend_status(user_id1=user0_id, user_id2=user_id), config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_status(user_id1=user_id, user_id2=user0_id), config.FRIEND_STATUS_FRIEND)

            self.assertEqual(friend.get_friend_details(user_id=user0_id, friend_id=user_id).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(friend.get_friend_details(user_id=user_id, friend_id=user0_id).relation, config.FRIEND_STATUS_FRIEND)

            self.assertEqual(search.find_user(user_id=user0_id, username=username).relation, config.FRIEND_STATUS_FRIEND)
            self.assertEqual(search.find_user(user_id=user_id, username='user0').relation, config.FRIEND_STATUS_FRIEND)

    def testGetAllFriends(self):
        user0_id = User.objects.get(name='user0').obfuscated_id
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        user3_id = User.objects.get(name='user3').obfuscated_id
        user4_id = User.objects.get(name='user4').obfuscated_id

        friend.add_friend(user_id=user0_id, friend_id=user1_id)
        friend.add_friend(user_id=user2_id, friend_id=user0_id)
        friend.add_friend(user_id=user0_id, friend_id=user3_id)
        friend.add_friend(user_id=user4_id, friend_id=user0_id)

        self.assertEqual(len(friend.get_user_friends(user0_id).friends), 4)

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

        self.assertRaises(RemoteException, search.find_user, user_id=user_id, username='nonexistent')

class WordPromptTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'user1'
        password = 'pw1'
        login.create_user(username=username, password=password)

        WordPrompt.objects.create(word='apple', word_class='noun', category='food')

    def testGetHint(self):
        user_view = login.login(username='user1', password='pw1')

        word_prompt_view = word_prompt.request_hint(user_id=user_view.user_id, word='apple')

        self.assertEqual('apple', word_prompt_view.word)
        self.assertEqual('noun', word_prompt_view.word_class)
        self.assertEqual('food', word_prompt_view.word_category)
        self.assertEqual(user_view.bank_account.stars - 1, word_prompt_view.bank_account.stars)

        # Can't get word prompt for non-existant word
        self.assertRaises(RemoteException, word_prompt.request_hint, user_id=user_view.user_id, word='banana')

        # No more stars
        bank.add_to_bank(user_id=user_view.user_id, stars=(word_prompt_view.bank_account.stars * -1))

        # Can't get word prompt since no more stars
        self.assertRaises(RemoteException, word_prompt.request_hint, user_id=user_view.user_id, word='apple')

class GameTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            login.create_user(username=username, password=password)

        WordPrompt.objects.create(word='apple', word_class='noun', category='food')
        WordPrompt.objects.create(word='banana', word_class='noun', category='food')
        WordPrompt.objects.create(word='orange', word_class='noun', category='food')
        WordPrompt.objects.create(word='avocado', word_class='noun', category='food')
        WordPrompt.objects.create(word='grapes', word_class='noun', category='food')
        WordPrompt.objects.create(word='watermelon', word_class='noun', category='food')

    def setUp(self):
        # Add each other as friends
        for i in range(4):
            user_id1 = login.login(username='user'+str(i), password='pw'+str(i)).user_id
            for j in range(i+1, 5):
                user_id2 = login.login(username='user'+str(j), password='pw'+str(j)).user_id
                friend.add_friend(user_id=user_id1, friend_id=user_id2)

        self.file_path = '/var/www/picturethis/media_test/'

    def tearDown(self):
        # Remove friends
        for i in range(4):
            user_id1 = login.login(username='user'+str(i), password='pw'+str(i)).user_id
            for j in range(i+1, 5):
                user_id2 = login.login(username='user'+str(j), password='pw'+str(j)).user_id
                friend.remove_friend(user_id=user_id1, friend_id=user_id2)

        for g in Game.objects.all():
            g.active = False
            g.save()

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

        # Assert game is active
        self.assertTrue(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

        # Remove friend
        friend.remove_friend(user_id=user1_id, friend_id=user2_id)

        # No active game between users now
        self.assertFalse(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

        # Add friend back
        friend.add_friend(user_id=user1_id, friend_id=user2_id)

        # Game is not reactivated
        self.assertFalse(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

        # Start a new game
        game_remote = game.start_new_game(user_id=user1_id, friend_id=user2_id)

        self.assertTrue(game_remote.active)
        self.assertTrue(game_model.active)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(game_model.curr_round, 1)

        self.assertEqual(game_remote.is_photographer, 1)
        self.assertEqual(game_remote.is_turn, 1)

        # Assert game is active
        self.assertTrue(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

        # Block friend
        friend.block_friend(user_id=user1_id, friend_id=user2_id)

        # No active game between users now
        self.assertFalse(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

        # Add friend back
        friend.add_friend(user_id=user1_id, friend_id=user2_id)

        # Game is not reactivated
        self.assertFalse(game._is_active_game(user_id1=user1_id, user_id2=user2_id))

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

        photo = config.BLANK_PICTURE

        self.assertRaises(RemoteException, game.send_picture, user_id=user2_id, game_id=game_remote.game_id, photo=photo, path=self.file_path)
        self.assertRaises(RemoteException, game.send_picture, user_id=user1_id, game_id=game_remote.game_id, photo=None, path=self.file_path)

        game_remote = game.send_picture(user_id=user1_id, game_id=game_remote.game_id, photo=photo, path=self.file_path)

        self.assertEqual(game_remote.curr_round, 1)
        self.assertEqual(game_remote.is_photographer, 1)
        self.assertEqual(game_remote.is_turn, 0)

        game_remote_friend = game.get_user_games(user_id=user2_id).games[0]

        self.assertEqual(game_remote_friend.curr_round, 1)
        self.assertEqual(game_remote_friend.is_photographer, 0)
        self.assertEqual(game_remote_friend.is_turn, 1)

    def testGetNewWord(self):
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

        self.assertRaises(game.get_new_word, user_id=user2_id, game_id=game_remote.game_id)

        game_remote_2 = game.get_new_word(user_id=user1_id, game_id=game_remote.game_id)

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

        photo = config.BLANK_PICTURE

        game_remote_1 = game.send_picture(user_id=user1_id, game_id=game_id, photo=photo, path=self.file_path)

        # Have not seen picture yet
        self.assertRaises(RemoteException, game.validate_guess, user_id=user2_id, game_id=game_id, score=200, guess=game_remote_1.curr_word, path=self.file_path)

        game.get_picture(user_id=user2_id, game_id=game_id, path=self.file_path)

        time.sleep(10) # seconds

        game.get_game_status(user_id=user2_id, friend_id=user1_id)

        self.assertRaises(RemoteException, game.validate_guess, user_id=user2_id, game_id=game_id, score=200, guess='pear', path=self.file_path)
        self.assertRaises(RemoteException, game.validate_guess, user_id=user1_id, game_id=game_id, score=200, guess=game_remote_1.curr_word, path=self.file_path)

        game_remote_2 = game.validate_guess(user_id=user2_id, game_id=game_id, score=200, guess=game_remote_1.curr_word, path=self.file_path)

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

class PollTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(5):
            username = 'user' + str(i)
            password = 'pw' + str(i)
            login.create_user(username=username, password=password)

    def testUpdate(self):
        user0_id = User.objects.get(name='user0').obfuscated_id
        user1_id = User.objects.get(name='user1').obfuscated_id
        user2_id = User.objects.get(name='user2').obfuscated_id
        user3_id = User.objects.get(name='user3').obfuscated_id
        user4_id = User.objects.get(name='user4').obfuscated_id

        friend.add_friend(user_id=user0_id, friend_id=user1_id)
        friend.add_friend(user_id=user2_id, friend_id=user0_id)
        friend.add_friend(user_id=user0_id, friend_id=user3_id)
        friend.add_friend(user_id=user4_id, friend_id=user0_id)

        self.assertEqual(len(poll.update(user_id=user0_id).friends), 4)

        friend.remove_friend(user_id=user2_id, friend_id=user0_id)
        friend.block_friend(user_id=user0_id, friend_id=user3_id)
        friend.block_friend(user_id=user4_id, friend_id=user0_id)

        self.assertEqual(len(poll.update(user_id=user0_id).friends), 1)

        self.assertRaises(poll.update, user_id=-1)
