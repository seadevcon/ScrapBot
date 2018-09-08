from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAK4eM42o:APA91bHMMHAJcTw-iQuK-R3CPMbUrqbfXdDj1DJyPljr7gLGmeH6r6RUwpUcfOcuHnLimtkrqWzkbcTux-uMRRX5Mffx4FX7LI5TVXqQ4nCTUV1n8qWQbWhe-9iY22Pu1BOWxsmLxE4L")

def send_notification(imo, owner, lat, lon, timestamp, vtype, name):
    registration_id = "eDIJvk1E-vI:APA91bGWxJweXGA3wlUshcOTfPQh3AjMnI4I8UbE0m_ecWZADWoP_kqTkVZ9fGAoKtAXgIIadgMpV9L6Hry7otyfA9slj2UEFGpGFV8lON4bYdm6QV5kVFwW-_WAU-W1DkyrEu8xBlei"
    message_title = "Scrapping Alert"
    message_body = name + ' entered the Alang scrapping area'
    data = {"imo": imo, "owner": owner, "lat":lat, "lon": lon, "time": timestamp, "vtype": vtype, "name": name}
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               data_message=data, click_action="http://localhost:8887/", message_body=message_body)
