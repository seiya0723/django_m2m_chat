from django.contrib import admin


from .models import Chat,ChatGroup

class ChatGroupAdmin(admin.ModelAdmin):

    list_display    = ["id","dt","members"]


    #多対多のフィールドはそのまま表示できない
    def members(self,obj):
        if obj.member:
            member_list = [ member.username for member in obj.member.all() ]

            return member_list



admin.site.register(Chat)
admin.site.register(ChatGroup,ChatGroupAdmin)

