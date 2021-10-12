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


    Initial = input('What is the intial investment amount: ')
    Initial = int(Initial)

    Return = input('What is the yearly return in decimal form?: ')
    Return = Decimal(Return)

    Time = input('How many years long is the investment?  ')
    Time = int(Time)
    Months = Time*12

    Amtadd = input('How many dollars are invested each month?: ')
    Amtadd = int(Amtadd)

    length = []
    
        

    for i in range(Months):
        length.append(i)
    
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
        monc = str(Amtadd)
              
        
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1,bottom=0.3)
        
       
        plt.ticklabel_format(style='plain')
        plt.title('Compound Interest of  Principle and Incremental Contribution Simulator')

        textreturn = Return*100
        textreturn = str(textreturn)
        
        p, = plt.plot(length,tlist,label=(graphlabel + ' dollar investment with ' + monc + ' dollars contributed monthly with a yearly return rate of '+ textreturn + "%"))
        plt.legend(loc='upper left')
        plt.text(Months, int(tlist[-1]), ' $' + str(tlist[-1]))
        
        graphlength = int(len(length) + 80)
        
        plt.xlim([0,graphlength])
        plt.ylabel("Dollars")
        plt.xlabel("Months Elapsed")
        plt.yscale('linear')
        
        plt.pause(1)
        repeatornah()
        
    
    def repeatornah():
        answer = input('Press 1 for another graph:  ')
        if (answer == '1'):
            again = True
            while (again == True):
                Graph()      
            else:
                print('Later space cowboy')        
    Formula()
    plt.show()
Graph()
