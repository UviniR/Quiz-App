# Generated by Django 4.1.2 on 2022-10-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Quiz", "0021_delete_teacher_alter_result_student"),
        ("student", "0006_remove_student_id_alter_student_email"),
    ]

    operations = [
        migrations.DeleteModel(name="Student",),
    ]
