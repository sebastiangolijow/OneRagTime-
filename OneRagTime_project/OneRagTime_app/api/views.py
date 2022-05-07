from xml.dom.pulldom import parseString
from rest_framework.viewsets import ModelViewSet
from OneRagTime_app.models import Investments, Investor, Bill, Cashcall
from OneRagTime_app.api.serializers import  InvestmentSerializer, InvestorSerializer,  BillSerializer, CashcallSerializer

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