from OneRagTime_app.models import Bill, Investments, Investor, Cashcall
from OneRagTime_app.api.serializers import BillSerializer, CashcallSerializer, InvestorSerializer
import datetime

def make_cashcall(pk):
    bills = Bill.objects.filter(investor_id=pk)
    bill_serializer = BillSerializer(bills, many=True)
    total_amount = 0
    for bill in bill_serializer.data:
        total_amount = total_amount + bill['fees_amount']
    investor_response = Investor.objects.filter(id=pk)
    investor_serializer = InvestorSerializer(investor_response, many=True)
    new_cash_call = Cashcall.objects.create(total_amount=total_amount, IBAN=extract_iban(investor_serializer.data[0]['credit']),
    email_send='pending', date_added=datetime.date.today(), invoice_status='validated')
    new_cash_call.save()
    cashcall = CashcallSerializer(new_cash_call)
    return cashcall

def extract_iban(credit):
    return ''.join(str(x) for x in list(filter(str.isdigit, credit)))








