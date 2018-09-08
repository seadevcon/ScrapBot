from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAK4eM42o:APA91bHMMHAJcTw-iQuK-R3CPMbUrqbfXdDj1DJyPljr7gLGmeH6r6RUwpUcfOcuHnLimtkrqWzkbcTux-uMRRX5Mffx4FX7LI5TVXqQ4nCTUV1n8qWQbWhe-9iY22Pu1BOWxsmLxE4L")

def send_notification(imo, owner, lat, lon, timestamp, vtype):
    registration_id = "ezk9vz373Ps:APA91bHKz5UOGzbcqOuZnTW6ZN-pMFtlJbenqcdANyYYd8qSJGvGs18iB7b1VxgRcU06Q9ez3j3n0bfccMv2Cpb2xapCx1DKxqsTSMJn4ESaagWGGtDHTZZb1CdQl6lzAn1QuDv7qO_P"
    message_title = "Vessel enters scrapping area"
    message_body = {"imo": imo, "owner": owner, "lat":lat, "lon": lon, "time": timestamp, "vtype": vtype}
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
