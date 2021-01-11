class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def get_name(self):
    return self.name

  def set_name(self, name):
      return self.name

  def get_salary(self):
    return self.salary

  def set_salary(self, salary):
    if salary > 0:
      return self.salary

  def display(self):
    return ("Name: " + self.name + "\n" + 
    "Salary: " + str(self.salary))

employee1 = Employee("enis", 0.25)
print(employee1.display())

class Company:
  def __init__(self):
    self.employee_list = []

  def get_employee_list(self):
    return self.employee_list
  
  def set_employee_list(self, employee list):
    if type(employee_list) == list:
      self.employee_list.append(new_employee)

  def calc_ave_salary(self):
    sum = 0
    for emp in self.employee_list:
      sum += emp.get_salary()
    return sum/len(self.get_employee_list

  def display(self):
    for emp in self.employee_list:
      emp.display()

