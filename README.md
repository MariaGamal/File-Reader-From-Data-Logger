 # **File Reader From Data Logger** 
 ## Project Description:
 A python program to read the dump file from a data logger. The program reads the file and decodes the data to extract different channels then plots specifc channels. Each line of data is a packet of data from different sensors.
 ### Specifically it does the following:
1. Read the included text file.
The data format is in Hex (Excluding time, date and text_id).
2. Convert hex values to decimal.
3. Extract different channels from each line using the packet format below.
4. Plot the data in subplots vs time.
      * sub plot 1 include: yoc_temp, yoc_SP, yoc_SP,yoc_h_adc, yoc_h1,yoc_h2,
      * sub plot 2 include: yoc_p1 till yoc_p5, yoc_i_adc,
      * sub plot 3 include: yoc_filter,yoc_h1 ,yoc_h2, yoc_i_adc
5. Write the processed data into a new csv file.

## Packet Format:
each row consists of the following  
{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Time:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; text_id,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_temp, // Current Temperature  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_SP, // Target Temperature  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_p1, // Device 1 state Off=0, LOW speed=1,on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_p2, // Device 2 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_p3, // Device 3 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_p4, // Device 4 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_p5, // Device 5 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl1, // External Device 1 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl2, // External Device 2 state Off=0, on=2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_lights, // Lights 1 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_stereo, // Stereo state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_h1, //H-Device 1 state Off=0, start-up routine=1, running=2,exit_routine  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_h2, //H-Device2 state Off=0, start-up routine=1, running=2,exit_routine  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_filter, // filter Stages from 0 to 7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl4, // External Device 4 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl5, // External Device 5 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl6, // External Device 6 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_h_adc, // Internal Temperature  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl7, // External Device 7 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_econ, // power saving state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_i_adc, // current  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_all_on, // alarm Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl8, // External Device 8 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl9, // External Device 9 state Off=0, on=1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yoc_bl10, // External Device 10 state Off=0, on=1   
}  
 
 
