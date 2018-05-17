import datetime

from json_ext_encoder import timezone


def test_is_aware():
    utcnow = datetime.datetime.utcnow()
    assert not timezone.is_aware(utcnow)

    utcnow = utcnow.replace(tzinfo=datetime.timezone.utc)
    assert timezone.is_aware(utcnow)
