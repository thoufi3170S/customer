# Generated by Django 5.1.6 on 2025-02-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_crmevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRMEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('recipient', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
    ]
