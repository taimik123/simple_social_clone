#from django.contrib import admin

#from . import models


#class GroupMemberInline(admin.TabularInline):
#    model = models.GroupMember



#admin.site.register(models.Group)

from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline]

# Optionally, you can register GroupMemberInline separately if needed:
# admin.site.register(models.GroupMember)

