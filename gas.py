import requests

MIN_FEE=75

def get_bitcoin_gas_fee():
    # URL to get the latest Bitcoin fees information
    url = "https://mempool.space/api/v1/fees/recommended"

    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            fees_data = response.json()
            hour_fee = fees_data.get('hourFee', 90)
            return max(hour_fee, MIN_FEE)
        else:
            return "Error: Unable to fetch fees data. Status code: " + str(response.status_code)
    except Exception as e:
        return 90


if __name__ == '__main__':
    # Get the current Bitcoin gas fee
    current_bitcoin_gas_fee = get_bitcoin_gas_fee()
    print(current_bitcoin_gas_fee)

