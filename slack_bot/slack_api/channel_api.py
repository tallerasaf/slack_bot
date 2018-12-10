import random


class ChannelApi:
    def __init__(self, slack_client):
        self.slack_client = slack_client

    def get_one_of_the_public_channels_randomly(self):
        public_channels = self._get_public_channels()
        random_channel = random.choice(public_channels)['id']
        return random_channel

    def _get_public_channels(self):
        channels = self.slack_client.api_call("conversations.list")['channels']
        public_channels = [channel for channel in channels
                           if channel['is_channel'] and not channel['is_private']]
        return public_channels
