import discord
from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Ping command registered for {self.bot.user}")

    @discord.slash_command(
        name="ping",
        description="Check the bot's ping"
    )
    async def ping(self, ctx):
        await ctx.defer()
        
        start_time = time.time()
        
        end_time = time.time()
        latency = round((end_time - start_time) * 1000)
        
        api_latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            color=discord.Color.green()
        )
        
        embed.add_field(name="Message Latency", value=f"``{latency}`` ms", inline=True)
        embed.add_field(name="API Latency", value=f"``{api_latency}`` ms", inline=True)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))