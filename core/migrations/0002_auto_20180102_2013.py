# Generated by Django 2.0 on 2018-01-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address_city',
            field=models.CharField(default='tbd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='address_state',
            field=models.CharField(default='tbd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='address_street',
            field=models.CharField(default='tbd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='address_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='address_zip',
            field=models.CharField(default='tbd', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.ManyToManyField(blank=True, to='core.Level'),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
    ]