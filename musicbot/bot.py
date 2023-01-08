import os
import hikari
import lightbulb
from dotenv import load_dotenv
import music_plugin
load_dotenv()
bot = lightbulb.BotApp(os.getenv("DISCORD_TOKEN"))

@bot.listen()
async def starting_load_extensions(_: hikari.StartingEvent) -> None:
    """Load the music extension when Bot starts."""
    bot.load_extensions("music_plugin")


@bot.command()
@lightbulb.command("ping", "The bot's ping.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Typical Ping-Pong command"""
    await ctx.respond("Ping?")


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot.run()