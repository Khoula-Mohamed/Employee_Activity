from ex1class import employee
def main():
    emp1 = employee("E7876","Adams",5000,"Accounting")
    emp2 = employee("E7499","Jons",45000,"Research")
    emp3 = employee("E7900","Martin",5000,"Sales")
    
    print(emp1.emp_details())
    
    print(emp1.emp_assign_dep())
    print(emp1.emp_details())
    
    print(emp1.cal_emp_salary())
    print(emp1.emp_details())

    

main()