from binance.client import Client
from binance.enums import *
from binance.websockets import BinanceSocketManager

from collections import deque
from twisted.internet import reactor

from CandleBase import CandleBase

import pickle

#import cPickle as pickle

class DeepTraderBotv1:

    symbol  = ""
    balance = 0		# in terms of btc

    totalStoredCandles = 0
    lastStoredCandles= 0
    maxcandles = 200

#    def __init__(self, symbol, balance,maxcandles = 200):
#        self.symbol = symbol
#        self.balance = balance
#        self.maxcandles = maxcandles 
#
#        self.candleQueue = deque(maxlen=self.maxcandles)
    
    def __init__(self, config,maxcandles = 50):
        self.symbol = config['symbol']
        self.maxcandles = maxcandles 

        self.candleQueue = deque(maxlen=self.maxcandles)

    def setKeyPriv(self,config):
        self.key  = config['key']
        self.priv = config['priv']

    def connectClientAccount(self,key = None , priv = None):

        if key == None and priv == None:
            self.client = Client(self.key , self.priv)
        else:	    
            self.client = Client(key , priv)

    def connectWebSocket(self):
        self.bm       = BinanceSocketManager(self.client)
        self.conn_key = self.bm.start_kline_socket(self.symbol, self.process_message_kline, interval=KLINE_INTERVAL_1MINUTE)

        self.bm.start()

    def saveCandles(self,fname):
        fileObject = open(fname,'wb')
        pickle.dump(self.candleQueue,fileObject)
        fileObject.close()
        
        #clear the queue
        self.candleQueue.clear()
        print('Saved the queue and cleared it.')

    def loadCandles(self,fname):
        fileObject = open(fname,'rb')
        self.candleQueue = pickle.load(fileObject)
        fileObject.close()

    def process_message_kline(self,msg):
        #print("message type: {}".format(msg['e']))
        #print(msg)
		# do something

        kline   = msg['k']
        openp  = float(kline['o'])
        closep = float(kline['c'])
        highp  = float(kline['h'])
        lowp   = float(kline['l'])

        starttime = kline['t']
        stoptime  = kline['T']

        if kline['x'] == True:		#kline is it closed ?

            candle = CandleBase(starttime, stoptime,openp,closep,highp,lowp)
            
            self.candleQueue.append(candle)
            self.totalStoredCandles = self.totalStoredCandles + 1
			
            if self.totalStoredCandles%self.maxcandles == 0:
                
                fname = self.symbol + '_' + str(self.lastStoredCandles) + '_' + str(self.totalStoredCandles) 
                self.saveCandles(fname)
                
                self.lastStoredCandles = self.totalStoredCandles
                
			
#                for cand in self.candleQueue:
#                    print(cand)

#            self.bm.stop_socket(self.conn_key)
#            self.bm.close()
#            reactor.stop()
#            exit()



		#print("%s opening: %.8f  and closing: %.8f" %(self.symbol,float(opening),float(closing)))

#	def __del__(self):
#		self.bm.close()
#		print("Socket connection closed")

