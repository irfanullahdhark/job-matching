# Generated by Django 4.1.2 on 2022-12-24 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_registrationno', models.IntegerField(primary_key=True, serialize=False)),
                ('company_password', models.CharField(max_length=30, unique=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=20)),
                ('company_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Db_admin',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='postajob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=120)),
                ('job_vacancynum', models.CharField(max_length=100)),
                ('job_emailaddress', models.EmailField(max_length=254)),
                ('job_startingdate', models.DateField()),
                ('job_endingdate', models.DateField()),
                ('job_experience', models.CharField(max_length=30)),
                ('job_duration', models.CharField(max_length=100)),
                ('job_salary', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=15)),
                ('job_noofoppurtunity', models.IntegerField()),
                ('job_location', models.CharField(max_length=30)),
                ('job_communicationskills', models.CharField(max_length=40)),
                ('job_degree', models.CharField(max_length=30, null=True)),
                ('job_field', models.CharField(max_length=40, null=True)),
                ('job_seconddegree', models.CharField(max_length=30, null=True)),
                ('job_secondfield', models.CharField(max_length=40, null=True)),
                ('job_gender', models.CharField(max_length=10)),
                ('job_educationalskillfirst', models.CharField(max_length=100, null=True)),
                ('job_educationalskillsecond', models.CharField(max_length=100, null=True)),
                ('job_educationalskillthird', models.CharField(max_length=100, null=True)),
                ('job_educationalskillfourth', models.CharField(max_length=100, null=True)),
                ('job_computerskillfirst', models.CharField(max_length=100, null=True)),
                ('job_computerskillsecond', models.CharField(max_length=100, null=True)),
                ('job_computerskillthird', models.CharField(max_length=100, null=True)),
                ('job_firstlanguage', models.CharField(max_length=100, null=True)),
                ('job_firstknowpercentage', models.IntegerField(null=True)),
                ('job_secondlanguage', models.CharField(max_length=100, null=True)),
                ('job_secondknowpercentage', models.IntegerField(null=True)),
                ('job_thirdlanguage', models.CharField(max_length=100, null=True)),
                ('job_thirdknowpercentage', models.IntegerField(null=True)),
                ('job_descriptoin', models.TextField(null=True)),
                ('job_responsibilities', models.TextField(null=True)),
                ('related_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtables.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='admin_user_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='dbtables.db_admin'),
        ),
        migrations.CreateModel(
            name='Applier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applierusername', models.CharField(max_length=30)),
                ('applieremail', models.EmailField(max_length=254)),
                ('applierphoneno', models.IntegerField(null=True)),
                ('applieridentityno', models.IntegerField()),
                ('applierdateofbirth', models.DateField()),
                ('appliergender', models.CharField(max_length=10)),
                ('applierorignlocation', models.CharField(max_length=30)),
                ('appliercurrentlocation', models.CharField(max_length=30)),
                ('applierdegree', models.CharField(max_length=30)),
                ('applierfield', models.CharField(max_length=40)),
                ('applierseconddegree', models.CharField(max_length=30, null=True)),
                ('appliersecondfield', models.CharField(max_length=40, null=True)),
                ('appliercommunicationskills', models.CharField(max_length=40)),
                ('applierexperience', models.CharField(max_length=30)),
                ('appliereducationalskillfirst', models.CharField(max_length=100, null=True)),
                ('appliereducationalskillsecond', models.CharField(max_length=100, null=True)),
                ('appliereducationalskillthird', models.CharField(max_length=100, null=True)),
                ('appliereducationalskillfourth', models.CharField(max_length=100, null=True)),
                ('appliercomputerskillfirst', models.CharField(max_length=100, null=True)),
                ('appliercomputerskillsecond', models.CharField(max_length=100, null=True)),
                ('appliercomputerskillthird', models.CharField(max_length=100, null=True)),
                ('applierfirstlanguage', models.CharField(max_length=100, null=True)),
                ('applierfirstknowpercentage', models.IntegerField(null=True)),
                ('appliersecondlanguage', models.CharField(max_length=100, null=True)),
                ('appliersecondknowpercentage', models.IntegerField(null=True)),
                ('applierthirdlanguage', models.CharField(max_length=100, null=True)),
                ('applierthirdknowpercentage', models.IntegerField(null=True)),
                ('aplirdescription', models.TextField(null=True)),
                ('Job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtables.postajob')),
            ],
        ),
    ]