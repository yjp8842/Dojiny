# Generated by Django 3.2.7 on 2022-11-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behinds', '0007_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
