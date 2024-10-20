import json

class Task:

    id = 1
    _getTask = []

    @classmethod
    def load(Task):
        with open("id_tracker.json", "r") as id_file:
            Task.id = json.load(id_file)
        
        with open("task.json", "r") as task_file:
            try:
                Task._getTask = json.load(task_file)
            except json.JSONDecodeError:
                Task._getTask = []


    def __init__(self,description,status,createdAt,updatedAt):
        self.id = Task.id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        Task.id += 1
        self.writeJson()

    def writeJson(self):
        newData = {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updateAt" : self.updatedAt,
        }
        Task._getTask.append(newData)
        
        Task._openAndWriteTask()

        with open("id_tracker.json","w") as json_file:
            json.dump(Task.id,json_file)
        
    def getTasks():
        if Task._getTask != []:
            for x in Task._getTask:
                print(" TASK NUMBER : ",x["id"],"\n","TASK DESCRIPTION : ",x["description"],"\n","TASK STATUS : ",x["status"],"\n","TASK CREATED DATE : ",x["createdAt"],"\n","TASK UPDATED DATE : ",x["createdAt"])
                print("------------------------------")
        else:
            print("TASK NOT FOUND")
            print("------------------------------")
            return  0  

    def changeStatus(taskId):
        for x in Task._getTask:
            if int(taskId) == x["id"]:
                if x["status"] == False:
                    x["status"] = True
                else:
                    x["status"] = False
                break
        Task._openAndWriteTask()
        Task.getTasks()

    def removeTask(taskId):
        for x in range(len(Task._getTask)):
            if int(taskId) == Task._getTask[x]["id"]:
                Task._getTask.pop(x)
                Task._openAndWriteTask()
                Task.getTasks()
                break
    
    def getActiveTask():
        if Task._getTask != []:
            for x in Task._getTask:
                if x["status"] == True:
                    print(" TASK NUMBER : ",x["id"],"\n","TASK DESCRIPTION : ",x["description"],"\n","TASK STATUS : ",x["status"],"\n","TASK CREATED DATE : ",x["createdAt"],"\n","TASK UPDATED DATE : ",x["createdAt"])
                    print("------------------------------")
        else:
            print("TASK NOT FOUND")
            print("------------------------------")

    def getInactiveTask():
        if Task._getTask != []:
            for x in Task._getTask:
                if x["status"] == False:
                    print(" TASK NUMBER : ",x["id"],"\n","TASK DESCRIPTION : ",x["description"],"\n","TASK STATUS : ",x["status"],"\n","TASK CREATED DATE : ",x["createdAt"],"\n","TASK UPDATED DATE : ",x["createdAt"])
                    print("------------------------------")
        else:
            print("TASK NOT FOUND")
            print("------------------------------")

    def activeDateRange(taskDate):
        if Task._getTask != []:
            for x in Task._getTask:
                if x["createdAt"] == taskDate and x["status"] == True:
                    print(" TASK NUMBER : ",x["id"],"\n","TASK DESCRIPTION : ",x["description"],"\n","TASK STATUS : ",x["status"],"\n","TASK CREATED DATE : ",x["createdAt"],"\n","TASK UPDATED DATE : ",x["createdAt"])
                    print("------------------------------")
        else:
            print("TASK NOT FOUND")
            print("------------------------------")

    def inactiveDateRange(taskDate):
        if Task._getTask != []:
            for x in Task._getTask:
                if x["createdAt"] == taskDate and x["status"] == False:
                    print(" TASK NUMBER : ",x["id"],"\n","TASK DESCRIPTION : ",x["description"],"\n","TASK STATUS : ",x["status"],"\n","TASK CREATED DATE : ",x["createdAt"],"\n","TASK UPDATED DATE : ",x["createdAt"])
                    print("------------------------------")
        else:
            print("TASK NOT FOUND")
            print("------------------------------")

    def updateTask(taskId,updatedDate):
        if Task._getTask == []:
            print("TASK NOT FOUND")
            print("------------------------------")
        else:
            for x in Task._getTask:
                if x["id"] == int(taskId):
                    desc = input("PLEASE ENTER THE NEW TASK DESCRIPTION : ")
                    x["description"] = desc
                    x["updatedAt"] = updatedDate
                    Task._openAndWriteTask()
                    Task.getTasks()
                    break
            print("TASK NOT FOUND")
            print("------------------------------")
            
    def _openAndWriteTask():
        with open("task.json", "w") as json_file:
            json.dump(Task._getTask, json_file, indent=4)
