# Generated by Django 4.0.8 on 2022-11-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(blank=True, max_length=120, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
