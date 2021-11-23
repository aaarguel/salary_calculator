from datetime import datetime, timedelta
#Constants

#First Interval
fInterval1 = datetime.strptime("01/01/21 00:00", '%d/%m/%y %H:%M')
fInterval2 = datetime.strptime("01/01/21 09:00",'%d/%m/%y %H:%M')
#Second Interval
sInterval1 = datetime.strptime("01/01/21 09:00", '%d/%m/%y %H:%M')
sInterval2 = datetime.strptime("01/01/21 18:00",'%d/%m/%y %H:%M')
#Third Interval
#tInterval1 = datetime.strptime("01/01/21 18:00", '%d/%m/%y %H:%M')
#tInterval2 = datetime.strptime("01/01/21 23:59",'%d/%m/%y %H:%M')

dic_employess = {}
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class FormatError(Exception):
    pass

def uploadEmployees(filetxt):
    """
    uploadEmployees is responsible for reading the txt line by line, validating if it meets the conditions.

    :param filetxt: name of file  
    :return: a bool if the process completed successfully
    """ 
    try:
        
        with open(filetxt, "r") as file:
            lines = file.readlines()
            count = 1
            for line in lines:
                line=line.strip("\n")
                if line.find("=") != -1:
                    generalData = line.split("=")
                    dic_employess[generalData[0]]={"salary": 0, "worked_days": [] }
                    if generalData[1].find(",") != -1:
                        daysHoursWorked=generalData[1].split(",")
                        for daysHours in daysHoursWorked:
                            calculateSalary(generalData[0],daysHours[:2],daysHours[2:])
                            
                    else:
                        raise FormatError("In line " + str(count)+ ": Character not found ',', check the format")
                else:
                    raise FormatError("In line " + str(count)+ ": Character not found '=', check the format")
                count+=1
            #print(dic_employess)
            print(colors.OKBLUE +"\nThe data of " +colors.BOLD + str(count-1)+ colors.ENDC+ colors.OKBLUE + " employees was uploaded"+ colors.ENDC)
            print(colors.OKGREEN +"Successfully completed\n\n\n\n\n"+ colors.ENDC)
            return True
    except FileNotFoundError:
        print(colors.FAIL +"\nOpps! This file doesn't exists. Please, try again"+ colors.ENDC)
        dic_employess.clear()
        return False
    except FormatError as e:             
        print(colors.WARNING + str(e) + colors.ENDC)
        print(colors.OKCYAN + "Example format: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00" + colors.ENDC)  
        dic_employess.clear()
        return False 
    except Exception as e:        
        print(colors.FAIL + str(e) + colors.ENDC)
        dic_employess.clear()
        return False


def calculateSalary(name,day,hoursInterval,saveData=True):
    """
    calculateSalary is responsible for calculating the salary of an employee in one day.

    :param name: name of employee 
    :param day: day to calculate   
    :param hoursInterval: interval of hours worked 
    :param saveData: saves the employee's data, if false, returns the employee's salary
    :return: salary of employee
    """ 
    salary=0
    weekend = isWeekend(day)
    hours = hoursInterval.split("-")
    #interval Worked
    fromHour = datetime.strptime("01/01/21 "+hours[0], '%d/%m/%y %H:%M')
    toHour = datetime.strptime("01/01/21 "+hours[1], '%d/%m/%y %H:%M')

    list_hours = [fromHour]
    from_hour = fromHour
    #Obtain list of hours in interval
    while from_hour < toHour:
        from_hour += timedelta(hours=1)
        list_hours.append(from_hour)
    list_hours.pop(0)
    
    for hour in list_hours:
        if fInterval1 <= hour <= fInterval2:
            if weekend:
                if saveData:
                    dic_employess[name]["salary"] += 30
                else:
                    salary+= 30                              
            else:
                if saveData:
                    dic_employess[name]["salary"] += 25
                else:
                    salary+= 25  
                          
        elif sInterval1 <= hour <= sInterval2:
            if weekend:
                if saveData:
                    dic_employess[name]["salary"] += 20
                else:
                    salary+= 20                             
            else:
                if saveData:
                    dic_employess[name]["salary"] += 15
                else:
                    salary+= 15                             
        else:
            if weekend:
                if saveData:
                    dic_employess[name]["salary"] += 25
                else:
                    salary+= 25
                                   
            else:
                if saveData:
                    dic_employess[name]["salary"] += 20
                else:
                    salary+= 20
                                
    if saveData:
        dic_employess[name]["worked_days"].append(day)
    else:
        return salary

def isWeekend(day):
    """
    isWeekend valid if it's weekend    
    :param day: day to calculate       
    :return: true it's a weekend, otherwise false 
    """ 
    if day in ["SA","SU"]:
        return True
    else:
        return False


def getSalary(name):
    """
    getSalary get an employee's salary
    :param name: name of employee      
    :return: salary
    """ 
    if name in dic_employess:
        return dic_employess[name]["salary"]
    else:
        raise Exception("Employee does not exist in uploaded file")

def getWorkedDays(name):
    """
    getWorkedDays get the days worked of an employee
    :param name: name of employee      
    :return: worked days
    """ 
    if name in dic_employess:
        return dic_employess[name]["worked_days"]
    else:
        raise Exception("Employee does not exist in uploaded file")
    