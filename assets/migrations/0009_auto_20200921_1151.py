# Generated by Django 2.2.16 on 2020-09-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_asset_exposure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='exposure',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('external', 'External'), ('internal', 'Internal'), ('restricted', 'Restricted')], default='unknown', max_length=16),
        ),
    ]
