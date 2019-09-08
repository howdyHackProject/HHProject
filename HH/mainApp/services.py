from mainApp.models import User

def create_user(User.user, firstname, lastname, interests):
    u = user(first_name=first_name, last_name=last_name, interests=interests)
    u.save()

def get_user(User.user, id):
    User.objects.get(id=id)

def get_all_users(User.user):
    User.objects.all()