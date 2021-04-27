from models import User
from playhouse.shortcuts import model_to_dict


def retrieveUsers(username, per_page, page):
    response = []
    user_1 = User.select().where(User.username.contains(username)).paginate(page, per_page)
    for user_response in user_1:
        response.append(model_to_dict(user_response))
    return str(response)
