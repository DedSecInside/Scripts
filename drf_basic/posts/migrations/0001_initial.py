# Generated by Django 3.0.7 on 2020-06-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_name', models.TextField()),
                ('date', models.DateTimeField()),
                ('article_category', models.TextField()),
                ('category_id', models.IntegerField()),
                ('article_content', models.TextField()),
            ],
        ),
    ]