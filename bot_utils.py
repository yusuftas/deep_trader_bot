import configparser

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