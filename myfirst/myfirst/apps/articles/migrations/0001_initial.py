# Generated by Django 3.2.6 on 2021-08-03 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='article title')),
                ('article_text', models.TextField(verbose_name='article text')),
                ('pub_date', models.DateTimeField(verbose_name='date of publication')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='author')),
                ('comment_text', models.CharField(max_length=200, verbose_name='comment text')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
