#!/usr/bin/python3

import requests

# Set authorization token of Mastodon account
MASTODON_ACCESS_TOKEN = 'OEs_7y6TvaIS5eAZVnZBkErwaH8A7NuUjg3g2KRkwzM'

# Set hostname (e.g. mstdn.social) of Mastodon account
MASTODON_HOST = 'mstdn.social'

# Text, den du posten möchtest
OWN_POST_TEXT = "Hallo Mastodon-Welt! Das ist mein eigener Text, den ich auf Mastodon teilen möchte."

# Funktion, um Text auf Mastodon zu posten
def post_to_mastodon(text):
    mastodon_api_url = f'https://{MASTODON_HOST}/api/v1/statuses'
    mastodon_api_auth = {'Authorization': f'Bearer {MASTODON_ACCESS_TOKEN}'}
    mastodon_api_params = {'status': text}
    response = requests.post(mastodon_api_url, data=mastodon_api_params, headers=mastodon_api_auth)
    return response

# Poste den eigenen Text auf Mastodon
response = post_to_mastodon(OWN_POST_TEXT)

# Drucke den Status der Mastodon-API-Anfrage, falls response definiert ist
if response and response.status_code == 200:
    print("Erfolg!")
elif response:
    print(f'Fehler mit Statuscode: {response.status_code}')
else:
    print("Es gab ein Problem beim Senden der Anfrage an die Mastodon-API.")
