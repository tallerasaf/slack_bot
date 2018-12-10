class UserApi:
    def __init__(self, slack_client):
        self.slack_client = slack_client

    def get_user_id_by_username(self, user_name):
        users = self.slack_client.api_call("users.list")
        for user in users['members']:
            if user['real_name'] == user_name:
                return user['id']
        return None
