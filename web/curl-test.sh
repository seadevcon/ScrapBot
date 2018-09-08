#!/bin/bash
curl -X POST -H "Authorization: key=AAAAK4eM42o:APA91bHMMHAJcTw-iQuK-R3CPMbUrqbfXdDj1DJyPljr7gLGmeH6r6RUwpUcfOcuHnLimtkrqWzkbcTux-uMRRX5Mffx4FX7LI5TVXqQ4nCTUV1n8qWQbWhe-9iY22Pu1BOWxsmLxE4L" -H "Content-Type: application/json" \
   -d '{
  "data": {
    "notification": {
        "title": "FCM Message",
        "body": {"imo": "12o20ß3213"},
        "icon": "/itwonders-web-logo.png",
    }
  },
  "to": "feeFnu_TOBM:APA91bG0iAyxD9RiAJsf2wielDESRgWep-s-UhO4z1W7hkgqUKE5TLZ4b6AKIHMos0Z3KncwvaquQblME5emtQ6IlLOuviD5Nv1UlE5vEdA2w3o7jvAfan5RZoZKKjz3qLt9MuYmTexS"
}' https://fcm.googleapis.com/fcm/send

