"""
Anthony Nguyen
CS1400
Fluffle Shuffle electronics
11/28/2017

Project help from
	Cory in Class

You are creating part of the payroll program for an Internet electronics store named "FluffShuffle Electronics".
The owner of FluffShuffle has given you the following requirements: FluffShuffle employs six (6) people.
The owner doesn't expect significant growth in his company, but to be on the safe side he would like the program to handle a few more employees.

All of the employee data (name, address, etc.) is kept in a text file on your disk.
Your program will read this employee data from the file and use that data to calculate the payroll for company employees.
The program will have to calculate the payroll deductions for each employee and their net pay.


An Employee has the following attributes:

    -employee number
    -name
    -street address
    -hourly wage
    -hours worked this week
an employee object will need the following methods:

    -A constructor for the employee class that takes arguments to initialize all of the above mentioned attributes.
    
    -A method, calcSalary(), that calculates and returns an employee's net pay as a float. 
        An employee's gross pay is calculated by multiplying the hours worked by their hourly wage.
        Be sure to give time-and-a-half for overtime (anything over 40 hours). 
        To compute the net pay, deduct 20% for Federal income tax, and 7.5% for state income tax.

Every employee on the payroll will need to be represented in the program by its own employee object.
A convenient way to handle this will be to create a list of employee objects.


"""

from graphics import *
from button import *


#create a class for eployee data with all the paramters from
#the .txt file in the directory
class EmpData:
    def __init__(self, empNum, name, address, wage, hoursWorked):
        # takes at the paramters from empdata.txt, (self, empNum, name, address, wage, hoursWorked) and creates a class names EmpData
        self.empNum = empNum
        self.name = name
        self.address = address
        self.wage = wage
        self.hoursWorked = hoursWorked

    #calculate the net salary of the employee
        
    def calcSalary(self):
        # takes paramters from the class empData (wage, hoursWorked), and passes them into a function designed to
        # calculate the salary - taxes at 20% and 7.5% and returns net salary rounded to 2 decimal places
        
        #if statement to catch overtime and calculate overtime
        #if not calculate the normal hours at the normal rate
        if self.hoursWorked > 40:
            overtime = (self.hoursWorked - 40)
            grossSalary = (overtime * (self.wage *1.5)) + (40 * self.wage)
        else:
            grossSalary = (self.hoursWorked * self.wage)
        netSalary = grossSalary - (grossSalary * .2) - (grossSalary * .075)

        #return net salary rounded to 2 decimal places
        return '${:,.2f}'.format(netSalary)

def main():
    # takes all info from class emp data and the function cal_salary and creates an object employee for each employee in the
    #txt file and uses that employee in the GUI to display the pertinemnt information

    #open the file from the directory
    fileData = open("empdata.txt", "r")

    #create  a list of all emplyees
    empList = []
    
    
    #run a try catch in order to iterate trough the list and gather all
    #information in order to create the employee object
    while True:
        try:
            empNum = int(fileData.readline())
            name = fileData.readline()[:-1]
            address = fileData.readline()[:-1]
            wage = float(fileData.readline())
            hoursWorked = float(fileData.readline()[:-1])
            
            
            #make an eployee object
            employee = EmpData(empNum, name, address, wage, hoursWorked)
            
            #add new employee to the new list of employees amde
            empList.append(employee)

        except ValueError:
            break


    #create GUI
    #draw window
    win = GraphWin("Employee Data", 700, 700)
    
    #GUI displays the information from the .txt file listed the empdata class earlier
    #Also houses a button used to iterate through the list and deactivate when there are no more employees
    #Left to use
    #Draw text and text boxes each being about 50 below the other one
    

    Text(Point(140,50), "Employee Number:").draw(win).setSize(24)
    entryEmpnum = Entry(Point(400, 50), 20 )
    entryEmpnum.draw(win).setFill("white")
    entryEmpnum.setText(empList[0].empNum)
    
    Text(Point(115,100), "Employee Name").draw(win).setSize(24)
    entryName = Entry(Point(400, 100), 20 )
    entryName.draw(win).setFill("white")
    entryName.setText(empList[0].name)
                                                                                         
    Text(Point(110,150), "Address:").draw(win).setSize(24)
    entryAddress = Entry(Point(400, 150), 20 )
    entryAddress.draw(win).setFill("white")
    entryAddress.setText(empList[0].address)
    
    Text(Point(120,200), "Hourly Wage:").draw(win).setSize(24)
    entryWage = Entry(Point(400, 200), 20 )
    entryWage.draw(win).setFill("white")
    entryWage.setText(empList[0].wage)

    Text(Point(120,250), "Hours Worked:").draw(win).setSize(24)
    entryHoursworked = Entry(Point(400, 250), 20 )
    entryHoursworked.draw(win).setFill("white")
    entryHoursworked.setText(empList[0].hoursWorked)

    Text(Point(120,300), "Net Salary:").draw(win).setSize(24)
    entryNetsalary = Entry(Point(400, 300), 20 )
    entryNetsalary.draw(win).setFill("white")
    entryNetsalary.setText(empList[0].calcSalary())
    
    #create a button

    button = Button(win, Point(250, 350), 110, 30,"Next Employee")
    button.activate()

    #run a try catch in order to have the nutton iterate through the list and
    #deactivate at the end of the list

    index = 0
    while True:
        try:       
            if button.clicked(win.getMouse()) == True:
                if index < len(empList) -1 :
                    index = index + 1
                    entryEmpnum.setText(empList[index].empNum)
                    entryName.setText(empList[index].name)
                    entryAddress.setText(empList[index].address)
                    entryWage.setText(empList[index].wage)
                    entryHoursworked.setText(empList[index].hoursWorked)
                    entryNetsalary.setText(empList[index].calcSalary())
                else:
                    button.deactivate()
        except:
            break
      
            

    fileData.close
    print("It worked!")

        

main()
