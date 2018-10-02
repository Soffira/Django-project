from django.db import models
import datetime
import django.utils.timezone


class Category(models.Model):

    title = models.CharField(
        max_length=250,
        unique=True
    )

    snippet = models.TextField(
        blank=True,
        null=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=250,
        unique=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        blank=True,
        null=True
    )

    snippet = models.TextField(
        blank=True,
        null=True
    )

    cost = models.DecimalField(
        max_digits=12,      #max_digits= ������������ ���������� �������� �� � ����� ������� � ����
        decimal_places=2,    #���������� ��������, ����� ������� �� ������� ���������� ��������(2 �� 12)     
        default=0
    )

    modified = models.DateTimeField(
        auto_now=True           #��� ���� ��������� ���� ������� ��������� � ������-�� �������������
    )

    created = models.DateTimeField(
        auto_now_add=True           #��� ���� ������ � ������-�� �������������
    )

    def __str__(self):
        return self.title