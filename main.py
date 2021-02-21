from rh_stock_functions import *
from system_functions import *


def buy_doge(price_to_buy):
    print(f'Buying Doge at ${price_to_buy} or lower...')
    sleep(3)
    try:
        buying = True
        while buying:
            current_doge_price = float(rs.crypto.get_crypto_quote('DOGE')['mark_price'])
            if current_doge_price < price_to_buy:
                amount_to_buy = (get_crypto_buying_power() - 0.04)
                buy_crypto_by_price('DOGE', amount_to_buy)
                buying = False
            time = get_current_time()
            print(f'${current_doge_price}/Doge at {time}')
            sleep(1)
            if current_doge_price > 0.0559:
                sleep(2)
        print(f'All Doge bought (around ${current_doge_price}/Doge).')
    except Exception:
        sleep(15)
        rh_login()
        buy_doge(price_to_buy)
    else:
        sell_doge()


def sell_doge():
    # Make sure there is no buying power first

    price_to_sell = float(input('Input price at which to sell Doge: '))
    try:
        selling = True
        while selling:
            current_doge_price = float(rs.crypto.get_crypto_quote('DOGE')['mark_price'])
            if current_doge_price > price_to_sell:
                sell_crypto_by_quantity('DOGE', 22711)
                selling = False
            time = get_current_time()
            print(f'${current_doge_price}/Doge at {time}')
            sleep(1)
            if current_doge_price < 0.0559:
                sleep(2)
        print(f'All Doge sold (around ${current_doge_price}/Doge).')
    except Exception:
        sleep(15)
        rh_login()
        sell_doge()
    else:
        price_to_sell = (price_to_sell - (price_to_sell * 0.028)).__round__(4)
        buy_doge(price_to_sell)


rh_login()
command = input('Buy or sell?\n').lower()
if command == 'buy':
    price_to_buy = float(input('Input price at which to buy Doge: '))
    buy_doge(price_to_buy)
elif command == 'sell':
    sell_doge()
rh_logout()
