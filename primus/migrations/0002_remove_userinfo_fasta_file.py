# Generated by Django 2.0.8 on 2018-09-20 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='fasta_file',
        ),
    ]
