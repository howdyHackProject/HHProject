from django.test import TestCase
from mainApp.models import User
from mainApp.database.userDao import UserDao

class TestUser(TestCase):

    def setUp(self):
        self.u = User(
            firstName = "a", 
            lastName = "b", 
            interests = ["walk", "run", "sit"]
            )
        self.dao = UserDao()

    def tearDown(self):
        del self.u
        del self.dao
    
    def test_insertAndRetrieve(self):
        # arrange
        self.u.save()
        # act
        user = self.dao.get_user()
        # assert
        self.assertEqual(user.first_name, "a")
    

