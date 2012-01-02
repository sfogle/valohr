from valohr.models import Room, Bed
from django.contrib import admin


#class RoomAdmin(admin.ModelAdmin):
    #fields = ['room_name', 'beds']
    #list_display = ('room_name')

#admin.site.register(Room, RoomAdmin)

class BedInline(admin.TabularInline):
    model = Bed

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        BedInline,
    ]

admin.site.register(Room, RoomAdmin)
