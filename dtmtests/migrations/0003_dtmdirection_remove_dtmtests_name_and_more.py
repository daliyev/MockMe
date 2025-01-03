# Generated by Django 5.0.2 on 2024-07-27 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtmtests', '0002_auto_20240726_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='DtmDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': "Dtm yo'nalish",
                'verbose_name_plural': "Dtm yo'nalishlar",
            },
        ),
        migrations.RemoveField(
            model_name='dtmtests',
            name='name',
        ),
        migrations.AddField(
            model_name='dtmtests',
            name='direction_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='dtmtests.dtmdirection'),
        ),
    ]
