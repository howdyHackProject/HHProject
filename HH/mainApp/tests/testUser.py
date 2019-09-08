from django.test import TestCase
from mainApp.models import User
from mainApp.database.userDao import UserDao

class TestUser(TestCase):

    def setUp(self):
        self.u = User(first_name = "jargo", last_name="picklsefick", interests = ["thingg", "thing", "other thing"])
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
        self.assertEqual(user.first_name, "jargo")
    

