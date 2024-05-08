# following steps partially as documented on mastodonpy.readthedocs.io

from mastodon import Mastodon

MASTODON_ACCESS_TOKEN = input('Please enter your Mastodon access token: ')
MASTODON_HOST_API_BASE_URL = 'https://mastodon.social'
MASTODON_POST_TEXT = input('What do you want to post on Mastodon? ')

# create and register Mastodon app - only once!
# Mastodon.create_app(
#     'post_string_to_mastodon',
#     api_base_url = 'https://mastodon.social',
#     to_file = 'post_string_to_mastodon_clientcred.secret'
# )

# log in - either every time, or use persisted with credentials
# mastodon = Mastodon(client_id = 'post_string_to_mastodon_clientcred.secret',)
# mastodon.log_in(
#     'walther@stud.fra-uas.de',
#     'wornop-ferxU9-xigsan',
#     to_file = 'post_string_to_mastodon_usercred.secret'
# )

# create actual API instance
# mastodon = Mastodon(access_token = 'post_string_to_mastodon_usercred.secret')
mastodon = Mastodon(access_token=MASTODON_ACCESS_TOKEN, api_base_url=MASTODON_HOST_API_BASE_URL)

# post a toot
result = mastodon.toot(MASTODON_POST_TEXT)

# check if the post was successful
if isinstance(result, dict):
    print('Successfully posted to Mastodon!')
else:
    print('Failed to post to Mastodon.')