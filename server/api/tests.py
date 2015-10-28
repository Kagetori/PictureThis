from django.test import TestCase

from models import User

from interface.exception import RemoteException

import login, search

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
        # Make a few users to test making
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
        try:
            search.find_user(username='nonexistent')
        except RemoteException:
            pass # TODO check error message too

