# Generated by Django 4.0 on 2022-01-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customer_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
