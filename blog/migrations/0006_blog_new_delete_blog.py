# Generated by Django 4.1 on 2022-08-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blog_data_blog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog_New",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("data_blog", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="Blog",),
    ]
