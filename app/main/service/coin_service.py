import datetime
import time

from flask import current_app
from pycoingecko import CoinGeckoAPI
from sqlalchemy import func

from app.main import db
from app.main.model.coin import CoinPrice
from app.main.notification.mail_notification import sendEmail

cg = CoinGeckoAPI()
price = 0


def getCointPriceFromCoinNDate(coin, date):
    se_date = datetime.datetime.strptime(date, "%d-%m-%Y")
    coinPriceObj = CoinPrice.query.filter_by(coin=coin).filter(func.date(CoinPrice.timestamp) == se_date.date()).all()
    return coinPriceObj


def checkAndUpdateCoinPrice(app, ids, vs_currencies, coin):
    subject = "Price Fluctuation"
    prepared_message = "Latest price of {coin} is {price}"
    with app.app_context():
        while True:
            global price
            latest_price = cg.get_price(ids=ids, vs_currencies=vs_currencies)[ids][vs_currencies]
            print(latest_price)
            if not price:
                coinprice_obj = CoinPrice.query.filter_by(coin=coin).order_by(CoinPrice.id.desc()).first()
                if not coinprice_obj:
                    create_coin_price(latest_price, coin)
                    price = latest_price
                    current_app.logger.info(f"Data Saved in Empty table with price --> {latest_price}")
                else:
                    if coinprice_obj.price != latest_price:
                        create_coin_price(latest_price, coin)
                        current_app.logger.info(f"New Data Added in table with price --> {latest_price}")
                        sendEmail(subject, prepared_message.format(coin=coin, price=price), "shivam4838@gmail.com",
                                  ['shivam4838@gmail.com"', ])
                price = latest_price
            else:
                if price != latest_price:
                    create_coin_price(latest_price, coin)
                    price = latest_price
                    sendEmail(subject, prepared_message.format(coin=coin, price=price), "shivam4838@gmail.com",
                              ['shivam4838@gmail.com"', ])
            time.sleep(30)  # TODO: This need to change from hard coding to enviromental variables.


def create_coin_price(latest_price, coin):
    new_coin_obj = CoinPrice(
        price=latest_price,
        coin=coin
    )
    save_changes(new_coin_obj)


def save_changes(data: CoinPrice) -> None:
    db.session.add(data)
    db.session.commit()
