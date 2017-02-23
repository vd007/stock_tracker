import requests
import config
import urllib

def buy_call(data):
    final_url ='https://slack.com/api/chat.postMessage?token='+config.stock_analyst_slack_bot+'&channel=%23buy_call&text='+urllib.quote(data)+'&username=stock_analyst&'+config.stock_analyst_slack_bot+'&pretty=1'
    response = requests.get(final_url)
    print(response)