# Generated by Django 3.2.5 on 2021-07-20 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GptInputOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userInput', models.TextField(db_column='userInput')),
                ('trainedInput', models.TextField(db_column='fullRequestInput')),
                ('gptOutput', models.TextField(db_column='gptOutput')),
                ('requestDateTime', models.DateTimeField(db_column='requestDateTime')),
            ],
            options={
                'db_table': 'GptInputOutput',
            },
        ),
        migrations.CreateModel(
            name='TrainingCorpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemaText', models.TextField()),
                ('inputText', models.TextField()),
                ('outputText', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.TextField()),
                ('password', models.TextField()),
                ('dateAccountCreated', models.DateField(db_column='dateAccountCreated')),
                ('loginStatus', models.IntegerField(blank=True, db_column='loginStatus', null=True)),
            ],
            options={
                'db_table': 'UserLogin',
            },
        ),
        migrations.CreateModel(
            name='UserDatabaseEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbName', models.TextField(verbose_name='dbName')),
                ('tableColumn', models.IntegerField()),
                ('dataType', models.TextField(db_column='dataType')),
                ('localGroupingKey', models.IntegerField(db_column='localGroupingKey')),
                ('elementName', models.CharField(max_length=50)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.userlogin')),
            ],
            options={
                'db_table': 'UserDatabaseEntity',
            },
        ),
        migrations.CreateModel(
            name='UserDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbName', models.CharField(max_length=50)),
                ('schemaString', models.TextField(db_column='schemaString')),
                ('dateTimeCreated', models.DateTimeField(db_column='dateTimeCreated')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.userlogin')),
            ],
            options={
                'db_table': 'UserDatabase',
            },
        ),
    ]
