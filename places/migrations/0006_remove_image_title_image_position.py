# Generated by Django 4.1.3 on 2022-11-26 19:27

from django.db import migrations, models

def add_position(apps, schema_editor):
    Image = apps.get_model('places', 'Image')
    for image in Image.objects.iterator():
        image.position = image.title
        image.save()



def rollback(apps, schema_editor):
    Image = apps.get_model('places', 'Image')
    for image in Image.objects.iterator():
        image.title = image.position
        image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_place_details_url_image_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RunPython(add_position, rollback),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),

    ]