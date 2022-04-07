from classic.components import component

from .join_points import join_point
from application import services


@component
class User:
    user: services.User

    @join_point
    def on_get_users(self, request, response):
        users = self.user.get_users()
        response.media = {
            'users': [{
                'id': user.id,
                'username': user.username,
            } for user in users],
        }

    @join_point
    def on_post_add_user(self, request, response):
        self.user.add_user(
            **request.media,
        )
        response.media = {
            'message': 'Пользователь был создан'
        }

    @join_point
    def on_get_info(self, request, response):
        user = self.user.get_user(
            **request.media,
        )
        response.media = {
            'book': {
                'id': user.id,
                'username': user.username,
            },
        }

    @join_point
    def on_post_delete_user(self, request, response):
        self.user.delete_user(**request.media)
        response.media = {
            'message': 'Пользователь был удалён'
        }
