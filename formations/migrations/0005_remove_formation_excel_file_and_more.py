# Generated by Django 4.2.1 on 2023-05-30 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0004_alter_formation_excel_file_alter_formation_pdf_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='excel_file',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='word_file',
        ),
    ]