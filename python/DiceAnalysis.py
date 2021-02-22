import sys
import math
import numpy as np
import matplotlib.pyplot as plt
# import data.txt
#filename = 'dice.txt'
#dat = np.loadtxt(filename)
#flat = dat.flatten()
#add=np.sum(dat,axis=1)
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s" % sys.argv[0])
        print ("   -input [filename]  name of file for data")
        print
        sys.exit(1)
        
    haveInput = False
        
    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        haveInput = True
           
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")	
        print ("   -input [filename]  name of file for data")
    filename = InputFile 
    dat = np.loadtxt(filename)
    flat = dat.flatten()
    add=np.sum(dat,axis=1)
    #print(dat)
    #print(len(dat))
    #print(list1)
    #print(type(dat))
    # creates histogram
    n, bins, patches = plt.hist(flat, bins=range(8),alpha=0.7,rwidth=0.95)

    # plot formating options
    plt.xlabel('face number')
    plt.ylabel('Counts')
    plt.title(str(len(dat)*len(dat[0])) + ' dice rolls')
    plt.grid(axis='y', alpha=0.75)
    plt.xlim(xmin=0.5, xmax = 7.5)
    #plt.xticks(range(6))
    # show figure (program only ends once closed
    plt.show()

    # creates histogram
    n, bins, patches = plt.hist(add, bins=range(6*len(dat[0])+2) , alpha=0.7, rwidth=0.95)

    # plot formating options
    plt.xlabel('Sum of the face numbers for each experiment')
    plt.ylabel('Counts')
    plt.title(str(len(dat))+' experiments of '+str(len(dat[0]))+' dice rolls')
    plt.grid(axis='y', alpha=0.75)
    plt.xlim([len(dat[0]), 6.0*len(dat[0])+2])
    #plt.xticks(range(len(dat[0])-1,6*len(dat[0])+2))
    # show figure (program only ends once closed
    plt.show()
