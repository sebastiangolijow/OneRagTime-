from OneRagTime_app.api.send_email import send_mail
from OneRagTime_app.api.make_cashcall import make_cashcall
from OneRagTime_app.models import Cashcall
from django.test import TestCase

class TestEmail(TestCase):
    def test_init(self):
        email_init = send_mail('Test', 'Testing', 'sebastian.golijow@gmail.com', 'test@test.com')
        assert isinstance(email_init, str)
    
class TestMakeCashcall(TestCase):
    def test_init(self):
        cashcall = make_cashcall(1)
        assert isinstance(cashcall, Cashcall)