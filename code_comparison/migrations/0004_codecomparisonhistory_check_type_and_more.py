# Generated by Django 5.0.7 on 2024-07-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_comparison', '0003_codecomparisonhistory_diff_content_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='codecomparisonhistory',
            name='check_type',
            field=models.CharField(choices=[('normal', '普通查重'), ('ast', '抽象语法树查重')], default=('normal', '普通查重'), max_length=20),
        ),
        migrations.AddField(
            model_name='codecomparisonhistory',
            name='group_name',
            field=models.CharField(default='default group', max_length=255),
        ),
        migrations.AlterField(
            model_name='codecomparisonhistory',
            name='diff_content',
            field=models.TextField(default=''),
        ),
    ]
