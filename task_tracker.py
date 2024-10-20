from task import Task
import datetime

class Main(Task):
    Task.load()
    print("------------------------------")
    print("WELCOME TO THE TASK TRACKER")
    print("------------------------------")
    while True:
        print("PLEASE CHOOSE YOUR TRANSACTION")
        print("------------------------------")
        print("1 - ADDING TASK")
        print("2 - CHANGE TASK STATUS")
        print("3 - REMOVE TASK")
        print("4 - GET ACTIVE TASK")
        print("5 - GET INACTIVE TASK")
        print("6 - LIST ACTIVE TASKS IN THE DATE RANGE")
        print("7 - LIST INACTIVE TASKS IN THE DATE RANGE")
        print("8 - UPDATE TASK")
        print("9 - LIST ALL TASK")
        print("10 - EXIT TASK TRACKER")
        print("------------------------------")
        choose = input(" YOUR CHOOSE : ")
        print("------------------------------")

        if choose == "1":
            desc = input("PLEASE ENTER THE TASK DESCRIPTION : ")
            print("------------------------------")
            current_time = datetime.datetime.now()
            current_time = current_time.strftime("%x")
            newTask = Task(description = desc, status = True, createdAt = current_time, updatedAt = current_time)
        elif choose == "2":
            Task.getTasks()
            inputId = input("PLEASE SELECT THE TASK WHOSE STATUS YOU WANT TO CHANGE : ")
            print("------------------------------")
            Task.changeStatus(inputId)
        elif choose == "3":
            Task.getTasks()
            inputId = input("PLEASE SELECT THE TASK YOU WANT TO REMOVE : ")
            print("------------------------------")
            Task.removeTask(inputId)
        elif choose == "4":
            Task.getActiveTask()
        elif choose == "5":
            Task.getInactiveTask()
        elif choose == "6":
            inputDate = input("PLEASE ENTER IN MM/DD/YY FORMAT : ")
            print("------------------------------")
            Task.activeDateRange(inputDate)
            pass
        elif choose == "7":
            inputDate = input("PLEASE ENTER IN MM/DD/YY FORMAT : ")
            print("------------------------------")
            Task.inactiveDateRange(inputDate)
            pass
        elif choose == "8":
            if Task.getTasks() != 0:
                inputId = input("PLEASE SELECT THE TASK YOU WANT TO UPDATE : ")
                print("------------------------------")
                current_time = datetime.datetime.now()
                current_time = current_time.strftime("%x")
                Task.updateTask(inputId,current_time)
        elif choose == "9":
            Task.getTasks()
        elif choose == "10":
            break
        else:
            print("WRONG CHOOSE")
            print("------------------------------")
