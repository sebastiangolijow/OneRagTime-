from xml.dom.pulldom import parseString
from rest_framework.viewsets import ModelViewSet
from OneRagTime_app.models import Investments, Investor, Bill, Cashcall
from OneRagTime_app.api.serializers import  InvestmentSerializer, InvestorSerializer,  BillSerializer, CashcallSerializer
from rest_framework.response import Response
from OneRagTime_app.api.make_cashcall import make_cashcall
from OneRagTime_app.api.send_email import send_mail

class InvestmentEndpoint(ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investments.objects.all()


class InvestorEndpoint(ModelViewSet):
    serializer_class = InvestorSerializer
    queryset = Investor.objects.all()

class BillEndpoint(ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class CashcallEndpoint(ModelViewSet):
    serializer_class = CashcallSerializer
    queryset = Cashcall.objects.all()

class GenerateBillsEndpoint(ModelViewSet):
    serializer_class = InvestmentSerializer
    def get_queryset(self):
        investments_specs = Investments.objects.all()
        return investments_specs
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        investment_response = Investments.objects.filter(investor_id=params['pk'])
        serializer = InvestmentSerializer(investment_response, many=True)
        for investment in serializer.data:
            new_bill = Bill.objects.create(investor_id=investment['investor_id'], investment_id=investment['id'], fees_amount=investment['invested_amount'], 
            date_added=investment['date_added'], fees_type=investment['fees_type'])
            new_bill.save()
        make_cashcall(params['pk'])
        bills = Bill.objects.filter(investor_id=params['pk'])
        bill_serializer = BillSerializer(bills, many=True)
        return Response(bill_serializer.data)

class SendEmailEndpoint(ModelViewSet):
    serializer_class = CashcallSerializer

    def get_queryset(self):
        pass

    def create(self, request, *args, **kwargs):
        params = kwargs
        cashcall_response = Cashcall.objects.filter(investor_id=params['pk'])
        serializer = CashcallSerializer(cashcall_response, many=True)
        investor_response = Investor.objects.filter(id=params['pk'])
        investor_serializer = InvestorSerializer(investor_response, many=True)
        send_mail(serializer.data, 'Cashcall', 'seba@oneragtime.com', investor_serializer.data[0]['email'])
        Cashcall.objects.filter(investor_id=params['pk'], many=True)[0].update(invoice_status='sent', email_send='sent')
        return Response('Email sent')
    
