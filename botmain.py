import sys
import os
import time

from DeepTraderBot import DeepTraderBotv1
from bot_utils import read_configuration

#import pickle

#import cPickle as pickle
from twisted.internet import reactor


if __name__ == "__main__":

	#Read the configuration file

    config = read_configuration('settings.config')
    
    mybot = DeepTraderBotv1(config,maxcandles=5)
    mybot.setKeyPriv(config)
    
    mybot.connectClientAccount()
    mybot.connectWebSocket()
    
    
        	
	

	#inst = ElixTheBot('XLMBTC',1)
	#inst.setMine()
	#inst.connectClientAccount()

#	inst.connectWebSocket()
    

#	time.sleep(300*50)
#	print("sleep has finished")


	#save the object to read it later on	

#	inst.saveCandles("test_pickle_200_from1105.p")
	
	#inst.loadCandles("test_pickle_200_from1105.p")
	
	#analyzeData(inst)


#	inst.bm.stop_socket(inst.conn_key)
#	inst.bm.close()
#	reactor.stop()

	#exit()
