from functions import *

def main():
    message = crypto_update(crypto_tickers)
    telegram_bot_sendtext(message, channel_id, 'Fg.png')      #1
    # telegram_bot_sendtext(message, chat_id, 'Fg.png')       #2

    ''' Use #1 for channel messages and #2 for chat messages'''

if __name__ == '__main__':
    main()
