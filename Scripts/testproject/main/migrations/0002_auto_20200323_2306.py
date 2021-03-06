# Generated by Django 3.0.4 on 2020-03-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='form_education',
            options={'verbose_name': 'Форма обучения', 'verbose_name_plural': 'Формы обучения'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Штатное расписание', 'verbose_name_plural': 'Штатные расписания'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Юридический адрес/Для ИП адрес регистрации'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='address_fact',
            field=models.CharField(max_length=100, verbose_name='Фактический адрес'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='address_postal',
            field=models.CharField(max_length=100, verbose_name='Почтовый адрес'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='begin_date',
            field=models.CharField(max_length=10, verbose_name='Дата, с которой осуществляется подготовка документов'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_status',
            field=models.CharField(max_length=50, verbose_name='Статус клиента (согласно выбранному тарифу)'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_name',
            field=models.CharField(max_length=50, verbose_name='ФИО контактного лица'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_phone',
            field=models.CharField(max_length=11, verbose_name='Телефон контактного лица'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contract_date',
            field=models.CharField(max_length=10, verbose_name='Дата заключения договора'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Адрес эл. почты'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='Полное наименование организации/ФИО ИП'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='kpp',
            field=models.CharField(max_length=9, null=True, verbose_name='КПП/Для ИП пусто'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='ogrn',
            field=models.CharField(max_length=15, verbose_name='ОГРН/ОГРНИП'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='okved2',
            field=models.CharField(max_length=50, verbose_name='ОКВЭД2 список'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='opf',
            field=models.CharField(max_length=5, verbose_name='Форма собственности по ОПФ'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Телефон организации'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='short_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Краткое наименование организации/Для ИП пусто'),
        ),
    ]
