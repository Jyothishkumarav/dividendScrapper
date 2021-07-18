from nsetools import Nse
import json
def stock_details(stock):
    nse = Nse()
    all_stock_details = nse.get_stock_codes()
    search_stock = stock.lower().replace('ltd', 'limited')
    newDict = {key: value for (key, value) in all_stock_details.items() if str(value).lower() in search_stock }
    try :
        if len(newDict) > 0:
            index = list(newDict.keys())[0]
            q = nse.get_quote(index)
            str_data = json.dumps(q)
            data =json.loads(str_data)
            lastPrice = data['lastPrice']
            dayLow = data['dayLow']
            change = data['change']
            dayHigh = data['dayHigh']
            low52 = data['low52']
            high52 = data['high52']
            stock_depth_details = 'lastPrice :{} change :{} dayHigh : {} low52 : {}  high52 : {} '.format(lastPrice,change,dayHigh,low52,high52)
            print('lastPrice :{} change :{} dayHigh : {} low52 : {}  high52 : {} '.format(lastPrice,change,dayHigh,low52,high52))
            return stock_depth_details
        else:
            print('Not able to find details of  stock')
            return 'Not able to find details of  stock'
    except :
        return 'Not able to filter'

stock_details('ESAB INDIA LTD')



