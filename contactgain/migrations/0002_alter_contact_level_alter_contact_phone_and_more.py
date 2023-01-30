# Generated by Django 4.1 on 2023-01-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactgain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact', to='contactgain.level'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=234),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='maximum_contact',
            field=models.IntegerField(default=0),
        ),
    ]