# Generated by Django 3.1.5 on 2021-02-06 08:38

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('prdsolapp', '0005_auto_20210206_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='District',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='State', chained_model_field='state', default=1, on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.district'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.state'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='District', chained_model_field='District', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.city'),
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('Branch_name', 'city', 'State', 'District')},
        ),
    ]
