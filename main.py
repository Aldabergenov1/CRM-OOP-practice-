from datetime import datetime

class Company:

    def __init__(self, name:str, field:str, departments:list, 
                 director:str, adress:str, year_of_foundation:int, 
                 count_of_employes:int, budget:float) -> None:
        self.name = name
        self.field = field
        self.departments = departments
        self.director = director
        self.adress = adress
        self.year_of_foundation = year_of_foundation
        self.count_of_emplyes = count_of_employes
        self.__budget = budget  #инкапсуляция бюджета
    
    def return_main_info(self) -> tuple:
        return (self.name, self.field, self.departments, 
                self.director, self.year_of_foundation, 
                self.adress, self.count_of_emplyes)

    @classmethod   #создаю метод класса, который проверяет, является ли параметр числом
    def __budget_setter_validator(cls, x) -> bool:
        return type(x) in (float, int)

    def set_budet(self, budget) -> None:  #создаю сеттер для смены бюджета
        if self.__budget_setter_validator(budget):
            self.__budget = budget
        else:
            raise ValueError("Бюджет должен быть числом!")

    def get_budget(self):  #геттер для бюджета
        return self.__budget

class Department:
    
    MAX_WORKERS = 500

    def __init__(self, mission:str, number_of_workers:int) -> None:
        self.mission = mission
        self.number_of_workers = number_of_workers

    def add_workers(self, count):
        if self.number_of_workers + count <= self.MAX_WORKERS:  #проверка на максимум работников в департаменте
            self.number_of_workers += count
        else:
            raise ValueError("Достигнут максимум работников!")
        
    def show_info(self) -> tuple:
        return (self.mission, self.number_of_workers)

class Person:
    
    def __init__(self, name:str, surname:str, age:int, adress:str) -> None:
        self.name = name
        self.surname = surname
        self.year_of_birth = datetime.today().year - age  #computed свойство
        self.__adress = adress  #инкапсуляция адреса

    def get_adress(self):
        return self.__adress


class Salary:
    def __init__(self, payment:float) -> None:
        self.payment = payment

    def compute_total(self):
        return self.payment*12
    
    def __add__(self, other):  #перегразука оператора чтобы считать надбавку
        if isinstance(other, (int, float)):
            return Salary(self.payment + other)
        elif isinstance(other, Salary):
            return Salary(self.payment + other.payment)
        else:
            raise ValueError("Неизвестный тип!")

class Employee(Person):  #наследование от класса Person
    
    def __init__(self, name: str, surname: str, age: int, adress: str,
                 id_number:str, payment:float, crm_account_password:str) -> None:
        super().__init__(name, surname, age, adress)
        self.id_number = id_number
        self.payment = payment
        self.__annual_salary = Salary(self.payment)  #вычисляю годовую зарплату
        self.__crm_account_password = crm_account_password  #инкапсуляция пароля

    def compute_total_salary(self):
        return self.__annual_salary.compute_total() #композиция

    def show_main_info(self) -> tuple:
        return (self.name, self.surname, self.year_of_birth, self.id_number)

    def make_sucsessful_deal(self, cost) -> str:
        self.__annual_salary += cost*0.01
        return "Успешная сделка! + к премии!"  #премия за успешную сделку



#проверка класса Company
ITCom = Company('ITCom', 'IT', ['Marketing Department', 'IT-Department'], 
                'Mr. Aldabergenov', 'Panfilov 130', 2003, 180, 654_000)
print(f'Main info:\n{ITCom.return_main_info()}')
print(f'Текущий бюджет: {ITCom.get_budget()}')
ITCom.set_budet(999_999)
print(f'Бюджет после смены: {ITCom.get_budget()}')


#проверка класса Employee(соотвественно, и Person, и Salary)
David = Employee('David', 'Mamedov', 21, 'Tole Bi 150', '22BD001819', 320_000, 'password123')
print(David.compute_total_salary())
print(David.show_main_info())
print(David.get_adress())
David.make_sucsessful_deal(12000)
print(David.compute_total_salary())

#проверка класса Department
IT_Department = Department("Обеспечить правильную работу всех технических сервисов компании", 120)
print(IT_Department.show_info())
IT_Department.add_workers(200)
print(IT_Department.show_info())
