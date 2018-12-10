from rtmbot import RtmBot
import os

SLACK_TOKEN = os.environ["SLACK_API_TOKEN"]

config = {
    "SLACK_TOKEN": SLACK_TOKEN,
    "ACTIVE_PLUGINS": [
        "slack_bot.average_bot.plugins.repeat_user_average.RepeatUserAveragePlugin",
        "slack_bot.average_bot.plugins.schedule_all_average.ScheduleAllAveragePlugin"
    ]
}


def run():
    bot = RtmBot(config)
    bot.start()
