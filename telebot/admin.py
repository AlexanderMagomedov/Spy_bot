from django.contrib import admin

from telebot.models import Word, User, Game


class WordAdmin(admin.ModelAdmin):
    search_fields = ['word1__startswith', 'word2__startswith']


admin.site.register(Word, WordAdmin)
admin.site.register(User)
admin.site.register(Game)
