# Generated by Django 3.1.4 on 2020-12-14 19:24

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
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_name', models.CharField(max_length=25)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Biology', 'Biology'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Business', 'Business'), ('Chemistry', 'Chemistry'), ('Communications', 'Communications'), ('Computer Science', 'Computer Science'), ('Economics', 'Economics'), ('Education', 'Education'), ('Electrical Engineering', 'Electrical Engineering'), ('English', 'English'), ('Environmental Studies', 'Environmental Studies'), ('Finance', 'Finance'), ('Fine Arts', 'Fine Arts'), ('History', 'History'), ('Journalism', 'Journalism'), ('Math', 'Math'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Nursing', 'Nursing'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Pre-Medicine', 'Pre-Medicine'), ('Psychology', 'Psychology'), ('Sociology', 'Sociology')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Brown', 'Brown'), ('Caltech', 'Caltech'), ('Carnegie Mellon', 'Carnegie Mellon'), ('Columbia', 'Columbia'), ('Cornell', 'Cornell'), ('Dartmouth', 'Dartmouth'), ('Duke', 'Duke'), ('Georgia Tech', 'Georgia Tech'), ('Harvard', 'Harvard'), ("John's Hopkins", "John's Hopkins"), ('MIT', 'MIT'), ('New York University', 'New York University'), ('Northwestern', 'Northwestern'), ('Princeton', 'Princeton'), ('Stanford', 'Stanford'), ('UC Berkeley', 'UC Berkeley'), ('UC San Diego', 'UC San Diego'), ('UCLA', 'UCLA'), ('UChicago', 'UChicago'), ('UIUC', 'UIUC'), ('UMich', 'UMich'), ('UPenn', 'UPenn'), ('UT Austin', 'UT Austin'), ('University of Southern California', 'University of Southern California'), ('University of Washington', 'University of Washington'), ('Washington University (St. Louis)', 'Washington University (St. Louis)'), ('Yale', 'Yale')], max_length=100)),
                ('follower', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.editor')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.editor')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='editor',
            name='college',
            field=models.ManyToManyField(to='main.School'),
        ),
        migrations.AddField(
            model_name='editor',
            name='major',
            field=models.ManyToManyField(to='main.Major'),
        ),
    ]