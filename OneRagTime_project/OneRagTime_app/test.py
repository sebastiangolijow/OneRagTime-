from OneRagTime_app.api.send_email import send_mail
from django.test import TestCase

class TestEmail(TestCase):
    def test_init(self):
        email_init = send_mail('Test', 'Testing', 'sebastian.golijow@gmail.com', 'test@test.com')
        assert isinstance(email_init, str) 