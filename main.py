import discord
from discord.ext import commands
import os
import json

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or("!"), intents=intents)

        self.load_extensions()

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        
        try:
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
                status_text = config.get('Status', '')
                
            if status_text:
                await self.change_presence(activity=discord.Game(name=status_text))
                print(f"Status set to: {status_text}")
            else:
                print("No status found in config.json")
                
        except Exception as e:
            print(f"Failed to set status: {e}")

    def load_extensions(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                try:
                    self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded extension: {filename[:-3]}")
                except Exception as e:
                    print(f"Failed to load extension {filename[:-3]}: {e}")

bot = Bot()

if __name__ == "__main__":
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            TOKEN = config.get('Token', '')
        
        if not TOKEN:
            print("Warning: Token not found in config.json")
            
        bot.run(TOKEN)
    except FileNotFoundError:
        print("Error: config.json file not found")
    except json.JSONDecodeError:
        print("Error: config.json is not a valid JSON file")
    except Exception as e:
        print(f"An error occurred: {e}")