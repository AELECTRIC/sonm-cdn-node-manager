# Generated by Django 2.0.5 on 2018-08-17 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180816_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='last_sent_bytes',
            field=models.BigIntegerField(blank=True, help_text='Последний замер объема отданного трафика с хоста', null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='last_sent_bytes_dt',
            field=models.DateTimeField(blank=True, help_text='Время последнего', null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='prev_sent_bytes',
            field=models.BigIntegerField(blank=True, help_text='Предыдущий замер объема отданного трафика с хоста', null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='prev_sent_bytes_dt',
            field=models.DateTimeField(blank=True, help_text='Время вредыдущего замера', null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='throughput',
            field=models.BigIntegerField(blank=True, help_text='Максимальная пропускная способность хоста. В байтах.', null=True),
        ),
    ]