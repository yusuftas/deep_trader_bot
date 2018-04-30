import configparser
from collections import deque
from CandleBase import CandleBase

import matplotlib.pyplot as plt


try:
    import cPickle as pickle
except ImportError:
    import pickle



def read_configuration(file_name):

    config = configparser.ConfigParser()
    config.read(file_name)
    
    return config['DEFAULT']


def analyzeData(bot):

	candles = bot.candleQueue

	openings = []
	closings = []

	for candle in candles:
		openings.append(candle.openp)
		closings.append(candle.closep)

	maxp = max(closings)
	minp = min(closings)

	print("Max and min points of closings : %.8f  %.8f"%(maxp,minp))


def importQueue(symbol,start,step,final):
    
    points = list(range(start,final+1,step))
    
    opening_list = []
    closing_list = []
    
    
    for i in range(len(points)-1):
        
        p_from = points[i]
        p_to   = points[i+1]
    
        #saved files should be under the folder history
        filename = './history/' + symbol + '_' + str(p_from) + '_' + str(p_to)
        
        #print(filename)
        
        fileObject = open(filename,'rb')
        candles = pickle.load(fileObject)
        fileObject.close()
        
        for candle in candles:
            opening_list.append(candle.openp)
            closing_list.append(candle.closep)
               

    return [opening_list,closing_list]


def plotList(curr_list):
    
    plt.plot(curr_list)
    plt.show()





