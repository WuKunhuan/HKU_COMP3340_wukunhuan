
## __Objectives__
1. Connect to HKU CS GPU Farm
2. Create a virtual environment
3. Install libraries and toolkits in the virtual environment
4. Install and open the JupyterLab of the virtual environment


## __Usage__

### Option 1: Run python scripts to use HKU CS GPU Farm remotely

Requirement: Have applied HKU CS GPU Farm memory
1. Download <a href="https://github.com/WuKunhuan/HKU_COMP3340/blob/main/HKU%20CS%20GPU%20Farm/setup_gpu_farm.py" target="_blank">setup_gpu_farm.py</a> and <a href="https://github.com/WuKunhuan/HKU_COMP3340/blob/main/HKU%20CS%20GPU%20Farm/setting.txt" target="_blank">setting.txt</a>
2. Open ```setting.txt``` and provide information
3. Open a Terminal (Mac/Linux) or Command Prompt (Windows) in the folder, enter 
```
python setup_gpu_farm.py
```
then follow the instructions. 
4. Open another Terminal (Mac/Linux) or Command Prompt (Windows) in the folder, enter 
```
python setup_gpu_farm_2.py
```
then follow the instructions. 


### Option 2: Run terminal commands to use HKU CS GPU Farm remotely

Set up a new folder ```root directory``` and open a Terminal (Mac/Linux) or Command Prompt (Windows) on it.

Enter the following command (replace ```account``` to your CS GPU Farm Account), and then followed by the password: 

```
ssh -X {account} @gpu2gate1.cs.hku.hk
```

Enter the following to get GPU memory: 

```
gpu-interactive
```

Enter the following commands to install Anaconda (replace ```account``` to your CS GPU Farm Account): 

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
export PATH=/userhome/cs2/{account}/anaconda3/bin:$PATH
```

Enter the following commands to install pip and jupyter lab: 

```
conda install pip
conda install jupyterlab
```

Create a virtual environment (replace ```venv``` to your desired name): 

```
conda create -n {venv} python=3.7 -y
```

Install Pytorch, torchvision, cudatoolkit in the virtual environment: 

```
conda install pytorch==1.7.1 torchvision==0.8.2 cudatoolkit=10.1 -c pytorch
```

Take note of the ```IP address``` of the GPU computed node by running the following command (e.g., 10.64.32.55): 

```
hostname -I
```

Start Jupyter Lab. Take note of the ```URL``` and the ```port number``` (e.g., 8888) in the end: 

```
jupyter-lab --no-browser
```

__Start another terminal,__ enter the following command to start the Jupyter Lab (replace ```account``` to your CS GPU Farm Account, replace ```port number```, ```IP address``` to the information above: 
```
ssh -L {port number}:localhost:{port number} {account}@{IP address}
```

Copy the ```URL``` to a web browser to see the jupyter lab of our virtual environment ```venv```. 


### Option 3: Run python scripts to setup the virtual environment locally. 


### Option 4: Run terminal commands to setup the virtual environment locally. 






