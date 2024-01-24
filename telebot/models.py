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
        verbose_name = 'Телеграм пользователь'
        verbose_name_plural = 'Телеграм пользователи'

    def __str__(self):
        return f'{self.name} - {self.telegram_id}'


class Game(models.Model):
    peace = models.PositiveSmallIntegerField(default=1)
    spy = models.PositiveSmallIntegerField(default=1)
    undercover = models.PositiveSmallIntegerField(default=1)
    telegram = models.CharField(max_length=32, unique=True, primary_key=True)
    word = models.ForeignKey(to=Word, related_name='word', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return f'{self.telegram} угадывают слово {self.word}'
