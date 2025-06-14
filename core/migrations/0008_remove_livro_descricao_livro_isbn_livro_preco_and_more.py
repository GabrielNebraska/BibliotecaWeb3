# Generated by Django 5.1.7 on 2025-06-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_autor_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='descricao',
        ),
        migrations.AddField(
            model_name='livro',
            name='isbn',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='quantidade',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='titulo',
            field=models.CharField(default='', max_length=255),
        ),
    ]
