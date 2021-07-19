import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

class Decode_Plot:
    def __init__(self, file):
        '''
        The decode is perfomed in 3 steps:
        Step 1: Reading the file in a dataframe, transposing it (replaced the rows by columns) and removing Nan values.
        Step 2: Changing the values from hex to decimal starting row 2 till the end of channels,
        assuming all files are given in the same format.
        Step 3: Mapping each row to its channel, where each channel is represented by a list.
        '''
        self.df = pd.read_csv(file, header = None).T.dropna()   #Step1
        self.df.iloc[2:] = self.df.iloc[2:].applymap(lambda s: int(str(s), 16))   #Step2
        self.Date = list(self.df.iloc[0])    #Step3
        Time_id = list(self.df.iloc[1])
        self.Time = list(map(lambda x : x.split(" : ")[0][1:], Time_id))
        self.Text_id = list(map(lambda x: x.split(" : ")[1], Time_id))
        [self.yoc_temp , self.yoc_SP, self.yoc_p1, self.yoc_p2, self.yoc_p3, self.yoc_p4, self.yoc_p5, self.yoc_bl1, self.yoc_bl2, 
                self.yoc_lights, self.yoc_stereo, self.yoc_h1, self.yoc_h2, self.yoc_filter, self.yoc_bl3, self.yoc_bl4, self.yoc_bl5,
                self.yoc_bl6, self.yoc_h_adc, self.yoc_bl7, self.yoc_econ, self.yoc_i_adc, self.yoc_all_on, self.yoc_bl8, self.yoc_bl9,
                self.yoc_bl10 ] = [list(self.df.iloc[i]) for i in range(2,len(self.df.index))] 
        
        #Converting the timestamps to Python datetime objects, then converting them to matplotlib dates format to be used for plotting.
        self.list_of_datetimes = list(map(lambda x, y : datetime.strptime(x + ' '+ y , "%m/%d/%Y %H:%M:%S"), self.Date, self.Time))
        self.dates = matplotlib.dates.date2num(self.list_of_datetimes)
        
        
    def Plot(self, *args): 
        '''
        Plot function, with a variable number of arguments to plot the labels specified by the user against the time axis.
        The time is used as given in the file, converted to datetime object, then converted to matplotlib dates format.
        *args is a tuple of channels as string and the last element in the tuple is the subplot number.
        '''
        fig, ax = plt.subplots()
        for i in range(len(args)-1):
            y = args[i] #string
            x = getattr(self, y)
            if y != 'yoc_i_adc':  #this is the channel with the large values, so it's plotted using twinx() for the integration of a new y axis.
                ax.plot_date( self.dates, x , linestyle = 'solid',  xdate= True, ydate = False, label = y)
                ax.legend()
            else:
                ax1 = ax.twinx()
                ax1.plot_date( self.dates, x ,linestyle = 'solid', xdate= True, ydate = False, label = y, color = "pink")
                ax1.legend(loc = "lower left")
        ax.set_xlabel("Date-Time")
        ax.set_title("Subplot {}".format(args[-1])) #where arg[-1] is the Subplot number        
        plt.show()

    def create_csv(self, filename):
        '''
        A function that creates a csv file from the processed data in the current dataframe.
        The dataframe is transposed to return back to its original shape.
        '''
        self.df.T.to_csv(filename, header = False, index = False)


#Test Case:
test = Decode_Plot('outputfile.txt')
test.Plot('yoc_temp', 'yoc_SP','yoc_h_adc','yoc_h1', 'yoc_h2', 1 )
test.Plot('yoc_p1', 'yoc_p2' , 'yoc_p3' , 'yoc_p4' , 'yoc_p5', 'yoc_i_adc', 2)
test.Plot('yoc_filter','yoc_h1', 'yoc_h2', 'yoc_i_adc',3 )
test.create_csv('test.csv')



#Checking whether the new processed csv file is similar to the original file.
Original_df = pd.read_csv('outputfile.txt', header = None)
del Original_df[28]    #Deleting last column which contains Nan values
New_df = pd.read_csv('test.csv', header = None)
print(Original_df)
print(New_df)


