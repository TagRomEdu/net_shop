# Generated by Django 4.2.5 on 2023-10-25 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_blog_user_alter_blog_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('set_published', 'Can publish blogs')], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
