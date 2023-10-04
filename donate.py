import discord
import credits
from discord.ext import commands


client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())



class Menu (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Donate 1$ for ECO world", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.response.send_message("click here https://www.donationalerts.com/r/skropy")

@bot.command()
async def eco(ctx):
    await ctx.send("Спаси природу! https://i.imgur.com/oTxJgj5.png")
    view = Menu()
    await ctx.reply(view=view)

bot.run("TOKEN")