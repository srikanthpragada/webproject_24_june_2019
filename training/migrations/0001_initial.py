# Generated by Django 2.2.2 on 2019-08-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('course', models.CharField(max_length=5)),
                ('feepaid', models.IntegerField()),
            ],
        ),
    ]
