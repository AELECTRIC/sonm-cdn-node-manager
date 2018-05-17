# Generated by Django 2.0.5 on 2018-05-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('region', models.CharField(max_length=100)),
                ('ip4', models.CharField(blank=True, max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('started', models.DateTimeField(null=True)),
                ('heartbeat', models.DateTimeField(null=True)),
                ('deleted', models.DateTimeField(null=True)),
            ],
        ),
    ]