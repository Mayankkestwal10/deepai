# Generated by Django 2.2.1 on 2019-09-28 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190926_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsandupdate',
            name='id',
        ),
        migrations.AlterField(
            model_name='newsandupdate',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
