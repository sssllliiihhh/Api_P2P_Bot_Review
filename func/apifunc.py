from func import dbfunc


def register_user(data):
    if dbfunc.check(data.other_id):
        dbfunc.create_user(data.name, data.link_to_git, data.other_id)
        return "successfully registered"
    else:
        return "user already exists"


def register_text(text):
    if dbfunc.check_link(text.link_to_git):
        dbfunc.create_text(text.text, text.link_to_git, text.other_id)
        return "successfully registered"


def return_queue(id):
    return dbfunc.return_queue(id)