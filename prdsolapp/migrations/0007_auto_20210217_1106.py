# Generated by Django 3.1.5 on 2021-02-17 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prdsolapp', '0006_auto_20210206_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name_plural': 'Bank'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'City'},
        ),
        migrations.AlterModelOptions(
            name='designation',
            options={'verbose_name_plural': 'Designation'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'District'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name_plural': 'Grade'},
        ),
        migrations.AlterModelOptions(
            name='keyskill',
            options={'verbose_name_plural': 'KeySkill'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'State'},
        ),
        migrations.AlterModelOptions(
            name='vertical',
            options={'verbose_name_plural': 'Vertical'},
        ),
    ]
