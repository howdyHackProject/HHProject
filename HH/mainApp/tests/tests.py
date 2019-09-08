from django.test import TestCase
from .models import User
from .services import Service

class TestUser(TestCase):

    def setUp(self):
        self.u = User(first_name = "jargo", last_name="picklsefick", interests = ["thingg", "thing", "other thing"])
        self.serv = Service()

    def tearDown(self):
        del self.u
        del self.serv
    
    def test_insertUserIntoDb(self):
        self.u.save()
        u2 = self.serv.get_user()
        # insert user 'u' into the database
        # create a new user, called "u2", and set that one to retrieve the last thing from db
        # putIntoDB(u)
        # u2 = getShitFromDb(~~hightestUserId)
        self.assertTrue("jargo" ==  u2.first_name)

        # pass
    

