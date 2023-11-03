import logging
import time
import util
from bot import Bot


def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)
    logging.info("Starting bot")

    settings = util.get_settings()
    app = settings['app']
    ticket = settings['ticket']
    # notification = settings['notification']
    logging.info("Retrieved data from json file")

    bot = Bot(ticket["magicLink"].strip(), app["browser"].strip())
    logging.info("Initialized a bot instance")

    time.sleep(20) # time to log in 
    logging.info("Starting to look for available tickets")
    while bot.find_available() is False:
        logging.warning("No tickets found, trying again...")
        bot.refresher()

    logging.info("Ticket(s) found!")

    logging.info("Reserving ticket")
    bot.reserve_ticket()

    logging.info("Waiting for checkout completion")
    time.sleep(900) # 15 minutes of buffer time to complete checkout

    logging.info("Closing bot")
    bot.quit()


if __name__ == "__main__":
    main()
