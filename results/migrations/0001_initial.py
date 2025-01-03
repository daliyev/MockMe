# Generated by Django 5.0.2 on 2024-07-26 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('dtmtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtmtest.testcollectionmodel')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.accountsmodel')),
            ],
            options={
                'verbose_name_plural': 'results',
                'db_table': 'result',
            },
        ),
    ]
