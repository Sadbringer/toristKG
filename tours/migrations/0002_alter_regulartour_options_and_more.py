# Generated by Django 4.0.3 on 2022-04-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regulartour',
            options={'ordering': ['-start'], 'verbose_name': 'Регулярный тур', 'verbose_name_plural': 'Регулярные туры'},
        ),
        migrations.RenameField(
            model_name='regulartour',
            old_name='start_datetime',
            new_name='start',
        ),
    ]
