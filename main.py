from scrapper import scrapper
from slackbot import buy_call

def main():
    print("At your service sir")
    stocks = ['IFCI:23','SBIN:248','ICICIBANK:250','INFY:930','JUBLFOOD:900']
    #stocks = ['INFY:930', 'JUBLFOOD:900']
    for index in range(len(stocks)):
        symbol,val= stocks[index].split(":")
        data = scrapper(symbol)
        current_value=data.split('"')
        final_value = current_value[1].replace(',','')
        if (float(final_value) < float(val)):
            buy_call(data)

if __name__ == "__main__":
    main()