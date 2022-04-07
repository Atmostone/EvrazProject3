from classic.components import component

from .join_points import join_point
from application import services


@component
class User:
    user: services.User

    @join_point
    def on_get_users(self, request, response):
        users = self.гыук.get_users()
        response.media = {
            'users': str(users),
        }

    @join_point
    def on_post_add_user(self, request, response):
        self.user.add_user(
            **request.media,
        )
        response.media = {
            'message': 'Пользователь был создан'
        }
