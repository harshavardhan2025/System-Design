class Employee:
    company = "TechCorp Solutions"
    total_employees = 0
    pf_percentage = 12.0
    MIN_SALARY = 15000
    MAX_SALARY = 500000

    def __init__(self,emp_id,name, department, salary, pan_number):
        self.name = name
        self._emp_id = emp_id
        self._department = department

        if(self.valid_salary(salary)):
            self.salary = salary
        else:
            raise ValueError("INVALID_SALARY")

        self.__pan_number = pan_number

        Employee.total_employees += 1
    
    def valid_salary(self, salary):
        if Employee.MIN_SALARY <= salary <= Employee.MAX_SALARY:
            return True
        else:
            return False


    @property
    def salary(self):
        return self._salary

    @property
    def emp_id(self):
        return self._emp_id

    
    @salary.setter
    def salary(self,salary):
        if(self.valid_salary(salary)):
            self._salary = salary
        else:
            raise ValueError("INValid Salary")

    @property
    def department(self):
       return self._department

    def transfer_depertment(self,new_dep):
        self._department = new_dep
        
    @property
    def pan_number(self):
        return self.__pan_number
    
    def apply_hike(self,percent):
        if(not (percent>=1 and percent <= 50)):
            raise ValueError("Hike should be done between 0 to 50 %")
        else:
            hiked = (self.salary * percent) // 100
            self.salary = (self.salary + hiked)
        


    def calculate_pf(self):
      return (self.salary * Employee.pf_percentage ) / 100

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    @staticmethod
    def is_valid_salary(amount):
        if(amount>=Employee.MIN_SALARY and amount<=Employee.MAX_SALARY):
          print("Valid")
        else:
            print("Not Valid")
        
          





e1 = Employee(1, "harsha", "Product", 50000, "DAUP6605E")
e2 = Employee(2,"mahith", "Develpoer", 70000, "DPAP5640F")