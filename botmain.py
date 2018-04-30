import sys
import os
import time


from twisted.internet import reactor

from DeepTraderBot import DeepTraderBotv1
from bot_utils import read_configuration
from bot_utils import importQueue,plotList



if sys.version_info[0] < 3: 
    input = raw_input



if __name__ == "__main__":

    #Read the configuration file
    config = read_configuration('settings.config')

    #Depending on the running type start an operation
    runner     = config['running_type']
    queue_size = int(config['queue_size'])


    #set credential of the accounts.    
    mybot = DeepTraderBotv1(config,maxcandles=queue_size)
    mybot.setKeyPriv(config)
    
    
    if runner == 'save':
	print('Connecting and starting the connection')
        mybot.connectClientAccount()
        mybot.connectWebSocket()
    elif runner == 'plot':
        start = int(config['start'])
        step  = int(config['step'])
        final = int(config['final'])
        
        [opening,closing] = importQueue('BTCUSDT',start,step,final)
        
        plotList(opening)
        
        sys.exit('Plot mode finished, exiting the robot')
        
    elif runner == 'test':
        print('Testing some part of the code')
    #more options will be added
    else:                           
        sys.exit('Error: Unknown running type is given')
    
    #Program execution options    	
	
    while 1:
        selection = input("Your selection? (h for help) ")    #python 3.x, for 2.x use raw_input
        
        if len(selection) > 1:
            print('Enter one character only.')
        elif selection == 'h':
            print('Select only one character option from available list:')
            print('\n\t h : help')
            print('\n\t e : exit')
	    print('\n\t t : test')
            print('\n\t p : print total stored candles')
        elif selection == 'e':
            print('Exiting the program and stopping all processes.')
            mybot.closeConnection()
            sys.exit('Finished and exiting.')
        elif selection == 'p':
            print('Total candles: ' + str(mybot.getTotalStored()))
	elif selection == 't':
	    mybot.test()
        else:
            print('Unknown option.')    
        

