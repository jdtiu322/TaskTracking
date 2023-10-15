# Generated by Django 4.2.6 on 2023-10-11 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leader', '0002_remove_leader_userid_leader_user_ptr'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='LeaderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leader.leader'),
            preserve_default=False,
        ),
    ]
