# Generated by Django 4.2 on 2024-10-04 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'default_related_name': 'employees', 'ordering': ('last_name', 'first_name'), 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('name',), 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name',), 'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AddField(
            model_name='employee',
            name='grade',
            field=models.CharField(choices=[('Junior', 'Джуниор'), ('Middle', 'Мидл'), ('Senior', 'Сеньор'), ('Intern', 'Cтажер'), ('Lead', 'Ведущий специалист'), ('Head', 'Руководитель')], default='Junior', max_length=6, verbose_name='Грейд сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.team', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название должности'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название команды'),
        ),
    ]
