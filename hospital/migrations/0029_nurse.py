# Generated by Django 4.2.2 on 2024-05-05 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0028_alter_room_roomno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/NurseProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('RoomNo', models.PositiveIntegerField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109')], default='101', max_length=50)),
                ('allotmentDate', models.DateField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
