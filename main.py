from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from termcolor import colored  # Importing the colored function

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
ASHRAF_USER_ID: Final = 856401001086582795  # Ashraf's specific Discord user ID

inte = Intents.default()
inte.message_content = True
client = Client(intents=inte)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print(colored('Message was empty because intents were not enabled probably', 'red'))
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(colored(str(e), 'red'))

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(colored(f'{client.user} is now running!', 'green'))

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is from Ashraf
    if message.author.id != ASHRAF_USER_ID:
        return  # Ignore messages from others

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(colored(f'[{channel}] {username}: "{user_message}"', 'blue'))
    
    await send_message(message, user_message)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
