# Generated by Django 2.2.18 on 2021-04-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0005_auto_20201202_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='scandefinition',
            name='taggroups_list',
            field=models.ManyToManyField(blank=True, to='assets.AssetCategory'),
        ),
    ]