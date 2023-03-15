# Generated by Django 4.1.7 on 2023-03-15 06:10

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
            name='filturm',
            fields=[
                ('filturmid', models.BigAutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=200)),
                ('mname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=200)),
                ('birthplacetaluka', models.CharField(max_length=200)),
                ('bpd', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('languageknown', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('maristetus', models.CharField(max_length=200)),
                ('bloodgroup', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=200)),
                ('category', models.CharField(default=0, max_length=50)),
                ('emailid', models.CharField(max_length=255)),
                ('contactno', models.CharField(max_length=200)),
                ('emergencycontactno', models.CharField(max_length=20)),
                ('ak', models.CharField(max_length=200)),
                ('adharimage', models.ImageField(upload_to='')),
                ('pancardno', models.CharField(max_length=200)),
                ('panimage', models.ImageField(upload_to='')),
                ('pad', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('permanentaddress', models.CharField(max_length=200)),
                ('perpincode', models.CharField(max_length=20)),
                ('Eii', models.ImageField(upload_to='')),
                ('ssc', models.CharField(default=0, max_length=200)),
                ('sscbord', models.CharField(default=0, max_length=200)),
                ('sscpersentage', models.CharField(default=0, max_length=200)),
                ('sscpassingyear', models.CharField(default=0, max_length=200)),
                ('ssccertificate', models.ImageField(default=0, upload_to='')),
                ('hsc', models.CharField(default=0, max_length=200)),
                ('hsccbord', models.CharField(default=0, max_length=200)),
                ('hsccpersentage', models.CharField(default=0, max_length=200)),
                ('hscpassingyear', models.CharField(default=0, max_length=200)),
                ('hsccertificate', models.ImageField(default=0, upload_to='')),
                ('diploma', models.CharField(default='', max_length=200)),
                ('diplomabord', models.CharField(default='', max_length=200)),
                ('diplomapersentage', models.CharField(default='', max_length=200)),
                ('diplomapassingyear', models.CharField(default='', max_length=200)),
                ('diplomacertificate', models.ImageField(default=0, upload_to='')),
                ('gradution', models.CharField(default='', max_length=200)),
                ('gradutionbord', models.CharField(default='', max_length=200)),
                ('gradutionpersentage', models.CharField(default='', max_length=200)),
                ('gradutionpassingyear', models.CharField(default='', max_length=200)),
                ('gradutioncertificate', models.ImageField(default=0, upload_to='')),
                ('postgradution', models.CharField(default='', max_length=200)),
                ('postgradutionbord', models.CharField(default='', max_length=200)),
                ('postgradutionpersentage', models.CharField(default='', max_length=200)),
                ('postgradutionpassingyear', models.CharField(default='', max_length=200)),
                ('postgradutioncertificate', models.ImageField(default=0, upload_to='')),
                ('other', models.CharField(default='', max_length=200)),
                ('institude', models.CharField(default='', max_length=200)),
                ('corsename', models.CharField(default=0, max_length=200)),
                ('corsepersentage', models.CharField(default=0, max_length=200)),
                ('corsecertificate', models.ImageField(default='', upload_to='')),
                ('father', models.CharField(default=0, max_length=200)),
                ('fdob', models.DateField(default=0)),
                ('fage', models.CharField(default=0, max_length=200)),
                ('fgen', models.CharField(default=0, max_length=200)),
                ('frelation', models.CharField(default=0, max_length=200)),
                ('mather', models.CharField(default=0, max_length=200)),
                ('mdob', models.DateField(default=0)),
                ('mage', models.CharField(default=0, max_length=200)),
                ('mgen', models.CharField(default=0, max_length=200)),
                ('mrelation', models.CharField(default=0, max_length=200)),
                ('cihldren1', models.CharField(default=0, max_length=200)),
                ('c1dob', models.DateField(default=0)),
                ('c1age', models.CharField(default=0, max_length=200)),
                ('c1gen', models.CharField(default=0, max_length=200)),
                ('c1relation', models.CharField(default=0, max_length=200)),
                ('children2', models.CharField(default=0, max_length=200)),
                ('c2dob', models.DateField(default=0)),
                ('c2age', models.CharField(default=0, max_length=200)),
                ('c2gen', models.CharField(default=0, max_length=200)),
                ('c2relation', models.CharField(default=0, max_length=200)),
                ('companyname', models.CharField(default=0, max_length=200)),
                ('durationfrom', models.DateField(default=0)),
                ('durationto', models.DateField(default=0)),
                ('joiningctc', models.CharField(default=0, max_length=200)),
                ('lctc', models.CharField(default=0, max_length=200)),
                ('twe', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HrLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mainfilturm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('mname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=200)),
                ('birthplacetaluka', models.CharField(max_length=200)),
                ('bpd', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('languageknown', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('maristetus', models.CharField(max_length=200)),
                ('bloodgroup', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=200)),
                ('category', models.CharField(default=0, max_length=50)),
                ('emailid', models.CharField(max_length=255)),
                ('contactno', models.CharField(max_length=200)),
                ('emergencycontactno', models.CharField(max_length=20)),
                ('ak', models.CharField(max_length=200)),
                ('adharimage', models.ImageField(upload_to='')),
                ('pancardno', models.CharField(max_length=200)),
                ('panimage', models.ImageField(upload_to='')),
                ('pad', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('permanentaddress', models.CharField(max_length=200)),
                ('perpincode', models.CharField(max_length=20)),
                ('Eii', models.ImageField(upload_to='')),
                ('ssc', models.CharField(default=0, max_length=200)),
                ('sscbord', models.CharField(default=0, max_length=200)),
                ('sscpersentage', models.CharField(default=0, max_length=200)),
                ('sscpassingyear', models.CharField(default=0, max_length=200)),
                ('ssccertificate', models.ImageField(default=0, upload_to='')),
                ('hsc', models.CharField(default=0, max_length=200)),
                ('hsccbord', models.CharField(default=0, max_length=200)),
                ('hsccpersentage', models.CharField(default=0, max_length=200)),
                ('hscpassingyear', models.CharField(default=0, max_length=200)),
                ('hsccertificate', models.ImageField(default=0, upload_to='')),
                ('diploma', models.CharField(default='', max_length=200)),
                ('diplomabord', models.CharField(default='', max_length=200)),
                ('diplomapersentage', models.CharField(default='', max_length=200)),
                ('diplomapassingyear', models.CharField(default='', max_length=200)),
                ('diplomacertificate', models.ImageField(default=0, upload_to='')),
                ('gradution', models.CharField(default='', max_length=200)),
                ('gradutionbord', models.CharField(default='', max_length=200)),
                ('gradutionpersentage', models.CharField(default='', max_length=200)),
                ('gradutionpassingyear', models.CharField(default='', max_length=200)),
                ('gradutioncertificate', models.ImageField(default=0, upload_to='')),
                ('postgradution', models.CharField(default='', max_length=200)),
                ('postgradutionbord', models.CharField(default='', max_length=200)),
                ('postgradutionpersentage', models.CharField(default='', max_length=200)),
                ('postgradutionpassingyear', models.CharField(default='', max_length=200)),
                ('postgradutioncertificate', models.ImageField(default=0, upload_to='')),
                ('other', models.CharField(default='', max_length=200)),
                ('institude', models.CharField(default='', max_length=200)),
                ('corsename', models.CharField(default=0, max_length=200)),
                ('corsepersentage', models.CharField(default=0, max_length=200)),
                ('corsecertificate', models.ImageField(default='', upload_to='')),
                ('father', models.CharField(default=0, max_length=200)),
                ('fdob', models.DateField(default=0)),
                ('fage', models.CharField(default=0, max_length=200)),
                ('fgen', models.CharField(default=0, max_length=200)),
                ('frelation', models.CharField(default=0, max_length=200)),
                ('mather', models.CharField(default=0, max_length=200)),
                ('mdob', models.DateField(default=0)),
                ('mage', models.CharField(default=0, max_length=200)),
                ('mgen', models.CharField(default=0, max_length=200)),
                ('mrelation', models.CharField(default=0, max_length=200)),
                ('cihldren1', models.CharField(default=0, max_length=200)),
                ('c1dob', models.DateField(default=0)),
                ('c1age', models.CharField(default=0, max_length=200)),
                ('c1gen', models.CharField(default=0, max_length=200)),
                ('c1relation', models.CharField(default=0, max_length=200)),
                ('children2', models.CharField(default=0, max_length=200)),
                ('c2dob', models.DateField(default=0)),
                ('c2age', models.CharField(default=0, max_length=200)),
                ('c2gen', models.CharField(default=0, max_length=200)),
                ('c2relation', models.CharField(default=0, max_length=200)),
                ('companyname', models.CharField(default=0, max_length=200)),
                ('durationfrom', models.DateField(default=0)),
                ('durationto', models.DateField(default=0)),
                ('joiningctc', models.CharField(default=0, max_length=200)),
                ('lctc', models.CharField(default=0, max_length=200)),
                ('twe', models.CharField(default=0, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appdate', models.DateField()),
                ('appname', models.CharField(max_length=250)),
                ('leavetype', models.CharField(max_length=250)),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('resumeon', models.DateField()),
                ('leaveday', models.CharField(max_length=50)),
                ('leavebalance', models.CharField(max_length=50)),
                ('leavereason', models.CharField(max_length=50)),
                ('empl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filturmapp.mainfilturm')),
            ],
        ),
    ]
