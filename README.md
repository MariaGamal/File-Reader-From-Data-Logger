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
 
 
