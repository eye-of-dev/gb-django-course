from collections import OrderedDict
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'google-oauth2':
        return

    api_url = urlunparse(('https',
                          'content-people.googleapis.com',
                          '/v1/people/me',
                          None,
                          urlencode(OrderedDict(
                              personFields=','.join(('birthdays', 'genders', 'locales')),
                              access_token=response['access_token']
                          )),
                          None
                          ))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    if resp.json()['locales'][0]['value']:
        user.shopuserprofile.locale = resp.json()['locales'][0]['value']

    if resp.json()['genders'][0]['value']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if resp.json()['genders'][0]['value'] == 'male' \
            else ShopUserProfile.FEMALE

    if resp.json()['birthdays'][0]['date']:
        age = timezone.now().date().year - resp.json()['birthdays'][0]['date']['year']
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

        user.age = age

    user.save()
