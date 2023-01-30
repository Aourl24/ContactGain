# Generated by Django 4.1 on 2023-01-29 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
                ('contact_list', models.ManyToManyField(blank=True, null=True, to='contactgain.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_number', models.IntegerField(default=1, unique=True)),
                ('proof', models.IntegerField(default=3)),
                ('maximum_contact', models.IntegerField(default=50)),
                ('download_link', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='The proof/')),
                ('active', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proof', to='contactgain.contact')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='level',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact', to='contactgain.level'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL),
        ),
    ]