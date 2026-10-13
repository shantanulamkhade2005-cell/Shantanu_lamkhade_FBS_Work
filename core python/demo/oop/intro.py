class Employee:
    def __init__(self):
        print('I am in employee',id(self))
        def display():
            print('I am for display of employee')
e1=Employee()
e2=Employee()
print(f"ide1={id(e1)}")
print(f"ide2={id(e2)}")