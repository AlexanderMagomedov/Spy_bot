from django.db import models


class Word(models.Model):
    word1 = models.CharField(max_length=32, unique=True)
    word2 = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return f'{self.word1} - {self.word2}'


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    telegram_id = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} - {self.id}'

