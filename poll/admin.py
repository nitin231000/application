from django.contrib import admin
from poll.models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ('question','option_one','option_two','option_three','option_one_count','option_two_count','option_three_count')

admin.site.register(Poll,PollAdmin)

