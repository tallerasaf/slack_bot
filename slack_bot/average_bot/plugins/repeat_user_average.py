from rtmbot.core import Plugin

from .config import BOT_NAME
from ...slack_api import Api


class RepeatUserAveragePlugin(Plugin):
    def process_message(self, data):
        slack_api = Api(self.slack_client)
        bot_user_id = slack_api.get_user_id_by_user_name(BOT_NAME)
        if data['user'] != bot_user_id:
            average = slack_api.get_average_numbers_user_wrote_in_channel(user_id=data['user'],
                                                                          channel_id=data['channel'])
            self.outputs.append([
                    data['channel'],
                    f'The average number is: "{average:.3f}", from user: \"{data["user"]}\"'
                ])
