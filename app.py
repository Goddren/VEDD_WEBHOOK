from flask import Flask, request
import os
import alpaca_trade_api as tradeapi
import kucoin.client

app = Flask(__name__)

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure Alpaca API authentication
alpaca_api = tradeapi.REST(
    os.getenv('ALPACA_API_KEY'),
    os.getenv('ALPACA_API_SECRET'),
    os.getenv('ALPACA_API_BASE_URL')
)

# Configure KuCoin API authentication
kucoin_api = kucoin.client.Client(
    os.getenv('KUCOIN_API_KEY'),
    os.getenv('KUCOIN_API_SECRET'),
    os.getenv('KUCOIN_API_PASSPHRASE')
)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Get the JSON data from the request payload
    
    # Retrieve the desired inputs from the webhook data or request parameters
    tp = data.get('tp')  # Example: Retrieve the TP value from the webhook data
    sl = data.get('sl')  # Example: Retrieve the SL value from the webhook data
    trail = data.get('trail')  # Example: Retrieve the trail value from the webhook data
    percent_per_trade = data.get('percent_per_trade')  # Example: Retrieve the % per trade value from the webhook data
    trade_size = data.get('trade_size')  # Example: Retrieve the specific trade size from the webhook data
    
    # Process the webhook data and perform your desired actions using the inputs
    # Extract necessary information, execute trades, etc.
    
    # Example: Print the received webhook data and the extracted inputs
    print("Received Webhook Data:")
    print(data)
    print("TP:", tp)
    print("SL:", sl)
    print("Trail:", trail)
    print("% per Trade:", percent_per_trade)
    print("Trade Size:", trade_size)
    
    # Place your Alpaca and KuCoin API-related code here
    # You can utilize the 'alpaca_api' and 'kucoin_api' instances for making API calls
    
    # Return a response to acknowledge the webhook
    return 'Webhook received successfully'

if __name__ == '__main__':
    app.run()
