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

    #Generates x values for the linear contributions and the exponential return of compound interest
    
    length1 = []
    length2 = [0]
    
    for i in range(Months):
        length1.append(i)
        
    for i in range(Months):
        length2.append(i)
        
    #Generates y values for the linear contributions by using the equation: Total Amount Invested = (Number of Months x Amount Contributed Monthly) 
        
    def Formula():
        
        principleys = [Initial]
        
        for i in range(Months):
            pyvalue = (Amtadd*i)+1
            principleys.append(pyvalue)

    #Generates y values by inputting the user input values into the compound interest formula
        
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
        
        fig, (ax1,ax2) = plt.subplots(2,1)
        fig.set_facecolor((0.87,0.87,0.87))
        
        #Labels the plot by converting the user input to text to be displayed
        
        ax1.ticklabel_format(style='plain')
        ax1.set_title('Compound Interest of  Principle and Incremental Contribution Simulator')
        
        textreturn = Return*100
        textreturn = str(textreturn)
        
        #Ploting both x and y values, labeling the plot based on the components of the investment and displaying the future value of the investment at maturity
        
        ax1.plot(length1,tlist,color=(0.650, 0, 0.740),label=(graphlabel + ' dollar investment with ' + monc + ' dollars contributed monthly with a yearly return rate of '+ textreturn + "%"))
        ax1.plot(length2,principleys,color=(0.027, 0.058, 0.874),label="Total Funds Invested")
        ax1.legend(loc='upper left')
        ax1.text(Months, int(tlist[-1]), ' $' + str(tlist[-1]))
        ax1.text(Months+2,int(principleys[-1]),'$'+str(principleys[-1]))
        ax1.set_facecolor((0.87,0.87,0.87))
        graphlength = int(len(length1) + 40)
        
        ax1.set_xlim([0,graphlength])

        #Formatting the x axis to display the amount of years elapsed instead of the amount of months elapsed
        xticksloc = [1]
        
        for i in list(length1):
            if ((i%12)==0):
                xticksloc.append(i)


        xtickslabels = []
        for i in list(xticksloc):
            xtickslabels.append(str(int((i/12)+1)))
        

        ax1.set_xticks(xticksloc)
        ax1.set_xticklabels(xtickslabels)
        ax1.set_ylabel("Dollars")
        ax1.set_xlabel("Years Elapsed")
        ax1.set_yscale('linear')

        #Creating a bar graph to visualize gains

        PortfolioValue = (tlist[-1])
        TotalInvested = (principleys[-1])
        
        Gains = PortfolioValue-TotalInvested
        Barwid = ["Portfolio Value", "Funds Invested","Gains"]
        Barhig = [PortfolioValue, TotalInvested, Gains]

        
        colors = [(0.650, 0, 0.740),(0.027, 0.058, 0.874),(0.611, 0.898, 0.988)]

        p1 = ax2.bar(Barwid,Barhig,width=0.6,align="center",color = colors,linewidth=1,edgecolor="k")
        ax2.bar_label(p1,labels = ["$"+str(PortfolioValue),"$"+str(TotalInvested), "$"+str(Gains)],label_type="center")
        ax2.set_title("Gains From Investment")
        ax2.set_facecolor((0.87,0.87,0.87))
        ax2.set_xlim([-0.5,3])
        xtick_loc = [0.1,1.15,2.2]
        ax2.set_xticks([])
        ax2.legend(iter(p1), ('Portfolio Value', 'Funds Invested', 'Gains'))
              
    Formula()
    plt.show()
    
Graph()
