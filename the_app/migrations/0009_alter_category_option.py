# Generated by Django 4.1.2 on 2022-10-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0008_alter_category_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='option',
            field=models.CharField(choices=[('S', 'STORY'), ('V', 'VENT'), ('C', 'CONFESSION'), ('I', 'IDEA'), ('A', 'ADVICE'), ('O', 'OPINION'), ('W', 'CREATIVE WRITING'), ('F', 'FUN FACT')], max_length=8),
        ),
    ]
