# Generated by Django 4.2.6 on 2023-10-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leader', '0002_remove_leader_userid_leader_user_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='LeaderID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
