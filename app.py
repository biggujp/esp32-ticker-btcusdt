import time
import urequests

SSID = "INSERT YOUR NAME WIFI"
SSID_PASSWORD = "INSERT YOUR WIFIPASSWORD"

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSID_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()

def lineNotify(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = 'INSERT YOUR TOKEN'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    msg = 'message={}'.format(msg).encode('utf-8')
    res = urequests.post(url, headers=headers , data = msg)
    return res

def get_dt_candle(symbols):
    url ='https://api.binance.com'
    response = urequests.get(url+'/api/v3/ticker/tradingDay?symbol='+symbols+'')
    if response.status_code == 200:
        data = response.json()
        print(data)
        symbol = data['symbol']
        last_price = data['lastPrice']
        last_price=round(float(last_price),2)
        high_price=data['highPrice']
        high_price=round(float(high_price),2)
        low_price=data['lowPrice']
        low_price=round(float(low_price),2)
        per_change=data['priceChangePercent']
        per_change=round(float(per_change),2)
        open_price=data['openPrice']
        #print(last_price,high_price,low_price,per_change)        
        return symbol,last_price,high_price,low_price,per_change,open_price
    
op_p = 0.0
while True :
    symbol,tk_last_btcusdt, tk_high_btcusdt,tk_low_btcusdt,tk_per_change,open_price = get_dt_candle('BTCUSDT')
    if op_p != open_price and open_price != 0.0 :
        msg = "{}\nราคาล่าสุด : {}\nราคาสูงสุด : {}\nราคาต่ำสุด : {}\nการเปลี่ยนแปลง : {}".format(symbol,tk_last_btcusdt,tk_high_btcusdt,tk_low_btcusdt,tk_per_change)
        time.sleep(3)
        lineNotify(msg)
        op_p = open_price   
