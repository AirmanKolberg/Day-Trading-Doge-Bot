import pandas as pd
from dataframe_info import *
from os import system


def put_data_into_framework(the_data):
    data_broken = [the_data[i:i + 31] for i in range(0, len(the_data), 31)]
    days = [i for i in range(31)]

    framework = {
        'Days to Sell': days,
        '1% Growth': data_broken[0],
        '1.1% Growth': data_broken[1],
        '1.2% Growth': data_broken[2],
        '1.3% Growth': data_broken[3],
        '1.4% Growth': data_broken[4],
        '1.5% Growth': data_broken[5],
    }
    return framework


def get_crypto_sell_price(percentage_growth, days_to_sell, initial_assets,
                          buying_power, personal_margin, crypto_amount):

    assets_after_sell = initial_assets * (percentage_growth ** days_to_sell)
    sell_price = ((assets_after_sell - buying_power + personal_margin) / crypto_amount).__round__(2)
    return sell_price


def retrieve_needed_variables():
    # Import the most recent DataFrame from Frank
    crypto_csv = pd.read_csv(trading_dataframe)

    # Retrieve relevant variables from the DataFrame
    daily_average = (float((list(crypto_csv[average_tag]))[-1].replace('%', '')) / 100).__round__(7)
    day_count = float(((list(crypto_csv[assets_tag])[-1]).replace(pre_num, '')).replace(post_num, ''))
    frank_assets = float(list(crypto_csv[assets_tag])[-4])

    crypto = secret_crypto
    buying_power = secret_buying_power
    assets_offset = secret_assets_offset
    initial_assets = secret_initial_assets

    return daily_average, day_count, frank_assets, crypto, buying_power, assets_offset, initial_assets


if __name__ == '__main__':
    # Retrieve all variables required for calculations
    daily_average, day_count, frank_assets, crypto,\
    buying_power, assets_offset, initial_assets = retrieve_needed_variables()

    # Create a list containing all data for the DataFrame
    all_data = list()
    for growth in potential_growths:
        for days_to_go in range(0, 31):
            days_to_go += day_count
            all_data.append(get_crypto_sell_price(growth, days_to_go, initial_assets,
                                                  buying_power, assets_offset, crypto))

    # Create the DataFrame, export and open it
    framework = put_data_into_framework(all_data)
    df = pd.DataFrame(framework, columns=['Days to Sell', '1% Growth', '1.1% Growth',
                                          '1.2% Growth', '1.3% Growth', '1.4% Growth',
                                          '1.5% Growth'])
    df.to_csv('frankProfitsChart.csv')

    _ = system('open frankProfitsChart.csv')
