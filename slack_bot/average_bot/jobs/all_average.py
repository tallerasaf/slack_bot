from rtmbot.core import Job

from ...slack_api import Api


class AllAverageJob(Job):
    def run(self, slack_client):
        slack_api = Api(slack_client)
        channel_id = slack_api.get_one_of_the_public_channels_randomly()
        average = slack_api.get_average_numbers_in_channel(channel_id)
        return [[
            channel_id,
            f'The average number is: "{average:.3f}", from all the users.'
        ]]
