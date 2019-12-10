**************
*  CSI 4999  *
* Stockwatch *
*    Readme  *
**************


********************************Machine Learning*****************************************
###Dependencies:
Windows 7 x64 or newer
Python 3.7
Tensorflow
OpenAI Gym | pip install gym
Keras + Keras-rl | pip install keras && keras-rl
bokeh | pip install bokeh
pandas | pip install pandas
h5py | pip install h5py


###File Structure
.
|
|- csv2npy
|	|-csv2npy.py  #used to convert csv files into numpy arrays. Its how we got our data files. Instructions are included in the program
|
|- data
|	|- <data folders> #The folders contain the three data files for each stock symbol. copy and paste these into the data folder to use the datasets in the program
|	|-test_data.npy			#the test data
|	|-train_data.npy		#the data used for training
|	|-validation_data.npy	#the data used to validate
|
|- trading_agent
|	|-trailing #this folder contains the data for each run of the Agent
|	|	|-<test folders> #these folders contain the output of the agent, including graphs and weights files. the naming convention is epochs, steps, window_length, day, month, hour, minute, random number. 
|	|
|	|-dqn_agent.py 	#RUN THIS CODE. this is the file that runs everything
|	|-env.py		
|	|-plotter.py	
|	|-trail_env.py



###How to run:
Install the dependencies
Select your datasets and place into the data folder
Run dqn_agent.py
view data output in \trading_agent\trailing\ folder



******************************************************************************************








references:
https://github.com/Kostis-S-Z/trading-rl