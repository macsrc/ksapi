from ks_api_client import ks_api

# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.

# Production Setup - 26-Oct-2022
client = ks_api.KSTradeApi(access_token="7abce22b-263e-36d0-b0c3-fbe6304bc517",
                           userid="SH3654",
                           consumer_key="KZifCybgPTZF8fTRfkuNNKK0WeQa",
                           ip="127.0.0.1",
                           app_id="DefaultApplication",
                           host="https://tradeapi.kotaksecurities.com/apim",
                           consumer_secret="eTIYRPzU0Q5dL_gL_2bWBaIifWYa")

# ### Sandbox Setup - 26-Oct-2022
# client = ks_api.KSTradeApi(access_token="caa80a21-38cd-32cb-943b-b58259fa4b17",
#                            userid="SH3654",
#                            consumer_key="O8MFM5v3FgO4BN2_R8vDp8XSTWIa",
#                            ip="76.223.105.230",
#                            app_id="DefaultApplication",
#                            host="https://theyogee.com/",
#                            consumer_secret="GR0t5f6iE3D58yWxhijf37RoaJQa")

# Initiate login and generate OTT
client.login(password="M_K@10E22g")

# Complete login and generate session token
client.session_2fa()
# You can choose to use a day-to-day access code by adding accesscode parameter : client.session_2fa(access_code = "")

# Place an order. Order_type can be "N", "MIS", "MTF". "SOR". Set variety as "AMO" for post-market orders. Please
# check detailed documentation (see bottom of page) for more details on each variable. Instrument tokens can be found
# at the following urls (NOTE: Please replace DD_MM_YYYY with the latest date for updated instrument tokens,
# for example 27_05_2021 will give tokens for 27 may): Equity:
# https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_DD_MM_YYYY.txt Derivatives:
# https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_DD_MM_YYYY.txt
client.place_order(order_type="N", instrument_token=727, transaction_type="BUY",
                   quantity=1, price=0, disclosed_quantity=0, trigger_price=0,
                   tag="string", validity="GFD", variety="REGULAR")

# Modify an order
client.modify_order(order_id="", price=0, quantity=1, disclosed_quantity=0, trigger_price=0, validity="GFD")

# Cancel an order
client.cancel_order(order_id="")

# Get Order Book
client.order_report()

# Get Detailed Order Report for specific order id [equity] .
client.order_report(order_id="")

# Get Detailed Order Report for specific order id [FNO] .
client.order_report(order_id="", is_fno="Y")

# Get Trade Book
client.trade_report()

# Get Detailed Trade Report for specific order id [equity] .
client.trade_report(order_id="")

# Get Detailed Trade Report for specific order id [FNO] .
client.trade_report(order_id="", is_fno="Y")

# Get Margin required for Equity orders.
order_info = [
    {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
    {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
]
client.margin_required(transaction_type="BUY", order_info=order_info)

# Get Available Margin
client.margin()

# Get Positions. position_type can be "TODAYS", "OPEN", "STOCKS".
client.positions(position_type="TODAYS")

# Get Quote details.
client.quote(instrument_token="110")
# Get Quotes for multiple tokens at once. Separate tokens by a hyphen.
client.quote(instrument_token="727-1250")


# Websocket:

# Subscribe to instrument price feed:
def callback_method(message):
    print(message)
    print("Your logic/computation will come here.")


client.subscribe(input_tokens="745,754", callback=callback_method)


# Response structure: ignore, ignore, Best buy price, Best buy quantity, Best sell price, Best sell quantity,
# Last trade price, High price, Low price, Average trade price, Closing price, Open price, Net change percentage,
# Total sell quantity, Total buy quantity, Total trade qty, Open Interest, Total trade value, Last trade quantity,
# Last trade time, Net change, Upper circuit limit, Lower circuit limit

# Subscribe to order status update websocket
# (instrument token supplied in function is merely a placeholder and serves no purpose here):
def callback_method(message):
    print(message)
    print("Your logic/computation will come here.")


client.subscribe(input_tokens="727", callback=callback_method,
                 broadcast_host="https://wstreamer.kotaksecurities.com/feed/orders")

# Unsubscribe from streaming service.
client.unsubscribe()

# Terminate user's Session
client.logout()
