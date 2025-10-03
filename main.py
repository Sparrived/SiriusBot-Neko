from ncatbot.core import BotClient

bot = BotClient()

def main():
    try:
        bot.run_frontend()
    except Exception:
        main()

if __name__ == "__main__":
    main()