import secrets
from datetime import datetime, timedelta
import jwt
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from tracker.models import Mouvements


class Command(BaseCommand):

    def handle(self, *args, **options):
        """a = secrets.token_urlsafe()
        print(a)"""
        ids = get_user_model().objects.values('id')
        ADMIN_USER_ID = ids[0]
        JWT_EXP_DELTA_SECONDS = 86400

        payload = {
            'user_id': ADMIN_USER_ID,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        encoded_jwt = jwt.encode(payload, "secret", algorithm="HS256")
        print(encoded_jwt)
        decode = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
        print(decode)
