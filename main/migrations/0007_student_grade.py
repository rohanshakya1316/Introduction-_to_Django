# Generated by Django 5.2.4 on 2025-07-31 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.grade'),
        ),
    ]
