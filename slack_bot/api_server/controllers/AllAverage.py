from flask_restful import Resource
import os
from slackclient import SlackClient

from ...slack_api import Api


SLACK_TOKEN = os.environ["SLACK_API_TOKEN"]
slack_client = SlackClient(SLACK_TOKEN)


class AllAverage(Resource):
    def get(self):
        slack_api = Api(slack_client)
        channel_id = slack_api.get_one_of_the_public_channels_randomly()
        average = slack_api.get_average_numbers_in_channel(channel_id=channel_id)
        return {channel_id: average}
