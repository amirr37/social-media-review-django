from django.contrib import admin

from Account.models import Relation


# Register your models here.


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass

