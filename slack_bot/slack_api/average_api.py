from statistics import mean


class AverageApi:
    def __init__(self, slack_client):
        self.slack_client = slack_client

    def get_average_of_numbers(self, channel_id, user_id=None):
        conversations_history = self.slack_client.api_call("conversations.history", channel=channel_id)
        average = self._get_average_of_numbers(messages=conversations_history['messages'], user_id=user_id)
        return average

    def _get_average_of_numbers(self, messages, user_id=None):
        messages_text = self._get_messages_text(messages=messages, user_id=user_id)
        if not messages_text:
            return -1
        numbers = map(int, messages_text)
        return mean(numbers)

    def _get_messages_text(self, messages, user_id=None):
        text_messages = self._get_messages_filtered_by_numbers(messages)
        if user_id:
            text_messages = self._get_messages_filtered_by_user(messages=text_messages, user_id=user_id)
        return self._get_text_from_messages(text_messages)

    def _get_text_from_messages(self, messages):
        return [message.get('text', 0) for message in messages]

    def _get_messages_filtered_by_numbers(self, messages):
        return [message for message in messages if message.get('text', 0).isdecimal()]

    def _get_messages_filtered_by_user(self, messages, user_id):
        return [message for message in messages if message.get('user') == user_id]
