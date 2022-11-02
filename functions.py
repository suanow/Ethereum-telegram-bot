from pycoingecko import CoinGeckoAPI
import requests
import json
from etherscan import Etherscan


ETHERSCAN_TOKEN = 'P1ARR161VTV5F45PSFDNWZ12I1DAK18J43'
gas_url = f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_TOKEN}'

cg = CoinGeckoAPI()

class price():
    def get_eth_usd():
        return cg.get_price(ids='ethereum', vs_currencies='usd').get('ethereum').get('usd')
    
    def get_eth_rub():
        return cg.get_price(ids='ethereum', vs_currencies='rub').get('ethereum').get('rub')
    
    def get_usd_rub():
        return cg.get_price(ids='busd', vs_currencies='rub').get('busd').get('rub')

    def gas():
        request = requests.get(gas_url)
        table = json.loads(request.content)['result']
        return f"FAST\t{table['FastGasPrice']}\nLOW\t{table['SafeGasPrice']}\nAVG\t{table['ProposeGasPrice']}"

    
class compute():
    def profit(msg):
        eth_rub = cg.get_price(ids='ethereum', vs_currencies='rub').get('ethereum').get('rub')
        
        p_sold = float(msg[0])
        p_com = float(msg[1])
        p_gas = float(msg[2])
        p_buy = float(msg[3])
        
        res = p_sold - p_com - p_gas - p_buy
        roi = 1 + (res / (p_com + p_gas + p_buy))
        
        return f'Input: \n \t Sale price = {p_sold} \n \t Fees amt = {p_com} \n \t Gas = {p_gas} \n \t Initial price = {p_buy}. \n \
                            \nProfit is: {round(res, 2)} eth or {round(res) * eth_rub} rub. \nROI = {round(roi, 2)}' 
    
class convert():
    def eth(msg):
        eth_usd = price.get_eth_usd()
        eth_rub = price.get_eth_rub()
        
        if len(msg) == 1:
            return f'ETH\t1\nUSD\t{eth_usd}\nRUB \t{eth_rub}'
        elif len(msg) == 2:
            return f'ETH\t{round(float(msg[1]), 2)}\nUSD\t{int(eth_usd * float(msg[1]))}\nRUB\t{int(eth_rub * float(msg[1]))}'
        else:
            return 'The function accepts either one or no number'
        
    def usd(msg):
        eth_usd = price.get_eth_usd()
        usd_rub = price.get_usd_rub()
        
        if len(msg) == 1:
            return f'USD\t1\nETH\t{1/eth_usd}\nRUB\t{usd_rub}'
        elif len(msg) == 2:
            return  f'USD\t{int(float(msg[1]))}\nETH\t{round(float(msg[1])/eth_usd, 2)}\nRUB\t{int(float(msg[1])*usd_rub)}'
        else:
            return 'The function accepts only one number.'
    
    def rub(msg):
        usd_rub = price.get_usd_rub()
        eth_rub = price.get_eth_rub()
        
        if len(msg) == 1:
            return f'RUB\t1\nETH\t{1/eth_rub}\nUSD\t{1/usd_rub}'
        elif len(msg) == 2:
             return  f'RUB\t{int(float(msg[1]))}\nETH\t{round(float(msg[1])/eth_rub, 2)}\nUSD\t{int(float(msg[1])/usd_rub)}'
        else:
            return 'The function accepts only one number.'

#Example cases
if __name__ == '__main__':
    print(price.get_eth_usd(), end='\n') # prints out the current exchange rate
    print(price.get_eth_rub(), end='\n') # prints out the current exchange rate
    print(price.get_usd_rub(), end='\n\n') # prints out the current exchange rate
    print(price.gas(), end='\n\n') # prints out the current gas prices for eth
    print(convert.eth(['/eth 1']))
    print(compute.profit([8, 0.1, 0.0015, 0.3]), end = '\n\n') # computes profit with buy, sell, gas and fees 