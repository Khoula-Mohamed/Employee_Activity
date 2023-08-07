class employee:
    def __init__(self,empid, empname, empsalary, empdep):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary
        self.empdep = empdep
        
    def get_id(self):
        return self.empid
    def get_name(self):
        return self.empname
    def get_salary(self):
        return self.empsalary
    def get_dep(self):
        return self.empdep
    
    def set_id(self,nid):
        self.empid = nid
    def set_name(self,nname):
        self.empname = nname
    def set_salary(self,nsalary):
        self.empsalary = nsalary
    def set_dep(self,ndep):
        self.empdep = ndep
        
    def cal_emp_salary(self):
        print("the employee salary is " +str(self.empsalary)+ " OMR")
        hour_work = int(input("Enter the number of hours worked by employee: "))
        if hour_work >= 50:
            overtime = hour_work - 50
            overtime_amount = (overtime * (self.empsalary/50))
            self.empsalary = self.empsalary + overtime_amount
        else :
            self.empsalary = self.empsalary
        return f'The new salary is {self.empsalary} OMR'
    
    def emp_assign_dep(self):
        nndep = input("Enter new department of " +self.empname+ ": ")
        self.empdep = nndep
        return f'The previous department is {self.empdep} and The new department is {nndep}'
    
    def emp_details(self):
        return f'Employee name is {self.empname} with id {self.empid} in {self.empdep} department , salary: {self.empsalary} OMR'
    