import sys
import os
import time


from twisted.internet import reactor

from DeepTraderBot import DeepTraderBotv1
from bot_utils import read_configuration

#import pickle
#import cPickle as pickle



if __name__ == "__main__":

	#Read the configuration file
    config = read_configuration('settings.config')

    #set credential of the accounts.    
    mybot = DeepTraderBotv1(config,maxcandles=5)
    mybot.setKeyPriv(config)
    
    #Depending on the running type start an operation
    runner = config['running_type']
    
    if runner == 'save':
        mybot.connectClientAccount()
        mybot.connectWebSocket()
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
            print('\n\t p : print total stored candles')
        elif selection == 'e':
            print('Exiting the program and stopping all processes.')
            mybot.closeConnection()
            raise Exception('exit')
        elif selection == 'p':
            print('Total candles: ' + str(mybot.getTotalStored()))
        else:
            print('Unknown option.')    
        

