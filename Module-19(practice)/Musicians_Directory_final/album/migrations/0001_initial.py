# Generated by Django 4.2.7 on 2023-12-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200)),
                ('album_relese_date', models.DateField(blank=True, null=True)),
                ('ratings', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicians.musician')),
            ],
        ),
    ]
