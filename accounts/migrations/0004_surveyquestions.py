# Generated by Django 4.2.9 on 2024-04-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_donation_donor_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='surveyquestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('question', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-created_on'],
                'abstract': False,
            },
        ),
    ]