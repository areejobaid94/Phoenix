# Generated by Django 2.2.2 on 2019-06-13 08:40

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
            name='Hotels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='SOME STRING', max_length=100)),
                ('country', models.CharField(default='SOME STRING', max_length=100)),
                ('phone', models.CharField(default='SOME STRING', max_length=50)),
                ('image', models.CharField(default='SOME STRING', max_length=500)),
                ('rating', models.CharField(default='SOME STRING', max_length=200)),
                ('price', models.CharField(default='SOME STRING', max_length=200)),
                ('desc', models.CharField(default='SOME STRING', max_length=500)),
                ('link', models.CharField(default='SOME STRING', max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(default='SOME STRING', max_length=100)),
                ('Bio', models.CharField(default='SOME STRING', max_length=200)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myapp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='SOME STRING', max_length=100)),
                ('country', models.CharField(default='SOME STRING', max_length=100)),
                ('Blog', models.TextField(blank=True)),
                ('image', models.CharField(default='SOME STRING', max_length=500)),
                ('ProfileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pheonixapp.Profile')),
            ],
        ),
    ]
