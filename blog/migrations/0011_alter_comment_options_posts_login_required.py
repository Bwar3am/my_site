# Generated by Django 4.2.7 on 2024-02-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='posts',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]