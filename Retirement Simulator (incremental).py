import pandas as p
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
from decimal import Decimal
import numpy as np
from sympy import *
import mplcursors
import matplotlib.ticker
from matplotlib.widgets import Button

def Graph():

    #Gathering user input pertaining to the investment
    
    Initial = input('What is the intial investment amount: ')
    Initial = int(Initial)

    Return = input('What is the yearly return in decimal form?: ')
    Return = Decimal(Return)

    Time = input('How many years long is the investment?  ')
    Time = int(Time)
    Months = Time*12

    Amtadd = input('How many dollars are invested each month?: ')
    Amtadd = int(Amtadd)

    #Generates x values by appending (Years*12) into a list that contains the length of the investment
    
    length = []
    
    for i in range(Months):
        length.append(i)
        
    #Generates y values by inputting the user input values into the compound interest formula
        
    def Formula():
        p = Initial
        PMT = Amtadd
        r = Return
        n = 12
        tlist = []
    
        for i in range(Months):
            newrate = r/n
            newrate = newrate+1
            ex = i
            newrate = newrate**ex
            newrate = newrate - 1
            steptwo = newrate/(r/n)
            last = int(steptwo*PMT)
            
            rate = (r/n)
            rate = rate+1
            rate = rate**i
            final =int(p*rate)
            
            value = int(final + last)
            tlist.append(value)

        graphlabel = str(Initial)
        monc = str(Amtadd) #The monc variable = monthly contributions
              
        #Defines a new figure, adjusting the location of the plot and setting the background color to a light grey
        
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1,bottom=0.3)
        fig.set_facecolor((0.87,0.87,0.87))
        
        #Labels the plot by converting the user input to text to be displayed
        
        plt.ticklabel_format(style='plain')
        plt.title('Compound Interest of  Principle and Incremental Contribution Simulator')

        textreturn = Return*100
        textreturn = str(textreturn)
        
        #Ploting both x and y values, labeling the plot based on the components of the investment and displaying the future value of the investment at maturity
        
        p, = plt.plot(length,tlist,label=(graphlabel + ' dollar investment with ' + monc + ' dollars contributed monthly with a yearly return rate of '+ textreturn + "%"),color='r')
        plt.legend(loc='upper left')
        plt.text(Months, int(tlist[-1]), ' $' + str(tlist[-1]))
        ax.set_facecolor((0.87,0.87,0.87))
        graphlength = int(len(length) + 40)
        
        plt.xlim([0,graphlength])

        #Formatting the x axis to display the amount of years elapsed instead of the amount of months elapsed
        xticksloc = [1]
        
        for i in list(length):
            if ((i%12)==0):
                xticksloc.append(i)


        xtickslabels = []
        for i in list(xticksloc):
            xtickslabels.append(str(int((i/12)+1)))
        

        plt.xticks(xticksloc,xtickslabels)
        plt.ylabel("Dollars")
        plt.xlabel("Years Elapsed")
        plt.yscale('linear')
              
    Formula()
    plt.show()
    
Graph()
