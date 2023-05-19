This repository contains data, scripts, and files related to experiments conducted for metric analysis.
The purpose of this readme is to provide an overview of the files and scripts available in this folder.

The metrics (latency, response rate, transmission rate)
In this folder, you will find files containing the mean execution time of the evaluated metrics.
Initially, the raw values obtained during the experiments were very small and did not provide 
satisfactory results when performing calculations.

To overcome this limitation, a different approach was adopted. 
The execution mean of each experiment day was calculated, and a new table was generated 
containing the results related to the mean execution time of each tested command. 
This approach allowed for more significant results and facilitated the processing of metrics using statistical methods.

Scripts
At the root of this folder, you will find two scripts:

Script 1: This script is responsible for calculating the mean of the latency and response rate metrics.

Script 2: This script is specific for handling the transmission rate metric.

Graphs and Tables
Within the subfolders of the "Mean" folder, you will find Python code that generates graphs for each evaluated metric. 
Additionally, there are scripts for creating tables in LaTeX format. The processed files, 
such as "media_latencia_apt.csv" and others, are also available in these subfolders.

Notes
It is important to note that the mean execution time values were calculated from ten days of experimentation, 
with 30 consecutive repetitions of the tested commands.
Ensure that the scripts are properly configured and that all necessary dependencies are installed for proper execution.
Feel free to explore the available graphs, tables, and processed files in this folder.
If you have any questions or need more information, feel free to contact us.