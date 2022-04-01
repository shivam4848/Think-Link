import threading

from app import blueprint
from app.main import create_app
from app.main.service.coin_service import checkAndUpdateCoinPrice

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    scheduler = threading.Thread(target=checkAndUpdateCoinPrice, args=(app, 'bitcoin', 'usd', 'btc'))
    scheduler.start()
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
