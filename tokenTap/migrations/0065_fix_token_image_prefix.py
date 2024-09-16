# Generated by Django 4.0.4 on 2024-08-25 09:12

from django.db import migrations, models


def fix_token_images_prefix(apps, schema_editor):
    TokenDistribution = apps.get_model("tokenTap", "TokenDistribution")

    tokens = TokenDistribution.objects.all()

    for token in tokens:
        if (
            token.image
            and token.image.name
            and token.image.name.startswith("https://imagedelivery.net")
        ):
            # split the url to get the image id
            token.image.name = token.image.name.split("/")[-2]
            token.save()

        if (
            token.token_image
            and token.token_image.name
            and token.token_image.name.startswith("https://imagedelivery.net")
        ):
            token.token_image.name = token.token_image.name.split("/")[-2]
            token.save()


class Migration(migrations.Migration):

    dependencies = [
        ("tokenTap", "0064_alter_constraint_name"),
    ]

    operations = [
        migrations.RunPython(
            fix_token_images_prefix, reverse_code=migrations.RunPython.noop
        )
    ]