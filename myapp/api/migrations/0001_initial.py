# Generated by Django 4.1.1 on 2022-09-11 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='band/logo')),
            ],
            options={
                'verbose_name_plural': 'Bands',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='band/member')),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='band_members', to='api.band')),
            ],
            options={
                'verbose_name_plural': 'BandMembers',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(choices=[('Acoustic', 'Acoustic'), ('Electric', 'Electric'), ('Bass', 'Bass')], max_length=40)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guitars', to='api.bandmember')),
            ],
            options={
                'verbose_name_plural': 'Guitars',
                'ordering': ('-created_at',),
            },
        ),
    ]
