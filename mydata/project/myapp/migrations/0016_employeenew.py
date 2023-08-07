# Generated by Django 4.1.4 on 2023-02-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_alter_employee_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeNew",
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
                ("eid", models.CharField(max_length=20)),
                ("ename", models.CharField(max_length=100)),
                ("eemail", models.EmailField(max_length=254)),
                ("econtact", models.CharField(max_length=15)),
            ],
            options={"db_table": "myapp",},
        ),
    ]
