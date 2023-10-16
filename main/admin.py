from django.contrib import admin
from django.urls import path
# from main.ClientTransaction import ClientTransactionAdminForm, TransactionProductForm

from main.helperMethod import action_on_delete_puchase
from .models import Client, ClientTransaction, CustomUser, ProductType,Unit,Product,ProductAttribute,Brand,WholeSaler,Purchase
# ProductTypeQuantity

class GaliAdmin(admin.AdminSite):
    site_header = "Gali Admin"
    
gali_admin = GaliAdmin(name='GaliAdmin')

class productTypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
    
gali_admin.register(ProductType,productTypeAdmin)

class BrandAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
    
gali_admin.register(Brand,BrandAdmin)
class UnitAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
gali_admin.register(Unit,UnitAdmin)

class WholeSalerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
gali_admin.register(WholeSaler,WholeSalerAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'brand', 'price', 'quantity')
    list_filter = ('name','type','brand','attributes')  # Example filter
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
gali_admin.register(Product,productAdmin)
# gali_admin.register(Purchase)
# gali_admin.register(ProductTypeQuantity)

class produtAttributeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
gali_admin.register(ProductAttribute,produtAttributeAdmin)

class clientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',)
    list_filter = ('age_group','gender','phone_number')  # Example filter
    search_fields = ('first_name', 'last_name',)  # Example search
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset

gali_admin.register(Client,clientAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    actions = ('delete_model')
    def delete_model(self, request, objs):
        print('============================delete_model============================')
        for item in objs:
            action_on_delete_puchase(item)
        objs.delete()
        print('============================delete_model============================')
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset
    # def delete_model(self, request, obj):
    #     print("deleting................")
    #     pro_base_quan = obj.number_of_unit * obj.unit_type.convertNumber
    #     print(pro_base_quan)
    #     convertTo = obj.unit_type.convertTo
    #     while convertTo:
    #         pro_base_quan = pro_base_quan * convertTo.convertNumber
    #         print(convertTo,convertTo.convertNumber,pro_base_quan)
    #         convertTo = convertTo.convertTo
    #     obj.product.quantity -= pro_base_quan
    #     print("number to delte ",obj.product.quantity,pro_base_quan)
    #     obj.product.save()
    #     obj.delete()
    
gali_admin.register(Purchase, PurchaseAdmin)
class ClientTransactionAdmin(admin.ModelAdmin):
    list_display = ('client','product','product_quantity','transaction_type', 'transaction_date','price_paid')
    list_filter = ('transaction_type',)  # Example filter
    search_fields = ('client', 'last_name',)  # Example search
    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)
        queryset = queryset.filter(vender=user)
        return queryset


gali_admin.register(ClientTransaction,ClientTransactionAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['shop_name']
admin.site.register(CustomUser,CustomUserAdmin)

# class TransactionProductInline(admin.TabularInline):
#     model = Product
#     form = TransactionProductForm
#     extra = 1

# class ClientTransactionAdmin(admin.ModelAdmin):
#     form = ClientTransactionAdminForm
#     inlines = [TransactionProductInline]

# gali_admin.register(ClientTransaction, ClientTransactionAdmin)
