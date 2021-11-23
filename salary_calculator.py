import modules.ioet_test as ioet


def mainMenu(menu=False):
    print("""\
  _            _     _            _   
 (_)          | |   | |          | |  
  _  ___   ___| |_  | |_ ___  ___| |_ 
 | |/ _ \ / _ \ __| | __/ _ \/ __| __|
 | | (_) |  __/ |_  | ||  __/\__ \ |_ 
 |_|\___/ \___|\__|  \__\___||___/\__|
                                                                      
                    """)
    if menu:
        print("Main menu \n1. Get the salary of a employee registered in the txt\n2. Get days worked of a employee registered in the txt\n3. Insert a salary line format to calculate salary\n4. Exit")
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            opt = int(input("Enter an option: "))
            if opt == 1:
                name = input("Input the name of the employee: ")
                print("\nThe amount to pay "+name+" is: "+str(ioet.getSalary(name))+" USD\n")
                mainMenu(True)
            elif opt == 2:
                name = input("Input the name of the employee: ")
                print("\nThe days worked is: "+str(ioet.getWorkedDays(name))+"\n")
                mainMenu(True)
            elif opt == 3:
                line = input("Input line of data of employee: ").strip("\n")
                
                if line.find("=") != -1:
                    generalData = line.split("=")
                    if generalData[1].find(",") != -1:
                        daysHoursWorked=generalData[1].split(",")
                        salary=0
                        for daysHours in daysHoursWorked:
                            salary += ioet.calculateSalary(generalData[0],daysHours[:2],daysHours[2:],False)
                        print("\nThe amount to pay "+generalData[0]+" is: "+str(salary)+" USD\n")
                        
                    else:
                        raise ioet.FormatError("Character not found ',', check the format")
                else:
                    raise ioet.FormatError("Character not found '=', check the format")
                mainMenu(True)
            elif opt == 4:
                print("\n\n\nGoodbye!\n\n\n")
                
                
        except ValueError:
            print("\nSorry, I didn't understand that.\n")
            mainMenu(True)
        except Exception as e:
            print("\n"+str(e)+"\n")
            mainMenu(True)
    else:
        file= input("Write the file to analyze: ")
        uploadCorrect = ioet.uploadEmployees(file)
        mainMenu(uploadCorrect)


mainMenu()


