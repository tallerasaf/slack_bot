import multiprocessing

from slack_bot import api_server
from slack_bot import average_bot


def main():
    api_server_process = multiprocessing.Process(name='api_server_process', target=api_server.run)
    average_bot_process = multiprocessing.Process(name='average_bot_process', target=average_bot.run)
    api_server_process.start()
    average_bot_process.start()
    # api_server.run()
    # average_bot.run()


if __name__ == '__main__':
    main()
