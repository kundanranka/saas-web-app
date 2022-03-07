# Generated by Django 4.0 on 2022-03-07 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='customers.department'),
        ),
    ]
