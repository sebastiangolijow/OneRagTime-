from posixpath import basename
from sys import prefix
from rest_framework.routers import DefaultRouter
from OneRagTime_app.api.views import  InvestmentEndpoint, InvestorEndpoint, BillEndpoint, CashcallEndpoint

router_endpoint_investment = DefaultRouter()
router_endpoint_investor = DefaultRouter()
router_endpoint_bill = DefaultRouter()
router_endpoint_cashcall = DefaultRouter()



router_endpoint_investment.register(prefix='investments', basename='investments', viewset= InvestmentEndpoint)
router_endpoint_investor.register(prefix='investor', basename='investor', viewset= InvestorEndpoint)
router_endpoint_bill.register(prefix='bill', basename='bill', viewset= BillEndpoint)
router_endpoint_cashcall.register(prefix='cashcall', basename='cashcall', viewset= CashcallEndpoint)



