# Generated by Django 3.2.7 on 2021-09-18 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_change', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.item', verbose_name='Продукт')),
            ],
        ),
    ]
