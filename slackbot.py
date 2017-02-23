import requests
import urllib



def buy_call(data):
    final_url ='https://slack.com/api/chat.postMessage?token=xoxp-144602751008-145388246788-145241612643-bea8b2229957eb06bfc3a89ead7686ca&channel=%23buy_call&text='+urllib.quote(data)+'&username=stock_analyst&xoxp-144602751008-145388246788-145241612643-bea8b2229957eb06bfc3a89ead7686ca&pretty=1'
    response = requests.get(final_url)
    print(response)