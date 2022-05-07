from django.contrib import admin
from OneRagTime_app.models import Investments, Investor, Bill, Cashcall

@admin.register(Investments) ##registrar modelo en el panel administrador
class InvestmentsAdmin(admin.ModelAdmin):
    list_display = ['startup_name', 'invested_amount']

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['investor_id', 'fees_amount']

@admin.register(Cashcall)
class CashcallAdmin(admin.ModelAdmin):
    list_display = ['total_amount', 'invoice_status']