from flask import current_app
import json
import requests


def notify_user(player_id, title, message, subtitle=None):
    """
    Sends push notification to a single user.
    :param player_id: String - Signal One id of user
    :param title: String - title of notification
    :param message: String - body of notification
    :param subtitle: String - optional subtitle of notification
    :return: None
    """
    api_key = current_app.config['ONE_SIGNAL_KEY']
    headers = {"Authorization": "Basic {}".format(api_key),
               'Content-Type': 'application/json; charset=utf-8'}
    body = {"include_player_ids": [player_id],
            "app_id": current_app.config['ONE_SIGNAL_APP_ID'],
            "contents": {"en": message},
            "headings": {"en": title},
            "ios_badgeType": "Increase",
            "ios_badgeCount": 1}
    if subtitle:
        body["subtitle"] = {"en": subtitle}
    url = 'https://onesignal.com/api/v1/notifications'
    r = requests.post(url, headers=headers, data=json.dumps(body))
    res = r.json()
    if r.status_code == 400:
        current_app.logger.error('Got 400 trying to send push notification \
                to player_id: ({})'.format(player_id))
    else:
        if res.get('errors'):
            current_app.logger.error('Error sending push notification: \
                ({})'.format(res.get('errors')))
    return None
