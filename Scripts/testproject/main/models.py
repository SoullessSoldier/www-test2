from django.db import models

# Create your models here.

class Clients(models.Model):
    full_name=models.CharField(max_length=100,verbose_name='Полное наименование организации/ФИО ИП')
    short_name=models.CharField(max_length=100,null=True,verbose_name='Краткое наименование организации/Для ИП пусто')
    opf=models.CharField(max_length=5, verbose_name='Форма собственности по ОПФ')
    inn=models.CharField(max_length=12, verbose_name='ИНН')
    ogrn=models.CharField(max_length=15, verbose_name='ОГРН/ОГРНИП')
    kpp=models.CharField(max_length=9,null=True, verbose_name='КПП/Для ИП пусто')
    address=models.CharField(max_length=100, verbose_name='Юридический адрес/Для ИП адрес регистрации')
    address_postal=models.CharField(max_length=100, verbose_name='Почтовый адрес')
    address_fact=models.CharField(max_length=100, verbose_name='Фактический адрес')
    phone=models.CharField(max_length=11, verbose_name='Телефон организации')
    email=models.CharField(max_length=50, verbose_name='Адрес эл. почты')
    contact_name=models.CharField(max_length=50, verbose_name='ФИО контактного лица')
    contact_phone=models.CharField(max_length=11, verbose_name='Телефон контактного лица')
    okved2=models.CharField(max_length=50, verbose_name='ОКВЭД2 список')
    contract_date=models.CharField(max_length=10, verbose_name='Дата заключения договора')#Date in YYYY-MM-DD
    begin_date=models.CharField(max_length=10, verbose_name='Дата, с которой осуществляется подготовка документов')#Date in YYYY-MM-DD
    client_status=models.CharField(max_length=50, verbose_name='Статус клиента (согласно выбранному тарифу)')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'

class Form_education(models.Model):
    
    form_name=models.CharField(max_length=50,verbose_name='Форма обучения')#"целевой   инструктаж"/"повышение уровня знаний", "вводный/дополнительный инструктаж"
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Форма обучения'
        verbose_name_plural='Формы обучения'
    
#res = Staff.objects.latest()
#res.client.inn    
#{{ object.client.name }}
class Staff(models.Model):
    client_inn=models.ForeignKey(Clients,null=True,on_delete=models.PROTECT, verbose_name='Клиент ИНН')
    position_1=models.CharField(max_length=50, verbose_name='Должность в именит.падеже')#Должность в именит.падеже
    position_2=models.CharField(max_length=50,verbose_name='Должность в родит.падеже')#Должность в родит.падеже
    position_3=models.CharField(max_length=50,verbose_name='Должность в дат.падеже')#Должность в дат.падеже
    position_4=models.CharField(max_length=50,verbose_name='Должность в винит.падеже')#Должность в винит.падеже
    position_5=models.CharField(max_length=50,verbose_name='Должность в творит.падеже')#Должность в творит.падеже
    date_approve=models.CharField(max_length=10,verbose_name='Дата утверждения')#Дата утверждения Date in YYYY-MM-DD
    date_exclusion=models.CharField(max_length=10, verbose_name='Дата исключения')#Дата исключения Date in YYYY-MM-DD
    form_education=models.ForeignKey(Form_education,null=True,on_delete=models.PROTECT, verbose_name='Форма обучения')
    staff_special=models.CharField(max_length=1, verbose_name='Признак специального должностного лица')#Признак   специального должностного лица
    staff_special_order_date=models.CharField(max_length=10,verbose_name='Дата приказа о назначении специального должностного лица')
    staff_special_order_number=models.CharField(max_length=10,verbose_name='Номер приказа о назначении специального должностного лица')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Штатное расписание'
        verbose_name_plural='Штатные расписания'


class Employee(models.Model):
    staff_name=models.ForeignKey(Staff,null=True,on_delete=models.PROTECT)
    fio1=models.CharField(max_length=100, verbose_name='ФИО в именит падеже')
    fio2=models.CharField(max_length=100, verbose_name='ФИО в родит падеже')
    fio3=models.CharField(max_length=100, verbose_name='ФИО в дат падеже')
    fio4=models.CharField(max_length=100, verbose_name='ФИО в винит падеже')
    fio5=models.CharField(max_length=100, verbose_name='ФИО в творит падеже')
    date_hiring=models.CharField(max_length=10, verbose_name='Дата приема на работу')
    date_firing=models.CharField(max_length=10, verbose_name='Дата увольнения')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'    
     