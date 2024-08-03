from robocorp.tasks import task
from core import Scrapping


@task
def main():
    try:
        print("Starting bot...")
        bot = Scrapping()
        bot.run()

    except Exception as e:
        print(f"Error: {e}")
