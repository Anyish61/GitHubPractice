# Generated by Django 2.2.4 on 2020-05-25 08:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('testing1', '0003_auto_20200525_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='are_you_ok',
            field=otree.db.models.BooleanField(choices=[['很好', True], ['還好', False]], null=True, verbose_name='你今天好嗎？'),
        ),
    ]
