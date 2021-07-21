class Employee:
    def __init__(self, years_of_experience, position, name):
        self.years_of_experience = years_of_experience
        self.position = position
        self.name = name


    def calculate_salary(self):
        base = 2500
        salary = None
        if(0 <= self.years_of_experience <= 2):
            salary = base + 1500
        elif(2 <= self.years_of_experience <= 5):
            salary = base + 2500
        elif(self.years_of_experience > 5):
            salary = base + 3500
        else:
            print('years of experience must be 0 or positive number')
        return salary

    def calculate_bonus(self, total_salary):
        salary_bonus = None

        if(self.position == 'front-end'):
            salary_bonus = total_salary * 1.1

        if(self.years_of_experience > 2):
            salary_bonus = total_salary * 1.2

        print('the salary+bonus of the position %s is: %s' % (self.position , salary_bonus))

class Programmer(Employee):

    def __init__(self,years_of_experience, position, name):
        super().__init__(years_of_experience, position, name)
        self.years_of_experience = years_of_experience
        self.position = position
        self.name = name

    def print_data(self):
        print('the employer %s works as %s' % (self.name, self.position))



junior_developer = Programmer(0, 'front-end','Ahmad')
junior_developer.calculate_bonus(junior_developer.calculate_salary())
junior_developer.print_data()

print("\n")

senior_developer = Programmer(7,'app developer', 'Omar')
senior_developer.calculate_bonus(senior_developer.calculate_salary())
senior_developer.print_data()
