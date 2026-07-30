import psutil
import sys
import os
import time
import schedule
from SendMail import SendMail

def ProcessScan():
    listprocess=[]

    
    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["pid","name","username","status"])
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            
            print("Unable to fetch process information:")
        

       listprocess.append(info)
       return listprocess


def PlatformSurvillance(FolderName,ReceiverMail):

    if "@" not in ReceiverMail:
        print("Invalid email address")
        return


    Border="_"*50
    Ret=False
    Ret=os.path.exists(FolderName)

    if(Ret==True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to proceed as  folder name is existing but its not a directory")
            return
            
        
    else:
        os.mkdir(FolderName)
        print("directory  for the log file gets created sucessfully")

    timestamp=time.strftime("%Y-%m-%d_%H_%M_%S")

    FileName=os.path.join(FolderName,"Ankita_%s.log" %timestamp)

    try:
        fobj=open(FileName,"w")

    except PermissionError:
        print("Permission denied for log file")
        return

    except Exception as e:
        print("Unable to create log file:",e)
        return
    
    print(f"log file get sucessfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("------ Platform Survillence System------\n")
    fobj.write("log file gets created at:"+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------System Report-----------------")

    #Cpu information

    fobj.write("no of active cpu cores :%s\n" %psutil.cpu_count())

    fobj.write("cpu usage :%s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #Ram information
    memory=psutil.virtual_memory()

    fobj.write("Ram usage :%s %%\n" %memory.percent)
    fobj.write("total ram available :%s\n" %memory.total)
    fobj.write(Border+"\n")

    #network usage
    netobj=psutil.net_io_counters()

    fobj.write("network usage report\n")

    fobj.write("sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))

    # process log

    Data=ProcessScan()

    for info in Data:
        
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("UserName: %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("cpu usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Ram usage: %.2f\n" %info.get("memory_percent"))

        fobj.write(Border+"\n")



   

    fobj.write(Border+"\n")
    fobj.write("----------------End of Log file-----------------")

    fobj.write(Border+"\n")
    fobj.close()


    subject = "Platform Surveillance Report"

    body = "Please find attached Platform Surveillance Log File."

    try:
        SendMail(ReceiverMail, subject, body, FileName)

    except Exception as e:
        print("Mail sending failed:",e)

    


def main():
    


    Border="_"*50
    print(Border)
    print("--------Platform Survillence System------")
    print(Border)


    #--h & --u handling
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
           print("this automation script is used to perform")
           print("1:it fetch the information of running processess")
           print("2:it fetch information about the primary storage as Ram")
           print("3:it fetch information about the secondary storage as Hdd")
           print("4:it fetch information about the microprocessor")
           print("5:it gets  auto schedule perodically")
           print("6:it maintains all records into log file")
           print("7: it sends the  log files through mail perodically")
                      
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use the automation script are")
            print(f"python {sys.argv[0]}  Time_Interval Folder_Name")
            print("Time_Interval:Time of folder for the log file creation")
           
           

                 
        else:
            print("Unable to proceed as there no matching argument")
            print("Please use --h or --u flag for getting more details")


    # actual project code
    elif(len(sys.argv)==4):

        #print("cpu usage:",psutil.cpu_percent())
        print("Schedular started sucessfully")
        print("press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(
    PlatformSurvillance,
    sys.argv[2],
    sys.argv[3]
)

        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not  matching")
        print("Please use --h or --u flag for getting more details")



    print(Border)
    print("Thank You For Using our Automation System")
    print(Border)


    


if __name__=="__main__":
    main()
