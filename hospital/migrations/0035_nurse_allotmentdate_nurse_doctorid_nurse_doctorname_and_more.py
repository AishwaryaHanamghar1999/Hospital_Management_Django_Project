# Generated by Django 4.2.2 on 2024-05-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0034_room_doctorid_room_doctorname_room_patientid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='allotmentDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='roomno',
            field=models.IntegerField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109')], default='101', max_length=50),
        ),
        migrations.AddField(
            model_name='nurse',
            name='roomtype',
            field=models.CharField(choices=[('General', 'General'), ('Private', 'Private'), ('ICU(Intensive Care Unit)', 'ICU(Intensive Care Unit)'), ('CCU(Cardiac/Coronary Care Unit)', 'CCU(Cardiac/Coronary Care Unit)'), ('Operation', 'Operation'), ('Surgical', 'Surgical'), ('MaternityCare', 'MaternityCare')], default='General Ward', max_length=50),
        ),
    ]