import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp=r"C:\Users\Lalit.Chouhan\PycharmProjects\python-mega-course\website_blocker\hosts"
redirect="127.0.0.1"
website_list=["www.tutorialspoint.com","in.linkedin.com","www.google.com","https://www.fast2sms.com/","www.fast2sms.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,10):    
        print("working hours...")
        with open(hosts_path,'r+')as file:
            
            content=file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
                    
    else:
        print("fun time")
        with open(hosts_path,"r+")as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        
    time.sleep(5)