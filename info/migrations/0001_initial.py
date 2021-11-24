# Generated by Django 3.2.9 on 2021-11-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.family')),
            ],
        ),
    ]
