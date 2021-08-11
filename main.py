from rh_stock_functions import *
from system_functions import *


def buy_doge(price_to_buy):
    money_to_spend = False
    while not money_to_spend:
        amount_to_buy = (get_crypto_buying_power() - 150.01).__round__(2)
        print(f'Total to spend: ${amount_to_buy}')
        sleep(1)
        if amount_to_buy > 76:
            money_to_spend = True
    print(f'Buying Doge at ${price_to_buy} or lower...')
    sleep(3)
    amount_to_buy = (get_crypto_buying_power() - 150.01).__round__(2)
    last_sold_price = float(rs.get_all_crypto_orders()[0]['price'])
    try:
        buying = True
        while buying:
            current_doge_price = float(rs.crypto.get_crypto_quote('DOGE')['mark_price'])
            if current_doge_price <= price_to_buy:
                buy_crypto_by_price('DOGE', amount_to_buy)
                sleep(1)
                buying = False
            time = get_current_time()
            print(f'${current_doge_price}/Doge at {time} (buying ${amount_to_buy} when under ${price_to_buy}/Doge); last sold: ${last_sold_price}')
            sleep(1)
            one_percent_away = current_doge_price * 1.01
            if current_doge_price > one_percent_away:
                sleep(2)
        print(f'All Doge bought (around ${current_doge_price}/Doge).')
        sleep(5)
    except Exception:
        sleep(15)
        rh_login()
        buy_doge(price_to_buy)
    else:
        price_to_sell = (current_doge_price * 1.02).__round__(6)
        sell_doge(price_to_sell)


def sell_doge(price_to_sell):
    doge_to_sell = False
    while not doge_to_sell:
        amount_to_sell = float(rs.crypto.get_crypto_positions()[0]['quantity'])
        print(f'Doge to sell: {int(amount_to_sell)}')
        sleep(1)
        if amount_to_sell > 1:
            doge_to_sell = True
    try:
        selling = True
        while selling:
            current_doge_price = float(rs.crypto.get_crypto_quote('DOGE')['mark_price'])
            if current_doge_price >= price_to_sell:
                sell_crypto_by_quantity('DOGE', amount_to_sell)
                selling = False
            time = get_current_time()
            print(f'${current_doge_price}/Doge at {time} (selling {int(amount_to_sell)} Doge at ${price_to_sell})')
            sleep(1)
            one_percent_away = price_to_sell * 0.99
            if current_doge_price < one_percent_away:
                sleep(2)
                amount_to_sell = float(rs.crypto.get_crypto_positions()[0]['quantity'])
        print(f'All Doge sold (around ${current_doge_price}/Doge).')
    except Exception:
        sleep(15)
        rh_login()
        sell_doge(price_to_sell)
    else:
        price_to_sell = (price_to_sell - (price_to_sell * 0.005)).__round__(6)
        buy_doge(price_to_sell)


if __name__ == '__main__':
    
    rh_login()
    
    command = input('Buy or sell?\n').lower()
    
    if command == 'buy':
        
       price_to_buy = float(input('Input price at which to buy Doge: '))
       buy_doge(price_to_buy)
        
    elif command == 'sell':
        
        price_to_sell = float(input('Minimum price to sell per Doge: '))
        sell_doge(price_to_sell)
        
    rh_logout()
