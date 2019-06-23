'''УСЛОВИЕ:
Реализовать класс Person, который отображает запись в книге контактов.
Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)
Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.
Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;
Примечание:
1) смотрите документацию по модулю datetime;
2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
- определить какая информация нужна для создания объекта datetime.date,
- получить эти данные из строки - разобрать ее (достать из нее отдельно,
год, месяц, число),
- на основании этой информации создать специальный объект datetime.date,
- поместить этот спец.объект в атрибут экземпляра класса'''

from datetime import datetime, timedelta

class Person:
    def __init__(self, surname, first_name, nickname, birth_date):
        self.surname = str(surname)
        self.first_name = str(first_name)
        self.nickname = str(nickname)
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        currentdate = datetime.date(datetime.today())
        currentyear = currentdate.year
        if currentdate.day <= self.birth_date.day and currentdate.month <= self.birth_date.month:
            return int(currentyear) - int(self.birth_date.year) - 1
        else:
            return int(currentyear) - int(self.birth_date.year)

    def get_fullname(self):
        fullname = self.first_name + ' ' + self.surname
        return fullname.upper()

    def get_fullage(self):
        print('родился ', self.birth_date.day, ' числа ', self.birth_date.month, ' месяца ', self.birth_date.year, ' года. Полных лет', self.get_age(), '\n')

a = Person("Morev", "Oleksii", "averom", "1980-10-20")
b = Person("Иванов", "Иван", "iivan", "2006-04-15")
c = Person("Сидоров", "Сидор", "123@domain.com", "1997-07-27")
print('Книга контактов:')
print('------------------------------------------------------')
print('1   | ', a.surname, ' | ', a.first_name, ' | ', a.nickname, ' | ', datetime.strftime(a.birth_date, "%d/%m/%Y"))
print('2   | ', b.surname, ' | ', b.first_name, ' | ', b.nickname, ' | ', datetime.strftime(b.birth_date, "%d/%m/%Y"))
print('3   | ', c.surname, ' | ', c.first_name, ' | ', c.nickname, ' | ', datetime.strftime(c.birth_date, "%d/%m/%Y"))
print('------------------------------------------------------')
print(a.get_fullname())
a.get_fullage()
print(b.get_fullname())
b.get_fullage()
print(c.get_fullname())
c.get_fullage()