from .channel_api import ChannelApi
from .average_api import AverageApi
from .user_api import UserApi


class Api:
    def __init__(self, slack_client):
        self.slack_client = slack_client
        self.channel_api = ChannelApi(self.slack_client)
        self.user_api = UserApi(self.slack_client)
        self.average_api = AverageApi(self.slack_client)

    def get_average_numbers_user_wrote_in_channel(self, user_id, channel_id):
        return self.average_api.get_average_of_numbers(user_id=user_id, channel_id=channel_id)

    def get_average_numbers_in_channel(self, channel_id):
        return self.average_api.get_average_of_numbers(channel_id=channel_id)

    def get_one_of_the_public_channels_randomly(self):
        return self.channel_api.get_one_of_the_public_channels_randomly()

    def get_user_id_by_user_name(self, user_name):
        return self.user_api.get_user_id_by_username(user_name)
