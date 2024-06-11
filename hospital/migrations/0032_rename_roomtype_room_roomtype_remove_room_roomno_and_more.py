# Generated by Django 4.2.2 on 2024-05-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0031_remove_room_doctorname_remove_room_patientname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='RoomType',
            new_name='roomtype',
        ),
        migrations.RemoveField(
            model_name='room',
            name='RoomNo',
        ),
        migrations.AddField(
            model_name='room',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='roomno',
            field=models.IntegerField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109')], default='101', max_length=50),
        ),
    ]