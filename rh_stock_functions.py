import robin_stocks as rs
from secrets import *
from system_functions import verify_int


def rh_login():
    rs.login(username=rh_user,
             password=rh_pass,
             expiresIn=86400,
             by_sms=True,
             store_session=True)


def rh_logout():
    rs.logout()


def buy_stock_by_dollar_amount(symbol, dollar_amount_to_buy):
    rs.orders.order_buy_fractional_by_price(symbol,
                                            dollar_amount_to_buy,
                                            timeInForce='gtc',
                                            extendedHours=False)


def buy_stock_by_shares(symbol, num_of_shares):
    rs.orders.order_buy_fractional_by_quantity(symbol,
                                               num_of_shares,
                                               timeInForce='gtc',
                                               extendedHours=False)


def buy_stock_when_price_is_right(symbol, quantity_as_int, price_limit):
    rs.orders.order_buy_limit(symbol,
                              quantity_as_int,
                              price_limit,
                              timeInForce='gtc',
                              extendedHours=False)


def buy_crypto_by_price(coin, dollar_amount_to_buy):
    rs.orders.order_buy_crypto_by_price(coin,
                                        dollar_amount_to_buy,
                                        timeInForce='gtc')


def buy_crypto_by_quantity(coin, num_of_coins):
    rs.orders.order_buy_crypto_by_quantity(coin,
                                           num_of_coins,
                                           timeInForce='gtc')


def buy_crypto_when_price_is_right(coin, coins_to_buy, price_per_coin):
    rs.orders.order_buy_crypto_limit(coin,
                                     coins_to_buy,
                                     price_per_coin,
                                     timeInForce='gtc')


def sell_stock_by_price(symbol, dollar_amount_to_sell):
    rs.orders.order_sell_fractional_by_price(symbol,
                                             amountInDollars=dollar_amount_to_sell,
                                             timeInForce='gtc',
                                             extendedHours=False)


def sell_stock_by_shares(symbol, num_of_shares):
    rs.orders.order_sell_fractional_by_quantity(symbol,
                                                num_of_shares,
                                                timeInForce='gtc',
                                                extendedHours=False)


def sell_stock_when_price_is_right(symbol, quantity_as_int, price_limit):
    rs.orders.order_sell_limit(symbol,
                               quantity_as_int,
                               price_limit,
                               timeInForce='gtc',
                               extendedHours=False)


def sell_crypto_by_price(coin, dollar_amount_to_sell):
    rs.orders.order_sell_crypto_by_price(coin,
                                         dollar_amount_to_sell,
                                         timeInForce='gtc')


def sell_crypto_by_quantity(coin, num_of_coins):
    rs.orders.order_sell_crypto_by_quantity(coin,
                                            num_of_coins,
                                            timeInForce='gtc')


def sell_crypto_when_price_is_right(coin, coins_to_sell, price_per_coin):
    rs.orders.order_sell_crypto_limit(coin,
                                      coins_to_sell,
                                      price_per_coin,
                                      timeInForce='gtc')


def get_crypto_buying_power():
    buying_power = float(rs.profiles.load_account_profile(info='crypto_buying_power')).__round__(2)
    return buying_power


def get_value_of_last_crypto_transaction():
    data = rs.get_all_crypto_orders()
    last_trade = data[0]['executions']
    try:
        transaction_value = (float(last_trade[0]['effective_price']) * float(last_trade[0]['quantity'])).__round__(2)
    except IndexError:
        return 'Transaction Pending...'
    else:
        return transaction_value
