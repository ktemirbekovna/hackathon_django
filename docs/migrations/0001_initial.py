# Generated by Django 3.2.8 on 2021-10-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_work', models.CharField(max_length=100)),
                ('doctor_experience', models.CharField(max_length=100)),
                ('doctor_number', models.CharField(max_length=100)),
                ('doctor_nurse', models.CharField(max_length=100)),
                ('doctor_pasients', models.CharField(max_length=200)),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Sawbones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_work', models.CharField(max_length=100)),
                ('doctor_experience', models.CharField(max_length=100)),
                ('doctor_number', models.CharField(max_length=100)),
                ('doctor_nurses', models.IntegerField()),
                ('doctor_patients', models.CharField(max_length=200)),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_number', models.CharField(max_length=100)),
                ('patient_doc', models.CharField(max_length=100)),
                ('patient_diagnostic', models.CharField(max_length=255)),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_work', models.CharField(max_length=100)),
                ('doctor_experience', models.CharField(max_length=100)),
                ('doctor_number', models.CharField(max_length=100)),
                ('doctor_patients', models.CharField(max_length=200)),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Maindoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_work', models.CharField(max_length=100)),
                ('doctor_experience', models.CharField(max_length=100)),
                ('doctor_number', models.CharField(max_length=100)),
                ('doctor_sawbones', models.IntegerField()),
                ('doctor_therapist', models.IntegerField()),
                ('doctor_nurses', models.IntegerField()),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Hosp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_name', models.CharField(max_length=100)),
                ('hosp_number', models.CharField(max_length=100)),
                ('hosp_maindoc', models.CharField(max_length=155)),
                ('hosp_docs', models.IntegerField()),
                ('hosp_nurses', models.IntegerField()),
                ('hosp_patients', models.IntegerField()),
                ('del_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.hospital')),
            ],
        ),
    ]
