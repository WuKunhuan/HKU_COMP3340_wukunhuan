
import os
account = "uxxxxxxx"
virtual_environment = "COMP3340"
setting = open("setting.txt", "r").readlines()
for line in setting:
    if (len(line) > 12):
        if (line[0:11] == "account = \""):
            account = line[11:len(line)-2:1]
            continue
    if (len(line) > 24):
        if (line[0:23] == "virtual_environment = \""):
            virtual_environment = line[23:len(line)-2:1]
            continue

os.system("clear")
input("Login to your CS GPU Farm")
os.system(f"ssh -X {account}@gpu2gate1.cs.hku.hk")
os.system("clear")
os.system(f"gpu-interactive")
os.system("clear")

input("Install Anaconda")
os.system("clear")
os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh")
os.system("bash Anaconda3-2020.11-Linux-x86_64.sh")
os.system("export PATH=/userhome/cs2/{account}/anaconda3/bin:$PATH")
os.system("clear")

input("Install pip")
os.system("clear")
os.system("conda install pip")
os.system("clear")

input("Install JupyterLab")
os.system("clear")
os.system("conda install jupyterlab")
os.system("clear")

input("Create a virtual environment")
os.system("clear")
os.system(f"conda create -n {virtual_environment} python=3.7 -y")
os.system("clear")

input("Install Pytorch, torchvision, cudatoolkit")
os.system("clear")
os.system("conda install pytorch==1.7.1 torchvision==0.8.2 cudatoolkit=10.1 -c pytorch")
os.system("clear")

