from rest_framework.serializers import ModelSerializer
from OneRagTime_app.models import Investments, Investor, Bill, Cashcall

class InvestmentSerializer(ModelSerializer):
    class Meta:
        model = Investments
        fields = ['id', 'startup_name', 'invested_amount', 'investor_id', 'percentage_fees', 'fees_type', 'date_added']

class InvestorSerializer(ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name', 'credit', 'adress', 'email']

class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'investor_id', 'investment_id', 'fees_amount', 'date_added', 'fees_type']

class CashcallSerializer(ModelSerializer):
    class Meta:
        model = Cashcall
        fields =  ['id', 'total_amount', 'IBAN', 'email_send', 'invoice_status', 'date_added']