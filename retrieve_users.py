from models import User
from playhouse.shortcuts import model_to_dict


def retrieveUsers(username, per_page, page):
    response = []
    print("estoy aquuiiiiiiii")
    #user = User.select().where(User.username.contains(username)).get().paginate(page, per_page)
    user_1 = User.select().where(User.username.contains(username)).paginate(page, per_page)
    #user_1 = User.get(User.username == username)
    #return model_to_dict(user)
    print(user_1)
    print("paseeeeee")
    for user_response in user_1:
        print("entreeeee")
        response.append(model_to_dict(user_response))
    return str(response)
