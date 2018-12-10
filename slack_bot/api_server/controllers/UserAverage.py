from flask_restful import Resource
import os
from slackclient import SlackClient

from ...slack_api import Api


SLACK_TOKEN = os.environ["SLACK_API_TOKEN"]
slack_client = SlackClient(SLACK_TOKEN)


class UserAverage(Resource):
    def get(self, slack_username):
        slack_api = Api(slack_client)
        channel_id = slack_api.get_one_of_the_public_channels_randomly()
        user_id = slack_api.get_user_id_by_user_name(slack_username)
        average = slack_api.get_average_numbers_user_wrote_in_channel(user_id=user_id,
                                                                      channel_id=channel_id)
        return {channel_id: average}
