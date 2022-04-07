from classic.app import AppError


class DoesNotExists(AppError):
    msg_template = "This object does not exists"
    code = 'not_exist'
