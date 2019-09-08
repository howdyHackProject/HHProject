from mainApp.models import User

class UserDao:

    def get_user(self):
        return User.objects.all().filter().order_by('-id')[0]

    # def get_all_users(self):
    #     return User.objects.all()