from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Contact, Product, Participant, Supplier
from django_admin_relation_links import AdminChangeLinksMixin


@admin.action(description='Удалить задолженность')
def remove_debt(self, request, queryset):
    remove_debt = queryset.update(debt=0.00)
    self.message_user(request, ngettext("%d задолженность удалена",
                                        "%d задолженности удалены", remove_debt) % remove_debt, messages.SUCCESS)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "number")
    search_fields = ("email", "country", "city", "street", "number")
    list_editable = ("country", "city", "street", "number")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "model", "issued", "show_sellers")
    search_fields = ("title", "model", "issued", "show_sellers")
    list_editable = ["model"]

    def show_sellers(self, obj):
        return "\n".join([a.title for a in obj.sellers.all()])


class ParticipantAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ("title", "level", "contact", "show_products", "created")
    search_fields = ("title", "level", "contact", "show_products", "created")
    list_editable = ("level", "contact")
    list_filter = ['contact__city']
    changelist_links = [
        ('buyer', {
            'label': 'Поставщик',
            'model': 'Supplier'
        })
    ]

    def show_products(self, obj):
        return "\n".join([a.title for a in obj.products.all()])


class SupplierAdmin(admin.ModelAdmin):
    list_display = ("seller", "buyer", "debt")
    search_fields = ("seller", "buyer", "debt")
    list_editable = ("buyer", "debt")
    actions = [remove_debt]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Supplier, SupplierAdmin)
