import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import discord, asyncio
from datetime import datetime
import psutil
import random

#------------------------------------------------ Basics ------------------------------------------------------#

# 📌 - Equinox's Community
# ⚙️ - Testing Server

# Load Token
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

# Client and Bot - Intents are permissions for the bot that are enabled based on the features necessary to run the bot
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(intents=discord.Intents.all(), command_prefix= "-eq")

# Removes the native help command
bot.remove_command('help')

#------------------------------------------------ Presets 🌟 ------------------------------------------------------#

# Members 
solstice_id = 995506191058862090
equinox_id = 882061427265921055
equinox_pfp_url = "https://cdn.discordapp.com/avatars/882061427265921055/d2dcf9ac35ef5a87677ce76d87811d4c.png?size=4096"
solstice_pfp_url = "https://cdn.discordapp.com/avatars/995506191058862090/4f777a1b7c6327c505077e57e3ebf709.png?size=4096"
server_pfp_url = "https://cdn.discordapp.com/icons/909605610641825842/a_1399013a2b1d2834ae0330271be122bb.gif"

# Utility Channels
solstice_log_channel_id = 1032086398179737670   # <------ SOLSITCE LOG CHANNEL ID HERE
basic_logs_channel_id = 909625580570431530   # <------ ORIGINAL LOGS CHANNEL ID HERE

# Warning Embed Basics
warning_embed_icon = "https://cdn.discordapp.com/attachments/935672317512650812/1154896305320112139/warning_2.png"
warning_embed_color = discord.Color.from_rgb(255,50,50)

# Generic Channels
general_channel_id = 909608455327850576
meme_channel_id = 909608850389336095
art_channel_id = 952307997395284008
bot_commands_channel_id = 909909981749465129
tww_chat_channel_id = 909608804860166216 
event_ideas_channel_id = 1019371787353600133
suggestions_channel_id = 909610657064837181
trading_help_channel_id = 1021585108077117501
tww_trading_channel_id =  916900301221539891
game_media_channel_id = 972536942208110633
media_channel_id = 928321092462977025
events_channel_id = 925796998903386214
qotd_channel_id = 946225117913055252

# Roles
unverified_role_id = 934701008494399490 # 📌 UNVERIFIED > 934701008494399490   ⚙️ UNVERIFIED > 995746177217736818
restricted_role_id = 1205576384903254116 # 📌 RESTRICTED > 1205576384903254116   ⚙️ RESTRICTED >
viewer_role_id = 1150880487976484895 # 📌 VIEWER > 1150880487976484895   ⚙️ VIEWER >
verified_role_id = 934514425933725798 # 📌 VERIFIED > 934514425933725798   ⚙️ VERIFIED > 995746177238712383
member_role_id = 909964707060940820 # 📌 MEMBER > 909964707060940820   ⚙️ MEMBER > 995746177238712384
noob_role_id = 909900628350881812 # 📌 NOOB > 909900628350881812   ⚙️ NOOB > 995746177238712385

event_pings_role_id = 923739335474438154
qotd_pings_role_id = 955992600396042291

event_winner_role_id = 925786099069095936 # 📌 925786099069095936   ⚙️ 995746177259671560
event_champion_role_id = 976565784727916564 # 📌 976565784727916564   ⚙️ 

#------------------------------------------------ Start Up ------------------------------------------------------#

@bot.event
async def on_ready():
    print("Bot is online")

    # Sync the slash commands to Discord (necessary)
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except:
        print(f'Failed to sync slash commands')

    # Activity Status
    while 1 != 2:
        await bot.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name = "Equinox on YouTube"))
        await asyncio.sleep(60)
        await bot.change_presence(status=discord.Status.online, activity = discord.Game(name = "🌵 The Wild West"))
        await asyncio.sleep(120)
 
# Playing -> activity = discord.Game(name="!help")
# Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")
# Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
# Watching -> activity = discord.Activity(type=discord.ActivityType.watching, name="!help")

#------------------------------------------------ Events ------------------------------------------------------#

# Channel specific responses to a message being sent
@bot.event
async def on_message(message):
# ART CHANNEL
    # React to every message sent in art 
    if message.channel.id == art_channel_id: 
        await bot.process_commands(message) # Commands fix
        artist_role = discord.utils.find(lambda r: r.name == 'Artist', message.guild.roles) # Set the artist role
        
        # Check to see if there is an attachment in the message                  
        if message.attachments:                                               
            # See if the author has the artist role
            if artist_role in message.author.roles:
                # Add the golden reactions
                await asyncio.sleep(1)
                await message.add_reaction("<:Gold_Number_3:1380258176108199966>")
                await message.add_reaction("<:Gold_Number_2:1380258168457658368>")
                await message.add_reaction("<:Gold_Number_1:1380258157296619550>")
            # Add the generic reactions if user doesn't have artist role
            else:
                await asyncio.sleep(1)
                await message.add_reaction("<:Number_3:1380257805252034670>")
                await message.add_reaction("<:Number_2:1380257792652476426>")
                await message.add_reaction("<:Number_1:1380257520245018675>")
            
        # Keep message and remove reactions if message from Solstice or Equinox or Needle bot
        elif message.author.id == solstice_id or message.author.id == equinox_id or message.author.id == 878399831238909952:
            # Delete message if from Needle with no warning pop up
            if message.author.id == 878399831238909952:
                await message.delete()
            else:
                await asyncio.sleep(2)
                await message.clear_reactions()

        # Delete message if it doesnt have attachments or from whitelisted users
        else:
            await message.delete()
            # Send warning embed
            channel = bot.get_channel(art_channel_id) # <------ ART CHANNEL ID HERE
            warning_embed = discord.Embed(colour = warning_embed_color)
            warning_embed.set_author(name = f"{message.author.name.capitalize()}, only send artwork in this channel.", icon_url = warning_embed_icon) 
            warning_msg = await channel.send(embed = warning_embed)
            await asyncio.sleep(10)
            await warning_msg.delete()

            # Helps from going to fast and bugging
            await asyncio.sleep(1)
            # Embed log for deleted message and author
            channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
            delete_embed = discord.Embed(title = "🎨 Art Message Deleted", colour = 0xe74c3c) # Color and Title, could add Description
            delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
            delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
            delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            delete_embed.timestamp = datetime.now() # Timestamp of when event occured
            await channel.send(embed = delete_embed)

# TWW-CHAT CHANNEL
    # W/L reactions for TWW-CHAT
    elif message.channel.id == tww_chat_channel_id:
        await bot.process_commands(message) # Commands fix
        # List of w/l phrases to look for
        wlist = ['w/l', 'w/f/l', 'w or l', 'wfl', 'w or f or l', 'win or lose', 'win or loss', 'win fair lose', 'win fair loss']
        # Add the w or l reactions (Phase 1)   
        for w in (wlist):
            if w in (message.content.lower()):
                await message.add_reaction("<:Win:1377108907998056448>") # <-- INSERT W EMOJI HERE ⭐ 
                await message.add_reaction("<:Fair:1377108906903470182>") # <-- INSERT F EMOJI HERE ⭐ 
                await message.add_reaction("<:Loss:1377108905955688479>") # <-- INSERT L EMOJI HERE ⭐ 
                #print("Running W/L Reaction (TWW-chat), Phase 2")

# EVENT IDEAS CHANNEL
    # Add thumbs up and thumbsdown to ideas posted in EVENT-IDEAS channel
    elif message.channel.id == event_ideas_channel_id:
        await bot.process_commands(message) # Commands fix
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        #print("Running Thumbs Up/Down Reaction (Event-Idea), Phase 1")

# SUGGESTIONS CHANNEL
    # Add thumbs up and thumbsdown to ideas posted in SUGGESTIONS channel
    elif message.channel.id == suggestions_channel_id: 
        await bot.process_commands(message) # Commands fix
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        #print("Running Thumbs Up/Down Reaction (Suggestions), Phase 1")

# TRADING-HELP CHANNEL
    # Add w/f/l reactions to every post in the TRADING-HELP channel
    elif message.channel.id == trading_help_channel_id:
        await bot.process_commands(message) # Commands fix
        # Generic Reactions
        await message.add_reaction("<:Win:1377108907998056448>") # <-- INSERT W EMOJI HERE ⭐ 
        await message.add_reaction("<:Fair:1377108906903470182>") # <-- INSERT F EMOJI HERE ⭐ 
        await message.add_reaction("<:Loss:1377108905955688479>") # <-- INSERT L EMOJI HERE ⭐ 
        #print("Running W/F/L Reaction (Trading-Help), Phase 1")

# TWW-TRADING CHANNEL
    # Remove all non-trades in the TWW-TRADING channel
    elif message.channel.id == tww_trading_channel_id:
        await bot.process_commands(message) # Commands fix
        # ALL THE VARIABLES
        # List of acceptable words that wont be blocked
        allowed = ["lf", "trading", "selling", "#", "dm", "trade", "sell", "looking", "buying", "sell", "buy", "look", "give", "offer", "offering", "giving", "body part", "gun part", "gun", "spitfire", "paterson", "henry", "lancaster", "guycot", "pistol", "carbine", "axegonne", "for", "lan", "pat", "want", "has", "spit", "gcc", "gc", "gcp", "ticket", "proto", "mlf", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"
                   "𝙡𝙛", "𝙩𝙧𝙖𝙙𝙞𝙣𝙜", "𝙨𝙚𝙡𝙡𝙞𝙣𝙜", "#", "𝙙𝙢", "𝙩𝙧𝙖𝙙𝙚", "𝙨𝙚𝙡𝙡", "𝙡𝙤𝙤𝙠𝙞𝙣𝙜", "𝙗𝙪𝙮𝙞𝙣𝙜", "𝙨𝙚𝙡𝙡", "𝙗𝙪𝙮", "𝙡𝙤𝙤𝙠", "𝙜𝙞𝙫𝙚", "𝙤𝙛𝙛𝙚𝙧", "𝙤𝙛𝙛𝙚𝙧𝙞𝙣𝙜", "𝙜𝙞𝙫𝙞𝙣𝙜", "𝙗𝙤𝙙𝙮 𝙥𝙖𝙧𝙩", "𝙜𝙪𝙣 𝙥𝙖𝙧𝙩", "𝙜𝙪𝙣", "𝙨𝙥𝙞𝙩𝙛𝙞𝙧𝙚", "𝙥𝙖𝙩𝙚𝙧𝙨𝙤𝙣", "𝙝𝙚𝙣𝙧𝙮", "𝙡𝙖𝙣𝙘𝙖𝙨𝙩𝙚𝙧", "𝙜𝙪𝙮𝙘𝙤𝙩", "𝙥𝙞𝙨𝙩𝙤𝙡", "𝙘𝙖𝙧𝙗𝙞𝙣𝙚", "𝙖𝙭𝙚𝙜𝙤𝙣𝙣𝙚", "𝙛𝙤𝙧", "𝙡𝙖𝙣", "𝙥𝙖𝙩", "𝙬𝙖𝙣𝙩", "𝙝𝙖𝙨", "𝙨𝙥𝙞𝙩", "𝙜𝙘𝙘", "𝙜𝙘", "𝙜𝙘𝙥", "𝙩𝙞𝙘𝙠𝙚𝙩", "𝙥𝙧𝙤𝙩𝙤", "𝙢𝙡𝙛", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"
                   "𝗹𝗳", "𝘁𝗿𝗮𝗱𝗶𝗻𝗴", "𝘀𝗲𝗹𝗹𝗶𝗻𝗴", "#", "𝗱𝗺", "𝘁𝗿𝗮𝗱𝗲", "𝘀𝗲𝗹𝗹", "𝗹𝗼𝗼𝗸𝗶𝗻𝗴", "𝗯𝘂𝘆𝗶𝗻𝗴", "𝘀𝗲𝗹𝗹", "𝗯𝘂𝘆", "𝗹𝗼𝗼𝗸", "𝗴𝗶𝘃𝗲", "𝗼𝗳𝗳𝗲𝗿", "𝗼𝗳𝗳𝗲𝗿𝗶𝗻𝗴", "𝗴𝗶𝘃𝗶𝗻𝗴", "𝗯𝗼𝗱𝘆 𝗽𝗮𝗿𝘁", "𝗴𝘂𝗻 𝗽𝗮𝗿𝘁", "𝗴𝘂𝗻", "𝘀𝗽𝗶𝘁𝗳𝗶𝗿𝗲", "𝗽𝗮𝘁𝗲𝗿𝘀𝗼𝗻", "𝗵𝗲𝗻𝗿𝘆", "𝗹𝗮𝗻𝗰𝗮𝘀𝘁𝗲𝗿", "𝗴𝘂𝘆𝗰𝗼𝘁", "𝗽𝗶𝘀𝘁𝗼𝗹", "𝗰𝗮𝗿𝗯𝗶𝗻𝗲", "𝗮𝘅𝗲𝗴𝗼𝗻𝗻𝗲", "𝗳𝗼𝗿", "𝗹𝗮𝗻", "𝗽𝗮𝘁", "𝘄𝗮𝗻𝘁", "𝗵𝗮𝘀", "𝘀𝗽𝗶𝘁", "𝗴𝗰𝗰", "𝗴𝗰", "𝗴𝗰𝗽", "𝘁𝗶𝗰𝗸𝗲𝘁", "𝗽𝗿𝗼𝘁𝗼", "𝗺𝗹𝗳", "𝟭𝟬", "𝟵", "𝟴", "𝟳", "𝟲", "𝟱", "𝟰", "𝟯", "𝟮", "𝟭"
                   "𝘭𝘧", "𝘵𝘳𝘢𝘥𝘪𝘯𝘨", "𝘴𝘦𝘭𝘭𝘪𝘯𝘨", "#", "𝘥𝘮", "𝘵𝘳𝘢𝘥𝘦", "𝘴𝘦𝘭𝘭", "𝘭𝘰𝘰𝘬𝘪𝘯𝘨", "𝘣𝘶𝘺𝘪𝘯𝘨", "𝘴𝘦𝘭𝘭", "𝘣𝘶𝘺", "𝘭𝘰𝘰𝘬", "𝘨𝘪𝘷𝘦", "𝘰𝘧𝘧𝘦𝘳", "𝘰𝘧𝘧𝘦𝘳𝘪𝘯𝘨", "𝘨𝘪𝘷𝘪𝘯𝘨", "𝘣𝘰𝘥𝘺 𝘱𝘢𝘳𝘵", "𝘨𝘶𝘯 𝘱𝘢𝘳𝘵", "𝘨𝘶𝘯", "𝘴𝘱𝘪𝘵𝘧𝘪𝘳𝘦", "𝘱𝘢𝘵𝘦𝘳𝘴𝘰𝘯", "𝘩𝘦𝘯𝘳𝘺", "𝘭𝘢𝘯𝘤𝘢𝘴𝘵𝘦𝘳", "𝘨𝘶𝘺𝘤𝘰𝘵", "𝘱𝘪𝘴𝘵𝘰𝘭", "𝘤𝘢𝘳𝘣𝘪𝘯𝘦", "𝘢𝘹𝘦𝘨𝘰𝘯𝘯𝘦", "𝘧𝘰𝘳", "𝘭𝘢𝘯", "𝘱𝘢𝘵", "𝘸𝘢𝘯𝘵", "𝘩𝘢𝘴", "𝘴𝘱𝘪𝘵", "𝘨𝘤𝘤", "𝘨𝘤", "𝘨𝘤𝘱", "𝘵𝘪𝘤𝘬𝘦𝘵", "𝘱𝘳𝘰𝘵𝘰", "𝘮𝘭𝘧", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"
                   "𝗅𝖿", "𝗍𝗋𝖺𝖽𝗂𝗇𝗀", "𝗌𝖾𝗅𝗅𝗂𝗇𝗀", "#", "𝖽𝗆", "𝗍𝗋𝖺𝖽𝖾", "𝗌𝖾𝗅𝗅", "𝗅𝗈𝗈𝗄𝗂𝗇𝗀", "𝖻𝗎𝗒𝗂𝗇𝗀", "𝗌𝖾𝗅𝗅", "𝖻𝗎𝗒", "𝗅𝗈𝗈𝗄", "𝗀𝗂𝗏𝖾", "𝗈𝖿𝖿𝖾𝗋", "𝗈𝖿𝖿𝖾𝗋𝗂𝗇𝗀", "𝗀𝗂𝗏𝗂𝗇𝗀", "𝖻𝗈𝖽𝗒 𝗉𝖺𝗋𝗍", "𝗀𝗎𝗇 𝗉𝖺𝗋𝗍", "𝗀𝗎𝗇", "𝗌𝗉𝗂𝗍𝖿𝗂𝗋𝖾", "𝗉𝖺𝗍𝖾𝗋𝗌𝗈𝗇", "𝗁𝖾𝗇𝗋𝗒", "𝗅𝖺𝗇𝖼𝖺𝗌𝗍𝖾𝗋", "𝗀𝗎𝗒𝖼𝗈𝗍", "𝗉𝗂𝗌𝗍𝗈𝗅", "𝖼𝖺𝗋𝖻𝗂𝗇𝖾", "𝖺𝗑𝖾𝗀𝗈𝗇𝗇𝖾", "𝖿𝗈𝗋", "𝗅𝖺𝗇", "𝗉𝖺𝗍", "𝗐𝖺𝗇𝗍", "𝗁𝖺𝗌", "𝗌𝗉𝗂𝗍", "𝗀𝖼𝖼", "𝗀𝖼", "𝗀𝖼𝗉", "𝗍𝗂𝖼𝗄𝖾𝗍", "𝗉𝗋𝗈𝗍𝗈", "𝗆𝗅𝖿", "𝟣𝟢", "𝟫", "𝟪", "𝟩", "𝟨", "𝟧", "𝟦", "𝟥", "𝟤", "𝟣"
                   "𝚕𝚏", "𝚝𝚛𝚊𝚍𝚒𝚗𝚐", "𝚜𝚎𝚕𝚕𝚒𝚗𝚐", "#", "𝚍𝚖", "𝚝𝚛𝚊𝚍𝚎", "𝚜𝚎𝚕𝚕", "𝚕𝚘𝚘𝚔𝚒𝚗𝚐", "𝚋𝚞𝚢𝚒𝚗𝚐", "𝚜𝚎𝚕𝚕", "𝚋𝚞𝚢", "𝚕𝚘𝚘𝚔", "𝚐𝚒𝚟𝚎", "𝚘𝚏𝚏𝚎𝚛", "𝚘𝚏𝚏𝚎𝚛𝚒𝚗𝚐", "𝚐𝚒𝚟𝚒𝚗𝚐", "𝚋𝚘𝚍𝚢 𝚙𝚊𝚛𝚝", "𝚐𝚞𝚗 𝚙𝚊𝚛𝚝", "𝚐𝚞𝚗", "𝚜𝚙𝚒𝚝𝚏𝚒𝚛𝚎", "𝚙𝚊𝚝𝚎𝚛𝚜𝚘𝚗", "𝚑𝚎𝚗𝚛𝚢", "𝚕𝚊𝚗𝚌𝚊𝚜𝚝𝚎𝚛", "𝚐𝚞𝚢𝚌𝚘𝚝", "𝚙𝚒𝚜𝚝𝚘𝚕", "𝚌𝚊𝚛𝚋𝚒𝚗𝚎", "𝚊𝚡𝚎𝚐𝚘𝚗𝚗𝚎", "𝚏𝚘𝚛", "𝚕𝚊𝚗", "𝚙𝚊𝚝", "𝚠𝚊𝚗𝚝", "𝚑𝚊𝚜", "𝚜𝚙𝚒𝚝", "𝚐𝚌𝚌", "𝚐𝚌", "𝚐𝚌𝚙", "𝚝𝚒𝚌𝚔𝚎𝚝", "𝚙𝚛𝚘𝚝𝚘", "𝚖𝚕𝚏", "𝟷𝟶", "𝟿", "𝟾", "𝟽", "𝟼", "𝟻", "𝟺", "𝟹", "𝟸", "𝟷"
                   "ʟꜰ", "ᴛʀᴀᴅɪɴɢ", "ꜱᴇʟʟɪɴɢ", "#", "ᴅᴍ", "ᴛʀᴀᴅᴇ", "ꜱᴇʟʟ", "ʟᴏᴏᴋɪɴɢ", "ʙᴜʏɪɴɢ", "ꜱᴇʟʟ", "ʙᴜʏ", "ʟᴏᴏᴋ", "ɢɪᴠᴇ", "ᴏꜰꜰᴇʀ", "ᴏꜰꜰᴇʀɪɴɢ", "ɢɪᴠɪɴɢ", "ʙᴏᴅʏ ᴘᴀʀᴛ", "ɢᴜɴ ᴘᴀʀᴛ", "ɢᴜɴ", "ꜱᴘɪᴛꜰɪʀᴇ", "ᴘᴀᴛᴇʀꜱᴏɴ", "ʜᴇɴʀʏ", "ʟᴀɴᴄᴀꜱᴛᴇʀ", "ɢᴜʏᴄᴏᴛ", "ᴘɪꜱᴛᴏʟ", "ᴄᴀʀʙɪɴᴇ", "ᴀxᴇɢᴏɴɴᴇ", "ꜰᴏʀ", "ʟᴀɴ", "ᴘᴀᴛ", "ᴡᴀɴᴛ", "ʜᴀꜱ", "ꜱᴘɪᴛ", "ɢᴄᴄ", "ɢᴄ", "ɢᴄᴘ", "ᴛɪᴄᴋᴇᴛ", "ᴘʀᴏᴛᴏ", "ᴍʟꜰ", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        # List of non-acceptable words that will be blocked
        blacklisted = ["# "]
    
        # List of member's ids that have sent messages in the channel
        author_ids = [msg.author.id async for msg in message.channel.history(limit=5)] # Shorter author history limit
        author_ids2 = [msg.author.id async for msg in message.channel.history(limit=10)] # Larger author history limit

        # Make a list of all the recent messages sent in the channel
        channel_msg_contents = [message.content.lower() async for message in message.channel.history(limit=5)] # Channel message history limit
        recent_msg_contents = [message.content.lower() async for message in message.channel.history(limit=1)] # Most recent message sent in channel

        # Make a string of the recent message and the msg_contents so they can compare
        msg_history = (str(channel_msg_contents).lower()).replace(" ", "")
        msg_history_popzero = (str(channel_msg_contents.pop(0)).lower()).replace(" ", "") # msg_history but remove the first element (aka: recent_msg)
        recent_msg = (str(message.content).lower()).replace(" ", "")

        # Count how many times the message.author.id shows up in each author list
        author_id_count_small = author_ids.count(message.author.id)
        author_id_count_large = author_ids2.count(message.author.id)

        # Set neccesary default channels
        solstice_log_channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
        tww_trading_channel = bot.get_channel(tww_trading_channel_id) # <------ TRADING CHANNEL ID HERE

        # Set the max amount of lines allowed (block walls of text from being sent)
        max_lines = 45
######
        # Message is from solstice (stop infi loop) or equinox so pass
        if message.author.id == solstice_id or message.author.id == equinox_id:
            await bot.process_commands(message) # Commands fix
######
        # Remove any messages with blacklisted words in it
        elif any(word in message.content.lower() for word in blacklisted):
            await message.delete()

            # Embed log for deleted message and author
            delete_embed = discord.Embed(title = "⚖️ Large Text Message Deleted", colour = 0xe74c3c) # Color and Title, could add Description
            delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
            delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
            delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            delete_embed.timestamp = datetime.now() # Timestamp of when event occured
            await solstice_log_channel.send(embed = delete_embed)

            # Send warning embed
            warning_embed = discord.Embed(colour = warning_embed_color)
            warning_embed.set_author(name = f"{message.author.name.capitalize()}, do not post large text in this channel.", icon_url = warning_embed_icon) 
            warning_msg = await tww_trading_channel.send(embed = warning_embed)
            await asyncio.sleep(10)
            await warning_msg.delete()
######
        # Check to see if its allowed and continue on with other factors
        elif any(word in message.content.lower() for word in allowed):

            # Count how many lines are in the message
            newlines = message.content.split("\n")
            line_counter = 0
            for line in newlines:
                if line:
                    line_counter += 1
            # Delete if more than max amount of new lines is in the message
            if line_counter > max_lines:
                # Delete the large post
                print("User spammed another large message trade")
                await message.delete()

                # Embed log for deleted message and author that has sent too many messages
                delete_embed = discord.Embed(title = "⚖️ Large Text Wall Deleted", colour = 0xe74c3c) # Color and Title, could add Description
                delete_embed.add_field(name = "Lines Sent / Lines Allowed:", value = (f"{line_counter} / {max_lines}")) # Show the deleted message
                delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
                delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
                delete_embed.timestamp = datetime.now() # Timestamp of when event occured
                await solstice_log_channel.send(embed = delete_embed)
                
                # Send warning embed
                warning_embed = discord.Embed(colour = warning_embed_color)
                warning_embed.set_author(name = f"{message.author.name.capitalize()}, do post massive walls of text. The maximum amount of lines is {max_lines}. Your message had {line_counter}.", icon_url = warning_embed_icon) 
                warning_msg = await tww_trading_channel.send(embed = warning_embed)
                await asyncio.sleep(10)
                await warning_msg.delete()

            # Stop people from spamming the same exact trade
            elif message.author.id in author_ids:

                # Same author has more than x messages in the larger list of recent messages
                if author_id_count_large > 6:
                    print("User sent too many messages recently")
                    await message.delete()

                    # Embed log for deleted message and author that has sent too many messages
                    delete_embed = discord.Embed(title = "⚖️ Member's Trade Post Deleted", colour = 0xe74c3c) # Color and Title, could add Description
                    delete_embed.add_field(name = "Information", value = (f"User has sent over 60% of recent messages in trading channel")) # Why the message was deleted
                    delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
                    delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
                    delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
                    delete_embed.timestamp = datetime.now() # Timestamp of when event occured
                    await solstice_log_channel.send(embed = delete_embed)

                    # Send warning embed
                    warning_embed = discord.Embed(colour = warning_embed_color)
                    warning_embed.set_author(name = f"{message.author.name.capitalize()}, you are posting too many trades. Please wait awhile before posting again.", icon_url = warning_embed_icon) 
                    warning_msg = await tww_trading_channel.send(embed = warning_embed)
                    await asyncio.sleep(10)
                    await warning_msg.delete()

                # Same author posted the same message more than once
                elif any(msg in recent_msg_contents for msg in channel_msg_contents):
                    print("User has sent the same exact message")
                    await message.delete()
                    
                    # Embed log for deleted message and author
                    delete_embed = discord.Embed(title = "⚖️ Spammed Trade Deleted", colour = 0xe74c3c) # Color and Title, could add Description
                    delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
                    delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
                    delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
                    delete_embed.timestamp = datetime.now() # Timestamp of when event occured
                    await solstice_log_channel.send(embed = delete_embed)

                    # Send warning embed
                    warning_embed = discord.Embed(colour = warning_embed_color)
                    warning_embed.set_author(name = f"{message.author.name.capitalize()}, please do not spam the same trade when the chat is inactive.", icon_url = warning_embed_icon) 
                    warning_msg = await tww_trading_channel.send(embed = warning_embed)
                    await asyncio.sleep(10)
                    await warning_msg.delete()
                    
                else:
                    pass
            else:
                pass
######
        # Message has an attachment (trading posts thru pic) and didn't run thru any of the other errors, so pass
        elif message.attachments:
            await bot.process_commands(message) # Commands fix
######
        # Delete the message if its not allowed and not blacklisted + send warning
        else:
            await message.delete()

            # Embed log for deleted message and author
            delete_embed = discord.Embed(title = "⚖️ Trading Message Deleted", colour = 0xe74c3c) # Color and Title, could add Description
            delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
            delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
            delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            delete_embed.timestamp = datetime.now() # Timestamp of when event occured
            await solstice_log_channel.send(embed = delete_embed)
            
            # Send warning embed
            warning_embed = discord.Embed(colour = warning_embed_color)
            warning_embed.set_author(name = f"{message.author.name.capitalize()}, only send trades in this channel.", icon_url = warning_embed_icon) 
            warning_msg = await tww_trading_channel.send(embed = warning_embed)
            await asyncio.sleep(10)
            await warning_msg.delete()

# GAME-MEDIA CHANNEL
    # Remove all non-youtube videos in the GAME-MEDIA channel
    elif message.channel.id == game_media_channel_id:
        await bot.process_commands(message) # Commands fix
        # list of acceptable links that wont be blocked
        allowed = ["https://www.youtube.com", "https://youtu.be", "https://youtube.com", "https://www.twitch.tv"]
        
        # Message matches with list meaning it's a legit YT link
        if any(word in message.content.lower() for word in allowed):
            await bot.process_commands(message) # Commands fix

        # Message is from Solstice or Equinox, so allow it
        elif message.author.id == solstice_id or message.author.id == equinox_id:
            await bot.process_commands(message) # Commands fix

        # Delete the message if its not allowed + send warning
        else:
            await message.delete()
            # Send warning embed
            channel = bot.get_channel(game_media_channel_id) # <------ GAME MEDIA CHANNEL ID HERE
            warning_embed = discord.Embed(colour = warning_embed_color)
            warning_embed.set_author(name = f"{message.author.name.capitalize()}, only post video/stream links in this channel.", icon_url = warning_embed_icon) 
            warning_msg = await channel.send(embed = warning_embed)
            await asyncio.sleep(10)
            await warning_msg.delete()

            # Embed log for deleted message and author
            channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
            delete_embed = discord.Embed(title = "<:YouTube:1374526830995832853> <#972536942208110633> Message Deleted", colour = 0xe74c3c) # Color and Title, could add Description
            delete_embed.add_field(name = "Message:", value = (f"{message.content}")) # Show the deleted message
            delete_embed.add_field(name = "Author:", value = f"{message.author}", inline=False) # Show the message author
            delete_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            delete_embed.timestamp = datetime.now() # Timestamp of when event occured
            await channel.send(embed = delete_embed)

# EVENTS CHANNEL
    # Add trophy reaction to every post in the events channel from Solstice bot (for event pings embed)
    elif message.channel.id == events_channel_id: # <------ EVENTS CHANNEL ID HERE
        await bot.process_commands(message) # Commands fix
        # Message is in event channel, sent by Solstice, and it's an embed...
        if message.author.id == solstice_id and message.embeds:  
            await message.add_reaction("🏆") # Needed for reaction role embed
            #print("Running Event Pings Reaction (Events), Phase 1")

# QOTD CHANNEL
    # Add microphone reaction to every post in the qotd channel from Solstice bot (for qotd pings embed)
    elif message.channel.id == qotd_channel_id: # <------ QOTD CHANNEL ID HERE
        await bot.process_commands(message) # Commands fix
        # Message is in qotd channel, sent by Solstice, and it's an embed...
        if message.author.id == solstice_id and message.embeds:  
            await message.add_reaction("🎙️") # Needed for reaction role embed
            #print("Running QOTD Pings Reaction (QOTD), Phase 1")

# DIRECT MESSAGES TO BOT (DMS)
    # Redirect all dms sent to bot to discord channel
    elif isinstance(message.channel, discord.DMChannel):
        await bot.process_commands(message) # Commands fix
        channel = bot.get_channel(1133886027057090560) # <------ BOT MAILBOX CHANNEL ID HERE ⭐
        log_author_pfp = message.author.display_avatar # author's pfp

        # Ignore if Solstice is the one sending the DM
        if message.author.id == solstice_id:
            pass

        else:
            # Send the user ID as a normal message (easier to copy and paste on mobile)
            await channel.send(f"{message.author.id}")

            # Embed for messages received by Solstice
            mail_embed = discord.Embed(title = "📮 Dm Received", colour = discord.Color.from_rgb(226,226,226)) # Title, Color
            mail_embed.add_field(name = f"DM received from {message.author.name}", value = (f"{message.content}")) # Show the content of the DM with author's name
            mail_embed.set_thumbnail(url=f"{log_author_pfp}") # Big Image in top right of embed
            mail_embed.set_footer(text=f"ID: {message.author.id}") # User's ID in footer
            mail_embed.timestamp = datetime.now() # Timestamp of when event occured

            # Set gif to empty until it confirms there was a gif in the message
            gif_content = "empty"
            # Message contains a gif
            if "https://tenor.com/view/" in (f"{message.content}"):
                gif_content = (f"{message.content}")

            # Attachments fix for received embed
            if message.attachments:
                if len(message.attachments) == 1:
                    # Check to see if it can be added to embed (image section)
                    if message.attachments[0].url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                        mail_embed.set_image(url=message.attachments[0].url)
                    # Wrong file format for embed
                    else:
                        mail_embed.add_field(name="", value = f"Attachment: \n{message.attachments[0].url}", inline = False) # Show any attachments

                # Up to 5 attachments logged
                # More than 1 image attched to message
                elif len(message.attachments) == 2:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}", inline = False) # Show any attachments
                # More than 2 images attched to message
                elif len(message.attachments) == 3:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}", inline = False) # Show any attachments
                # More than 3 images attched to message
                elif len(message.attachments) == 4:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}", inline = False) # Show any attachments
                # More than 4 images attched to message
                elif len(message.attachments) == 5:
                    mail_embed.add_field(name = "", value = f"Attachments: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}\n5. {message.attachments[4].url}", inline = False) # Show any attachments
                # More than 5 images attched to message
                elif len(message.attachments) > 5:
                    mail_embed.add_field(name = "", value = f"Attachments Overload: \n1. {message.attachments[0].url}\n2. {message.attachments[1].url}\n3. {message.attachments[2].url}\n4. {message.attachments[3].url}\n5. {message.attachments[4].url}", inline = False) # Show any attachments

            # Send the embed DM along with the gif (if there is one)
            await channel.send(embed = mail_embed)
            if gif_content != "empty":
                await channel.send(gif_content)

# END OF SECTION
    else:
        await bot.process_commands(message) # Commands fix

# Event pings reaction added in Events & QOTD channel, Add Event Pings, goes with -eqrolesad
@bot.event
async def on_raw_reaction_add(payload):
    # Payloads / Variables
    channel_id = payload.channel_id
    user_id = payload.user_id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    # Ping Roles
    eventpings_role = discord.utils.get(member.guild.roles, id=event_pings_role_id)
    qotdpings_role = discord.utils.get(member.guild.roles, id=qotd_pings_role_id)
    # Channels
    log_channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
    # If Solstice is the one adding the reaction, ignore it
    if user_id == solstice_id:
        return
    
    # Reaction channel is Event Channel 
    if channel_id == events_channel_id:
        # The emoji that has been reacted to is
        if payload.emoji.name == "🏆":
            await member.add_roles(eventpings_role) # Add the role
            print("Running Reaction Roles, Added Event Pings")

            # Send add message to logs channel
            log_embed = discord.Embed(title = "🔔 Event Pings", colour = 0x2ecc71) # Color, Title, could add Description
            log_embed.add_field(name = "Information:", value = (f"{member.mention} has been added to Event Pings")) # Show the Event Pings role was removed
            log_embed.set_footer(text=f"ID: {user_id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)

    # Reaction channel is QOTD Channel 
    if channel_id == qotd_channel_id:
        # The emoji that has been reacted to is
        if payload.emoji.name == "🎙️":
            await member.add_roles(qotdpings_role) # Add the role
            print("Running Reaction Roles, Added QOTD Pings")

            # Send add message to logs channel
            log_embed = discord.Embed(title = "🔔 QOTD Pings", colour = 0x2ecc71) # Color, Title, could add Description
            log_embed.add_field(name = "Information:", value = (f"{member.mention} has been added to QOTD Pings")) # Show the Event Pings role was removed
            log_embed.set_footer(text=f"ID: {user_id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)
    else:
        return
    
# Event pings reaction removed in Events & QOTD channel, Remove Event Pings, goes with -eqrolesad
@bot.event
async def on_raw_reaction_remove(payload):
    # Payloads / Variables
    channel_id = payload.channel_id
    user_id = payload.user_id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    # Ping Roles
    eventpings_role = discord.utils.get(member.guild.roles, id=event_pings_role_id)
    qotdpings_role = discord.utils.get(member.guild.roles, id=qotd_pings_role_id)
    # Channels
    log_channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
    # If Solstice is the one adding the reaction, ignore it
    if user_id == solstice_id:
        return
    
    # Reaction channel is Event Channel 
    if channel_id == events_channel_id:
        # The emoji that has been reacted to is
        if payload.emoji.name == "🏆":
            await member.remove_roles(eventpings_role) # Remove the role
            print("Running Reaction Roles, Removed Event Pings")

            # Send removed message to logs channel
            log_embed = discord.Embed(title = "🔔 Event Pings", colour = 0xe74c3c) # Color, Title, could add Description
            log_embed.add_field(name = "Information:", value = (f"{member.mention} has been removed from Event Pings")) # Show the Event Pings role was removed
            log_embed.set_footer(text=f"ID: {user_id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)

    # Reaction channel is QOTD Channel 
    if channel_id == qotd_channel_id:
        # The emoji that has been reacted to is
        if payload.emoji.name == "🎙️":
            await member.remove_roles(qotdpings_role) # Remove the role
            print("Running Reaction Roles, Removed QOTD Pings")

            # Send removed message to logs channel
            log_embed = discord.Embed(title = "🔔 QOTD Pings", colour = 0xe74c3c) # Color, Title, could add Description
            log_embed.add_field(name = "Information:", value = (f"{member.mention} has been removed from QOTD Pings")) # Show the Event Pings role was removed
            log_embed.set_footer(text=f"ID: {user_id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)
    else:
        return

#------------------------------------------------Logging------------------------------------------------------#

# Log Solstice Command Usage
    # 📌 1032086398179737670
    # ⚙️ 995746177649758228

# Logs every Solstice commands used
@bot.event
async def on_command(ctx):
    # Channel
    log_channel = bot.get_channel(solstice_log_channel_id) # Channel to send the logs to
    log_msg_sent_channel = ctx.channel.id # Channel command was sent in
    # Author
    log_author_id = ctx.author.id # Command author's ID
    log_author = ctx.author # Command author's name
    log_author_pfp = ctx.author.display_avatar # Command author's pfp
    # Command
    log_command = ctx.command # Command used, only says the command name 'winner'
    log_msg = ctx.message.content # Full command message

    # Solstice Command Usage Embed Logging
    log_embed = discord.Embed(title = "Command usage logged by Solstice", colour = 0xf1c40f) # Title and Color, could add Description
    log_embed.set_author(name = f"{log_author}", icon_url = str(log_author_pfp)) # Author's Name and Pfp at top of embed
    log_embed.set_thumbnail(url=f"{log_author_pfp}") # Big Image in top right of embed
    log_embed.add_field(name = "Command Name and Info:", value = f"The **{log_command}** command was used in <#{log_msg_sent_channel}>") # Log the command and channel it was used
    #log_embed.add_field(name = "This is field 2", value = "This field is just a inline", inline=True)
    log_embed.add_field(name = "Full Command:", value = f"{log_msg}", inline=False) # Log the full command that was used then deleted
    log_embed.set_footer(text=f"Author ID: {log_author_id}") # Author's ID in footer
    log_embed.timestamp = datetime.now() # Timestamp of when event occured
    await log_channel.send(embed = log_embed)  

# Notice when a new role is given to a user
@bot.event
async def on_member_update(before, after):
    log_channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE

    if len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)

        # Event Winner role given log
        if new_role.name == 'Event Winner':
            log_embed = discord.Embed(title = "🏆 Event Winner", colour = 0x2ecc71) # Color, could add Description and Title
            log_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Event Winner role")) # Show the Event Winner role was given
            log_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)

        # Event Champion role given log
        elif new_role.name == 'Event Champion':
            log_embed = discord.Embed(title = "<:Champion_trophy:1380260555448909954> Event Winner", colour = 0x2ecc71) # Color, could add Description and Title
            log_embed.add_field(name = "Information:", value = (f"{after.mention} has received the Event Champion role")) # Show the Event Champion role was given
            log_embed.set_footer(text=f"ID: {after.id}") # User's ID in footer
            log_embed.timestamp = datetime.now() # Timestamp of when event occured
            await log_channel.send(embed = log_embed)

#------------------------------------------------ Commands ------------------------------------------------------#

# Event Winner give role command -eqwinner <user>
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Event Manager')
# Cooldown settings, 4 uses in 43200 seconds (12 hours)
@commands.cooldown(4, 43200, commands.BucketType.guild)
async def winner(ctx, user: discord.Member):
    print("Running Commands, Event Winner role")
    role = discord.utils.get(ctx.message.guild.roles, id=event_winner_role_id) # <------ EVENT WINNER ROLE ID HERE
    channel = bot.get_channel(events_channel_id)
    # Already has the event winner role
    if role in user.roles:
        await ctx.message.delete()
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = f"{user.name.capitalize()} already has the Event Winner role.", icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()
        print("Running Commands, Event Winner role, Phase 1")
    # Doesn't already have the event winner role
    if role not in user.roles:
        await ctx.message.delete()
        await user.add_roles(role)
        await asyncio.sleep(1)
        await channel.send(f"**🏆 Congrats on winning the event {user.mention}. You have received the Event Winner title!**")
        print("Running Commands, Event Winner role, Phase 2 (In Event Channel)")

# Event Champion give role command -eqchamp <user>
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Event Manager')
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def champ(ctx, user: discord.Member):
    print("Running Commands, Event Champion role")
    role = discord.utils.get(ctx.message.guild.roles, id=event_champion_role_id) # <------ EVENT CHAMPION ROLE ID HERE
    channel = bot.get_channel(events_channel_id)
    # Already has the event champion role
    if role in user.roles:
        await ctx.message.delete()
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = f"{user.name.capitalize()} already has the Event Champion role.", icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()
        print("Running Commands, Event Champion role, Phase 1")
    # Doesn't already have the event champion role
    if role not in user.roles:
        await ctx.message.delete()
        await user.add_roles(role)
        await asyncio.sleep(1)
        await channel.send(f"**<:Champion_trophy:1380260555448909954> Congrats on winning 3 events {user.mention}! You have received the Event Champion title.**")
        print("Running Commands, Event Champion role, Phase 2 (In Event Channel)") 

# Reset the command author's nickname -eqreset
@bot.command(pass_context=True)
@commands.has_role('Member')
# Cooldown settings, 2 uses in 10 seconds
@commands.cooldown(2, 10, commands.BucketType.user)
async def reset(ctx):
    await ctx.message.delete()
    try:
        await ctx.message.author.edit(nick=None) # Reset their nickname
        # Confirmation
        s_sent = await ctx.send(f"**Nickname Reset!**")
        await asyncio.sleep(5)
        await s_sent.delete()
    # Doesn't have perms to change this member's nickname
    except:
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = f"{ctx.author.name.capitalize()}, I'm unable to change your nickname.", icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()

# Purge command for primarly mods, but anyone with manage message perms -eqpurge
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
# Cooldown settings, 1 uses every 45 seconds
@commands.cooldown(1, 45, commands.BucketType.user)
async def purge(ctx, member: discord.Member, limit: int):
    await ctx.message.delete()
    msg = []
    deleted_msgs = []
    maximum = 35
    attempted = limit
    # Set limit to the maximum variable
    if limit > maximum:
        attempted = int(limit)
        limit = maximum
    # Delete the messages
    async for message in ctx.channel.history():
        if len(msg) == limit:
            break
        if message.author == member:
            msg.append(message)
            deleted_msgs.append(str(message.content))
    await ctx.channel.delete_messages(msg)
    await asyncio.sleep(1)

    # Send the logging info embed
    log_channel = bot.get_channel(solstice_log_channel_id) # <------ SOLSTICE LOG CHANNEL ID HERE
    logs_channel = bot.get_channel(basic_logs_channel_id) # <------ NORMAL LOG CHANNEL ID HERE 
    log_embed = discord.Embed(title = "⚠️ Purge Command", colour = 0x2ecc71) # Title and color
    log_embed.add_field(name = "Information:", value = (f"{ctx.author.mention} has used the purge command in <#{ctx.channel.id}>\nAttempted Amount: **{attempted}**\nUsed Amount: **{limit}**\nMember: **{member}**"))
    log_embed.set_footer(text=f"ID: {member.id}") # Member + ID in footer
    log_embed.timestamp = datetime.now() # Timestamp of when event occured
    await log_channel.send(embed = log_embed)
    await logs_channel.send(embed = log_embed)
    
    deleted_msgs == deleted_msgs.reverse()
    # Log the messages deleted
    dms_embed = discord.Embed(title = "🚫 Messages Deleted", colour = 0xe74c3c) # Title and color
    dms_embed.add_field(name = f'**{ctx.author} deleted {limit} messages from {member} in <#{ctx.channel.id}>**', value = '\n'.join(deleted_msgs))
    dms_embed.set_footer(text=f"ID: {member.id}") # Author + ID in footer
    dms_embed.timestamp = datetime.now() # Timestamp of when event occured
    await log_channel.send(embed = dms_embed)
    await logs_channel.send(embed = dms_embed)

    # Success confirmation
    s_sent = await ctx.send(f"**Purged {limit} messages from {member.name.capitalize()}**")
    await asyncio.sleep(5)
    await s_sent.delete()

# Custom fake level remove command for Omega Mods -eqrmvlvl <user> <num> 
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Omega Moderator')
# Cooldown settings, 1 uses every 5 seconds
@commands.cooldown(1, 5, commands.BucketType.user)
async def rmvlvl(ctx, user: discord.Member, *args):
    if args == 1:
        level = " level "
    else:
        level = " levels "
    await asyncio.sleep(.5)
    message = await ctx.reply("<a:spin_loading:1380261482733768795> " + f'Removing ' + f'`{"{}".format(" ".join(args))}`' + level + f"from {user.mention}")
    await asyncio.sleep(3.5)
    message2 = f'Successfully removed ' + f'`{"{}".format(" ".join(args))}`' + " Arcane" + level + f"from {user.mention}"
    await message.edit(content = f'**{message2}**')
    print("Running Commands, Fake Level Reset")
    await asyncio.sleep(10)
    await ctx.message.delete()

# Custom fake level add command for Omega Mods -eqaddlvl <user> <num> 
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Omega Moderator')
# Cooldown settings, 1 uses every 5 seconds
@commands.cooldown(1, 5, commands.BucketType.user)
async def addlvl(ctx, user: discord.Member, *args):
    if args == 1:
        level = " level "
    else:
        level = " levels "
    await asyncio.sleep(.5)
    message = await ctx.reply("<a:loading:976985717043499078> " + f'Adding ' + f'`{"{}".format(" ".join(args))}`' + level + f"to {user.mention}")
    await asyncio.sleep(3.5)
    message2 = f'Successfully added ' + f'`{"{}".format(" ".join(args))}`' + " Arcane" + level + f"to {user.mention}"
    await message.edit(content = f'**{message2}**')
    print("Running Commands, Fake Level Reset")
    await asyncio.sleep(10)
    await ctx.message.delete()

# Fake ban countdown for all Moderators to use -eqban <user>
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Moderator')
# Cooldown settings, 1 uses every 5 seconds
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx, user: discord.Member):
    await asyncio.sleep(.25)
    print("Running Commands, Fake Ban Countdown")

    message = await ctx.reply(content = "<a:loading:976985717043499078> " + f'Banning {user.mention} in.')
    await asyncio.sleep(.5)

    await message.edit(content = "<a:loading:976985717043499078> " + f'Banning {user.mention} in..')
    await asyncio.sleep(.5)

    await message.edit(content = "<a:loading:976985717043499078> " + f'Banning {user.mention} in...')
    await asyncio.sleep(.5)

    await message.edit(content = f'Banning {user.mention} in... ')
    await asyncio.sleep(.25)

    await message.edit(content = f'Banning {user.mention} in... 5️⃣')
    await asyncio.sleep(1)

    await message.edit(content = f'Banning {user.mention} in... 4️⃣')
    await asyncio.sleep(1)

    await message.edit(content = f'Banning {user.mention} in... 3️⃣')
    await asyncio.sleep(1)

    await message.edit(content = f'Banning {user.mention} in... 2️⃣')
    await asyncio.sleep(1)

    await message.edit(content = f'Banning {user.mention} in... 1️⃣', delete_after = 1)
    await asyncio.sleep(1)

    # Embeded message
    ban_msg = (f"🔨 {user} has been banned.") # Message displayed on embed
    bancn_embed = discord.Embed(colour = discord.Color.from_rgb(86,186,126))
    bancn_embed.set_author(name = ban_msg) # Check mark and ban message
    await ctx.send(embed = bancn_embed)
    await asyncio.sleep(10)
    await ctx.message.delete()

# Fun Hack command for all Members to use -eqhack <user> 
@bot.command()
@commands.has_role('Member')
# Cooldown settings, 1 uses every 5 seconds
@commands.cooldown(1, 5, commands.BucketType.user)
async def hack(ctx, user: discord.Member):
    # Lists of fake info
    emails = ["1111nothacker@gmail.com", "Dog@yahoo.com", "learn2spell@school.com", "lastsamurai@earth.com", "susbak_gaming@amogus.com", "xXImaRoboxCidLmaoXx@gmail.com", "cat_lover@yahoo.com", "tww_addict@urmom.com", "the_lego_mane@yourhouse.com", "i_have_your_ip@gmail.com"]
    passwords = ["Equinoxi$besT_YT", "Password", "SmellySock39", "YouWontGuessThisOne", "yetanotherpassword", "iforgot", "LifeIsLikeABoxOfChocolates", "I_$ecretlyloveAmogus", "69420KullestCidOnBoblocx", "TuwuRidg3isCute", "Ieat_dinoNuggiEs", "123456789 :0", "I$ell_EquiNox-Feetpics", "xX_twwprogamer69420_Xx"]
    quotes = ["My computer got virus, so I injected it with vaccine.exe", "The worst thing about hackers finding your password is having to rename your dog", "I want my children to have all the things I couldn’t afford. Then I want to move in with them.", "My favorite machine at the gym is the vending machine.", "Equinox's content is just so good! You should definitely Subscribe", "Where did the three people that escaped Alcatraz go? We don’t know we’re still looking",
             "Equinox Go BRRRRRRRRRRRR", "When life gives you melons, you could be dyslexic.", "I can’t brain today. I have the dumb", "You know it’s cold outside when you go outside and it’s cold.", "Money can’t buy happiness, but it can buy you tons of Robux!"]
    random_words = ["Your Mom", "Bob", "Homiephobic", "amogus", "Equinox", "stonks", "The Wild West", "Jailbreak", "Adopt me", "Brookhaven RP", "sus bak", "uwu", "Milk", "doge", "ong", "¯\_(ツ)_/¯", "cooki", "MERICA"]
    ip_addresses = ["193.179.222.158", "32.57.249.93", "92.231.211.104", "61.118.248.11", "115.5.38.195", "245.33.204.162", "68.186.156.22", "84.220.35.89", "232.192.222.188", "162.80.186.72", "49.95.63.191", "29.37.42.227", "1.248.165.101", "174.161.215.214", "237.60.98.237", "195.89.104.99", "242.208.152.153", "225.51.199.70", "15.92.231.91", "27.230.12.214"]
    search_history = ["How do I drink water?", "What does grass feel like?", "How to get more than 30fps in The Wild West?", "Baby Shark song words", "Equinox is the best YouTuber, right?", "Books on scamming, How to scam people in Roblox", "I bought a book on scamming but it never came", "How to clear search history", "What is search history", "Can the government see what you search", "How to commit tax fraud", "How get rid of virus", "How to trick mom into buying robuck",
                    "How to eat a hamter", "When does life give you lemons?", "Is there any better YouTuber than Equinox?", "How to trick my dad into coming back", "Is raw chicken edible?", "How long does it normally take to get milk?", "How to hack into the Roblox IRS, so I don't have to pay Robuck taxes?"]
    roblox_accounts = ["Sniper1yfe", "7Labrodor7", "Detective_Tux", "CrowbarJones17", "FlashKylo", "ciokint", "DensetsuDied", "crabbycrab5641", "150bilder", "Frankmeister31", "jackbanks27", "iLikeLettuse", "Kenosis80", "LAVA_opmytrf", "leadCarl", "MaskedNoLife", "samuel430555", "ravenravener", "OnskuThe", "YT_deadly301", "ThunderBolt_YeeT", "starbuck_starfighter", "VexticyYT", "SusBak_Gaming69", "Abyss760", "jemodederisdonut", "Mukkysek", "Nobster3000", "jaialaipleb420", "Equinox21", "Tuwuridge77"]

    loading = "<a:loading:976985717043499078>" # assigning the spinning emoji

    message = await ctx.send(content = loading + f' Hacking {user.name} now...')
    await asyncio.sleep(1.5)

    await message.edit(content = loading + f' Finding Discord login...')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' 2fa bypassed')
    await asyncio.sleep(1)

    await message.edit(content = loading + f""" **Login Information**:
    Email:`{random.choice(emails)}`
    Password:`{random.choice(passwords)}`""")
    await asyncio.sleep(4)

    await message.edit(content = loading + f' Fetching DMs with closest friends (if they have any)')
    await asyncio.sleep(3)

    await message.edit(content = loading + f' **Last DM:** `{random.choice(quotes)}`')
    await asyncio.sleep(4.5)

    await message.edit(content = loading + f' Finding most common word...')
    await asyncio.sleep(2.5)

    await message.edit(content = loading + f' **Most common word**: `{random.choice(random_words)}`')
    await asyncio.sleep(2.5)

    await message.edit(content = loading + f" Injecting the Equinox virus into {user.name}'s computer ")
    await asyncio.sleep(3)

    await message.edit(content = loading + f' Virus injected...')
    await asyncio.sleep(1.25)

    await message.edit(content = loading + f' Discord Nitro stolen')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' Scanning for Roblox account...')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' Hacking into Roblox account...')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' **Roblox account username**: `{random.choice(roblox_accounts)}`')
    await asyncio.sleep(3.5)

    await message.edit(content = loading + f' Finding IP address')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' **IP address**: `{random.choice(ip_addresses)}`')
    await asyncio.sleep(2.5)

    await message.edit(content = loading + f' Stealing data from Starboard Stuidos')
    await asyncio.sleep(2)

    await message.edit(content = loading + f' Reporting account to Discord for breaking TOS')
    await asyncio.sleep(2.5)

    await message.edit(content = loading + f' Hacking Google search history...')
    await asyncio.sleep(2.5)

    await message.edit(content = loading + f' **Last Search**: `{random.choice(search_history)}`')
    await asyncio.sleep(4)

    await message.edit(content = loading + f' Finished hacking {user.name}')
    await asyncio.sleep(1.5)

    await message.edit(content = f' **{ctx.message.author.mention} finished hacking {user.name}**')
    await ctx.message.delete() 
    print("Running Commands, Fake Hack Command Finished")

# Fake giveaway blacklist command for all moderators to use -eqblacklist <user>
@bot.command(pass_context=True)
@commands.has_any_role('Owner', 'Moderator', 'Event Manager', 'QOTD Host', 'Giveaway Manager')
# Cooldown settings, 1 uses every 3 seconds
@commands.cooldown(1, 3, commands.BucketType.user)
async def blacklist(ctx, user: discord.Member):
    await asyncio.sleep(.25)
    print("Running Commands, Fake Giveaway Blacklist")

    message = await ctx.reply(content = "<a:loading:976985717043499078> " + f'Blacklisting {user.mention} from winning giveaways')
    await asyncio.sleep(.5)

    await message.edit(content = "<a:loading:976985717043499078> " + f'Blacklisting {user.mention} from winning giveaways.')
    await asyncio.sleep(.5)

    await message.edit(content = "<a:loading:976985717043499078> " + f'Blacklisting {user.mention} from winning giveaways..')
    await asyncio.sleep(.5)

    await message.edit(content = "<a:loading:976985717043499078> " + f'Blacklisting {user.mention} from winning giveaways...')
    await asyncio.sleep(1)

    await message.delete()

    # Embeded message
    black_msg = (f"🎁 {user} has been blacklisted from winning giveaways.") # Message displayed on embed
    black_embed = discord.Embed(colour = discord.Color.from_rgb(255,215,0))
    black_embed.set_author(name = black_msg) # Check mark and ban message
    await ctx.send(embed = black_embed)
    await asyncio.sleep(5)
    await ctx.message.delete() 
    
#------------------------------------------------ Admin Commands ------------------------------------------------------#

# Automated embed message for trading channel -eqtraderule
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def traderule(ctx):
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Trading Rule")
        channel = bot.get_channel(tww_trading_channel_id) # <------ INSERT TWW-TRADING CHANNEL ID HERE
        Trade_embed = discord.Embed(colour = discord.Color.from_rgb(255, 174, 0)) # Color, could add Description and title
        Trade_embed.add_field(name = "🤝 Trading Channel Golden Rule", value = "Please do not repeatedly post the same trade, especially large trades, if the chat isn't super acitve. Doing this makes it hard for others to find trades and can be annoying.") # field one, golden rule info
        Trade_embed.set_footer(text= "Reminder: Do not post anything but trades in this channel") # Reminder in footer
        await channel.send(embed = Trade_embed)
        #await ctx.send(f"Embed sent to <#{tww_trading_channel_id}")
        await asyncio.sleep(129600) # 36 Hours

# Automated message for helping people verify -eqverifyhelp
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def verifyhelp(ctx):
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Verify Help")
        verify_channel = bot.get_channel(934519651063443506) # <------ INSERT VERIFY - ASK FOR HELP CHANNEL ID HERE ⭐
        unverified = discord.utils.get(ctx.guild.roles, id=unverified_role_id) # <------ INSERT UNVERIFIED ROLE ID HERE
        await verify_channel.send(f"**{unverified.mention} users, need help linking a Roblox account to your Discord account with Bloxlink? Make sure to read all the instructions in <#934514301136408586> and if you still need help ping an online Moderator**")
        await asyncio.sleep(302400) # 84 Hours

# Automated message for helping people accept the rules -eqaccepthelp
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def accepthelp(ctx):
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Accepting Rules Help")
        rule_channel = bot.get_channel(1029081817585831937) # <------ INSERT RULE - ASK FOR HELP CHANNEL ID HERE ⭐
        verified = discord.utils.get(ctx.guild.roles, id=verified_role_id) # <------ INSERT VERIFIED ROLE ID HERE
        message = await rule_channel.send(f"**users, need help accepting the rules? You can either click the ✅ reaction in <#934510079028379738> or use the -eqacceptrules command. Full instructions can be found in <#934589950593208450>**")
        await asyncio.sleep(3)
        # Don't ping Equinox, edit message to ping verified
        await message.edit(content = f"**{verified.mention} users, need help accepting the rules? You can either click the ✅ reaction in <#934510079028379738> or use the -eqacceptrules command. Full instructions can be found in <#934589950593208450>**")
        await asyncio.sleep(151200) # 42 Hours

# Automated embed message for meme channel -eqmemerule
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def memerule(ctx):           
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Meme Rule")
        channel = bot.get_channel(meme_channel_id) # <------ INSERT MEME CHANNEL ID HERE
        Meme_embed = discord.Embed(colour = discord.Color.from_rgb(255, 174, 0)) # Color, could add Description and title
        Meme_embed.add_field(name = "📜 Meme Channel Rules", value = "All the server rules still apply in this channel, but there is an exception concerning Rule 13, No Profanity. Mild Profanity in memes is alright, but if a Moderator feels it's too much then you may be warned or muted. If you have any questions concerning this exception ask a Moderator") # field one, rule info
        Meme_embed.set_footer(text= "Although mild profanity is tolerated, slurs will not be") # Reminder in footer
        await channel.send(embed = Meme_embed)
        #await ctx.send(f"Embed sent to <#{meme_channel_id}")
        await asyncio.sleep(223200) # 62 Hours

# Automated informational embed message for art channel -eqartinfo
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def artinfo(ctx):           
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Art Info")
        channel = bot.get_channel(art_channel_id) # <------ INSERT MEME CHANNEL ID HERE
        Art_embed = discord.Embed(title = 'Art Channel Information', colour = discord.Color.from_rgb(255,165,94)) # Color, could add Description and title
        Art_embed.set_author(name = f"Equinox's Community", icon_url = server_pfp_url) # Author's Name and Pfp at top of embed
        Art_embed.add_field(name = '', value = "Post artwork you have created here! It can be anything (IRL drawings, digital art, animations, things created in games, etc.) and it will be on display for other Members to vote on by reacting with one of the following reactions:\n> **<:Number_3:1178820069044781056> = Very impressive (3 Points)**\n> **<:Number_2:1154844866405204058> = Amazing (2 Points)**\n> **<:Number_1:1178819846063017984> = Good job (1 Point)**", inline = False)
        Art_embed.add_field(name = '', value = "At the end of each month (or sometimes every two months) the person with the best overall drawing based on votes will get the <@&952657675601207306> role, which will be announced in <#909620958191550465>! Each vote is manually counted and checked to make sure it is a legitimate person voting and not some bot/alt.", inline = False)
        Art_embed.add_field(name = '', value = ":warning: Before posting your artwork, make sure its following all the rules stated here:\n> **➤ The artwork is not inappropriate**\n> **➤ The artwork is not stolen from someone else or generated by AI**\n> **➤ It does not include sensitive info/topics**\n> **➤ It's actual artwork and not just some random image**", inline = False)
        Art_embed.set_footer(text= "If these rules are not followed you may be warned/muted by a Moderator and get your post will get deleted.") # Reminder in footer
        await channel.send(embed = Art_embed)
        await asyncio.sleep(691200) # 8 days

# Automated embed message for resetting nickname -eqnickhelp
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def nickhelp(ctx):           
    await ctx.message.delete()
    while 1 != 2:
        print("Running Commands, Nickname Reset Help")
        channel = bot.get_channel(bot_commands_channel_id) # <------ INSERT BOT COMMAND CHANNEL ID HERE 
        Trade_embed = discord.Embed(colour = 0xf1c40f) # Color, could add Description and title
        Trade_embed.add_field(name = "🏷️ Resetting your Nickname", value = "If you wish to reset your nickname, use the **-eqreset** command") # field one, rule info
        Trade_embed.set_footer(text= "Need any help doing this? Ping @Equinox21") # Reminder in footer
        await channel.send(embed = Trade_embed)
        await asyncio.sleep(259200) # 72 Hours

# Event Pings Advertisement -eqrolesad
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def rolesad(ctx):
    await ctx.message.delete()
    while 1 != 2:
        # Event Pings Ad
        print("Running Commands, Event Pings Advertisement")
        # Sending the embed
        event_channel = bot.get_channel(events_channel_id) # <------ INSERT EVENT CHANNEL ID HERE 
        event_embed = discord.Embed(title = "🔔 Ping Roles", colour = 0x3498db) # Title, Color, could add Description
        event_embed.add_field(name = "Want to get notified when Events are happening?", value = (f"React with 🏆 below to get Event Pings role"))
        event_embed.set_footer(text=f"Solstice") # Solstice in footer
        event_embed.timestamp = datetime.now() # Timestamp of when event occured
        await event_channel.send(embed = event_embed)
        await asyncio.sleep(172800) # 2 Days

        # QOTD Pings Ad
        print("Running Commands, Event Pings Advertisement")
        qotd_channel = bot.get_channel(qotd_channel_id) # <------ INSERT QOTD CHANNEL ID HERE
        qotd_embed = discord.Embed(title = "🔔 Ping Roles", colour = discord.Color.from_rgb(196, 128, 255))   # Title, Color, could add Description
        qotd_embed.add_field(name = "Want to get notified for new Questions/News of the Day?", value = (f"React with 🎙️ below to get QOTD Pings role"))
        qotd_embed.set_footer(text=f"Solstice") # Solstice in footer
        qotd_embed.timestamp = datetime.now() # Timestamp of when event occured
        await qotd_channel.send(embed = qotd_embed)
        await asyncio.sleep(172800) # 2 Days

        # Group Member Ad
        print("Running Commands, Group Member Advertisement")
        group_channel = bot.get_channel(general_channel_id) # <------ INSERT GENERAL CHANNEL ID HERE 
        group_embed = discord.Embed(title = "<:roblox_logo:1132025950461243443> Group Member Role", colour = discord.Color.from_rgb(255, 17, 17))   # Title, Color, could add Description
        group_embed.add_field(name = "Want to get the Group Member role?", value = (f"Become a Member of the Roblox Group today! https://www.roblox.com/groups/14510739/Equinoxs-Community#!/about"))
        group_embed.set_footer(text=f"After joining the group, run the /getrole command in #bot-commands") # Message in footer
        #group_embed.timestamp = datetime.now() # Timestamp of when event occured
        await group_channel.send(embed = group_embed)
        await asyncio.sleep(172800) # 2 Days

# Talk through bot command -eqsay <arg>
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 5 seconds per user
@commands.cooldown(2, 5, commands.BucketType.user)
async def say(ctx, *args):
    await ctx.message.delete()
    await ctx.send("{}".format(" ".join(args)))
    print("Running Commands, EQ-Say")

# Send message through bot to another channel    -eqsend <channel> <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 5 seconds per user
@commands.cooldown(2, 5, commands.BucketType.user)
async def send(ctx, channel, *args):
    await ctx.message.delete()
    # remove the <#> from channel input
    channel_id = ''.join(filter(str.isdigit, channel))
    #print (f"{channel_id}")
    send_channel = bot.get_channel(int(channel_id)) # <------ CHANNEL ID
    await send_channel.send("{}".format(" ".join(args)))
    s_sent = await ctx.send(f"**Message sent to <#{channel_id}>**")
    # Delete confirmation
    await asyncio.sleep(5)
    await s_sent.delete()

# Send a user a dm through Solstice -eqdm
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds
@commands.cooldown(2, 10, commands.BucketType.guild)
async def dm(ctx, user: discord.User, *, message):
    await ctx.message.delete()
    await user.send(message)
    s_sent = await ctx.send(f"**Dm succesfully sent to {user.name}**")
    # Send embed to log channel
    log_channel = bot.get_channel(1133886027057090560) # <------ MAILBOX CHANNEL ID HERE ⭐
    log_embed = discord.Embed(title = "📧 Dm Sent", colour = 0x3498db) # Color, could add Description and Title
    log_embed.add_field(name = f"DM sent by Solstice to {user.name}", value = (f"{message}")) # Show what was sent in dm
    log_embed.set_thumbnail(url= f"{solstice_pfp_url}") # Big Image in top right of embed (Solstice's PFP)
    log_embed.set_footer(text=f"ID: {user.id}") # User's ID in footer
    log_embed.timestamp = datetime.now() # Timestamp of when event occured
    await log_channel.send(f"{user.id}") # Send the user ID as a normal message (easier to copy and paste on mobile)
    await log_channel.send(embed = log_embed)
    # Delete confirmation message
    await asyncio.sleep(5)
    await s_sent.delete()

# Dm all unverified members telling them to verifiy -eqdmunverified
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def dmunverified(ctx):
    await ctx.message.delete()
    await ctx.send("**📧 Sending DMs to all Unverified Members**")
    for guild in bot.guilds:
        role = discord.utils.find(lambda r: r.name == 'Unverified', guild.roles) # Set role which members need to have to recieve dm
        for member in guild.members:
            if guild.id == 909605610641825842: # Equinox's Community ID
                if role in member.roles:
                    try:
                        # Big Embed sent to everyone that's unverified
                        thumbnail = ctx.guild.icon.url # Command author's pfp
                        log_embed = discord.Embed(title = f"👋 Hello {member.display_name},", colour = discord.Color.from_rgb(13, 115, 237)) # Title and Color
                        log_embed.set_thumbnail(url=f"{thumbnail}") # Big Image in top right of embed
                        log_embed.add_field(name = "", value = f"I noticed you are still unverified in Equinox's Community even though you joined the server on " + f'{member.joined_at.strftime("%m/%d/%y")}.', inline = False)
                        log_embed.add_field(name = "Here are some steps to help you get verified, so you can gain full access to the server!", value = f"1. Check <#{934514301136408586}>, which explains each step of verifying with Bloxlink.", inline = False)
                        log_embed.add_field(name = "", value = f"2. Watch these videos created by Bloxlink that show you how to verify using their Bot.\n<:YouTube:1374526830995832853> https://www.youtube.com/watch?v=SbDltmom1R8&t=0s\n<:YouTube:1374526830995832853> https://www.youtube.com/watch?v=RhC8AIv1Mfk&t=0s", inline = False)  
                        log_embed.add_field(name = "", value = f"3. Ping <@882061427265921055> in <#{934519651063443506}> for help and they will assist you in the verification process.", inline = False)
                        log_embed.add_field(name = "", value = "**Until you verify, your permissions will be limited and you will be unable to participate in Giveaways and certain Events.**", inline = False)
                        log_embed.set_footer(text = f"Message sent from Equinox's Community")
                        log_embed.timestamp = datetime.now() # Timestamp of when event occured
                        await member.send(embed = log_embed)
                        
                        print(f"DM sent to {member}")
                        await asyncio.sleep(2)
                    # Dms probably closed so just skip to next member
                    except:
                        print(f"Unable to send DM to {member}")
                        pass 
                # Pass members that dont meet the criteria (they are verified)
                else:
                    pass
            # Pass members that are not even in Equinox's Community 
            else:
                pass
    # Loop ends
    await ctx.send("**📧 Finished sending DMs to all Unverified Members**")

# Advertisment command to post a random Equinox video! -eqad
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def ad(ctx):
    await ctx.message.delete()
    # Lists to randomize and variables
    videos = ["https://youtu.be/0I1ncrxU-J8","https://youtu.be/pqSQzX-cj3o","https://youtu.be/X-oQrsGMfgc","https://youtu.be/hoF7g3J41XY","https://youtube.com/shorts/-I410zAEeMA","https://youtu.be/Md2_0HJsCwk","https://youtube.com/shorts/4Jd0Be85TcA","https://youtu.be/Ac6xQBwJPoE","https://youtu.be/j_sr8AdKPss","https://youtu.be/xrRVkW_idDg","https://youtu.be/1OpK-6bleRc","https://youtu.be/pr7zB1ukHB0","https://youtube.com/shorts/c6wE_ipVnI4","https://youtube.com/shorts/2g-Wnr_-J0A",
    "https://youtu.be/v682Oh-xHP0","https://youtu.be/vFZow84aQmQ","https://youtu.be/bv6FSj0GgO0","https://youtu.be/ipya37x464I","https://youtu.be/FUNjHY9OllI","https://youtu.be/3ufDCCSVX_8","https://youtu.be/-rpDRm6a804","https://youtube.com/shorts/AjVBSLbpbI4","https://youtu.be/v6YCrUYirV8","https://youtu.be/YsjDpm35gC0","https://youtu.be/Ad-YIVY3xeE","https://youtu.be/oYhwziSJbPs", "https://youtube.com/shorts/YWYk_0YBHAk?feature=share", "https://youtu.be/dcdhuqln3I8",
    "https://youtube.com/shorts/uhGvCoiLEK0", "https://youtu.be/GjRU-JCaQGE", "https://youtu.be/1ZFiL06JeDI", "https://youtu.be/D8edZ1SEhCM", "https://www.youtube.com/shorts/LptmKm1Z18M", "https://www.youtube.com/shorts/HPQKNZ0wdhA", "https://youtu.be/rj1m-dOX5EQ", "https://youtu.be/VnafpoLNWn4", "https://youtube.com/shorts/vEKi9MeftP0", "https://youtube.com/shorts/H0M7fEmsI_g", "https://youtu.be/gYJ-GIOoZzc", "https://youtu.be/et0KIWiZvPA", "https://youtu.be/XyrE6sgoZFM",
    "https://youtu.be/ypsIoEoSwic"]
    phrases = ["Have you seen this Equinox video yet?", "What are your thoughts on this Equinox video?", "Check out this video by Equinox!"]
    log_author_pfp = ctx.author.display_avatar # Command author's pfp

    # Set the embed
    vid = discord.Embed(title = f' {random.choice(phrases)}', colour = discord.Color.from_rgb(255,0,0))
    vid.set_author(name = f'Made by @Equinox21', icon_url = str(log_author_pfp)) # Author's Name and Pfp at top of embed
    # Send Embed with phrase in it
    await ctx.send(embed = vid)
    await asyncio.sleep(1)
    # Send the video link as normal message
    message = await ctx.send(content = "<:YouTube:1374526830995832853>" + f' {random.choice(videos)}')
    await asyncio.sleep(1)
    
    # Loop it to change after set time
    while 1 != 2:
        await asyncio.sleep(900) # 15 mins
        #print("Running Commands, Switching Equinox Ad")
        await message.edit(content = "<:YouTube:1374526830995832853>" + f' {random.choice(videos)}')

# Member give role command -eqmember <user>
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 5 seconds per user
@commands.cooldown(2, 5, commands.BucketType.user)
async def member(ctx, user: discord.Member):
    print("Running Commands, give Member role")
    await ctx.message.delete()
    role = discord.utils.get(ctx.message.guild.roles, id=member_role_id) # <------ MEMBER ROLE ID HERE
    # Already has the Member role
    if role in user.roles:
        await ctx.message.delete()
        # Send warning embed
        warning_embed = discord.Embed(colour = warning_embed_color)
        warning_embed.set_author(name = f"{user.name.capitalize()} already has the Member role.", icon_url = warning_embed_icon) 
        warning_msg = await ctx.send(embed = warning_embed)
        await asyncio.sleep(10)
        await warning_msg.delete()
        #print("Running Commands, Member role, Phase 1")
    # Doesn't already have the Member role
    if role not in user.roles:
        await user.add_roles(role)
        await ctx.send(f"**Successfully gave {user.name.capitalize()} the Member role**")
        #print("Running Commands, Member role, Phase 2") 

# Logs all member's roles and join dates
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def logmembers(ctx):
    await ctx.message.delete()
    intents = discord.Intents.default()
    intents.members = True
    channel = bot.get_channel(1081452487736832080) # <------ MEMBER LOGS CHANNEL ID HERE ⭐
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5

    # Messages stating it's started and the counter
    await ctx.send("📋 **Started logging all Members.**")
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} currently logged.**")
    # For loop to go through all members
    for guild in bot.guilds:
        for member in guild.members:
            if guild.id != 909605610641825842: # Equinox's Community ID
                pass
            else:
                # Embed Message
                logging = discord.Embed(title = '', description = f'{member.mention}', colour = discord.Color.from_rgb(46, 164, 255)) # Member's name and embed color
                logging.set_author(name = f"{member}", icon_url = str(member.display_avatar)) # Member's ID at top
                roles = [role.mention for role in member.roles[1:]]
                num_of_roles = (str(len(roles)))
                roles = (" ".join(roles))
                logging.add_field(name = 'Account Created:', value = f'{member.created_at.strftime("%m/%d/%y")}', inline = True) # Discord join date
                logging.add_field(name = 'Joined Server:', value = f'{member.joined_at.strftime("%m/%d/%y")}', inline = True) # Server join date
                logging.add_field(name = f'<:logmembers:1143674996930117732> Roles [{num_of_roles}]', value = f"{roles}", inline = False) # List out the member's roles
                logging.set_footer(text=f"{member.id}") # Text + ID in footer
                logging.timestamp = datetime.now() # Timestamp of when event occured
                await channel.send(embed = logging)
                # Counter system
                counter +=1
                if counter >= five_counter:
                    await counter_message.edit(content = f"**🔄 {counter} out of {total_members} currently logged.**")
                    # Add 5 more to the five counter
                    five_counter += 5
                    await asyncio.sleep(2)
                # Skip every 5
                else:
                    await asyncio.sleep(2)
                    pass
    # Loop ends
    await counter_message.edit(content = f"**🔄 {counter} out of {total_members} currently logged.**")
    await ctx.send("📋 **Finished Logging all Members.**")

# Reset everyone's nickname (everyone under bot role) -resetnick
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def resetnick(ctx):
    await ctx.message.delete()
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5
    # Messages stating it's started and the counter
    await ctx.send("📛 **Started Reseting all Members' Nicknames.**")
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")

    # Loop to reset all nicknames
    for member in ctx.guild.members: # loop through every member in the guild
        try:
            await member.edit(nick=None) # reset their nickname
            counter +=1
        except:
            print(f"I was unable to change {member}'s nickname.")
            counter +=1
            pass
        # Counter system
        if counter >= five_counter:
            await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")
            # Add 5 more to the five counter
            five_counter += 5
            await asyncio.sleep(2)
        # Skip every 5
        else:
            await asyncio.sleep(2) # Keeps bot from rate limiting
            pass

    # Loop ends
    await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently reset.**")
    await ctx.send("📛 **Finished Reseting all Members' Nicknames.**")

# Change everyone's nickname (everyone under bot role) -trollnick
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 43200 seconds (12 hours)
@commands.cooldown(2, 43200, commands.BucketType.guild)
async def trollnick(ctx, *args):
    await ctx.message.delete()
    # Counter System for Progress
    total_members = str(ctx.guild.member_count)
    counter = 0
    five_counter = 5
    nickname = str("{}".format(" ".join(args)))
    # Messages stating it's started and the counter
    await ctx.send(f"📛 **Started Changing all Members' Nicknames to __{nickname}__.**")
    counter_message = await ctx.send(f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed.**")

    # Loop to change all member's nicknames
    for member in ctx.guild.members: # loop through every member in the guild
        try:
            await member.edit(nick=f'{nickname}') # Reset their nickname
            counter +=1
        except:
            print(f"I was unable to change {member}'s nickname.")
            counter +=1
            pass
        # Counter system
        if counter >= five_counter:
            await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed.**")
            # Add 5 more to the five counter
            five_counter += 5
            await asyncio.sleep(2)
        # Skip every 5
        else:
            await asyncio.sleep(2) # Keeps bot from rate limiting
            pass

    # Loop ends
    await counter_message.edit(content = f"**🔄 {str(counter)} out of {str(total_members)} nicknames are currently changed.**")
    await ctx.send(f"📛 **Finished Changing all Members' Nicknames to __{nickname}__.")

# Lists out all the faces Equionx owns the trademark to -eqtm 
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def tm(ctx):
    await ctx.message.delete()
    # Info for top of embed 
    log_author_pfp = ctx.author.display_avatar # Command author's pfp
    # Embeded message
    tm = discord.Embed(title = "Equinox's Copyrighted Faces", colour = 0xf1c40f)
    tm.set_author(name = f"©️ Copyright Notice", icon_url = str(log_author_pfp)) # Author's Name and Pfp at top of embed
    tm.add_field(name = ':D', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = ':o', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = ':0', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = 'D:', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = ':O', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = ':|', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:o', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:)', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:D', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:|', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:O', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    tm.add_field(name = '>:(', value = "©️ 2022 -2025 Equinox. All Rights Reserved", inline = True)
    await ctx.send(embed = tm)

# ONLY WORKS WHEN THERE IS NO ROTATING STATUS
# Set a Playing status on bot     -play <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def play(ctx, *message):
    await ctx.message.delete()
    message = str("{}".format(" ".join(message)))
    await bot.change_presence(status=discord.Status.online, activity = discord.Game(name=f"{str(message)}"))
    s_sent = await ctx.send(f"Changed bot activity to **Playing {message}**")
    # Delete confirmation
    await asyncio.sleep(7.5)
    await s_sent.delete()

# Set a Watching status on bot     -watch <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def watch(ctx, *message):
    await ctx.message.delete()
    message = str("{}".format(" ".join(message)))
    await bot.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name=f"{str(message)}"))
    s_sent = await ctx.send(f"Changed bot activity to **Watching {message}**")
    # Delete confirmation
    await asyncio.sleep(7.5)
    await s_sent.delete()

# Set a Listening status on bot     -listen <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def listen(ctx, *message):
    await ctx.message.delete()
    message = str("{}".format(" ".join(message)))
    await bot.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name=f"{str(message)}"))
    s_sent = await ctx.send(f"Changed bot activity to **Listening to {message}**")
    # Delete confirmation
    await asyncio.sleep(7.5)
    await s_sent.delete()

# Set a Streaming status on bot     -stream <link> <message>
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def stream(ctx, link, *message):
    await ctx.message.delete()
    message = str("{}".format(" ".join(message)))
    await bot.change_presence(status=discord.Status.online, activity = discord.Streaming(name=f"{str(message)}", url = str(f"{link}")))
    s_sent = await ctx.send(f"Changed bot activity to **Streaming {message}**")
    # Delete confirmation
    await asyncio.sleep(7.5)
    await s_sent.delete()

# Clear status on bot     -clearstatus
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def clearstatus(ctx):
    await ctx.message.delete()
    await bot.change_presence(status=None)
    s_sent = await ctx.send("Cleared bot activity status")
    # Delete confirmation
    await asyncio.sleep(7.5)
    await s_sent.delete()

# Check bot ping command -eqping
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def ping(ctx):
    await ctx.message.delete()
    # Send embed
    warning_embed = discord.Embed()
    warning_embed.set_author(name = f"Ping: {round(bot.latency * 1000)}ms", icon_url = "https://cdn.discordapp.com/attachments/935672317512650812/1155259162553503864/Ping_Icon.png") 
    await ctx.send(embed = warning_embed)

# Check memory command -eqmemory
@bot.command()
@commands.has_permissions(administrator = True)
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def usage(ctx):
    await ctx.message.delete()
    bedem = discord.Embed(title = 'System Resource Usage', description = 'CPU and Memory usage of Solstice')
    bedem.add_field(name = 'CPU Usage', value = f'{psutil.cpu_percent()}%', inline = False)
    bedem.add_field(name = 'Memory Usage', value = f'{psutil.virtual_memory().percent}%', inline = False)
    memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    memory = '{:0.1f}'.format(memory)
    bedem.add_field(name = 'Available Memory', value = f'{memory}%', inline = False)
    await ctx.send(embed = bedem)
    bedem.timestamp = datetime.now() # Timestamp of when event occured

#------------------------------------------------ List out all Commands ------------------------------------------------------#

# Informational Embeds
informational_embed = discord.Embed(title = 'Informational Embeds', colour = 0xf1c40f)
informational_embed.set_author(name = f"Made by @Equinox21", icon_url = equinox_pfp_url) # Author's Name and Pfp at top of embed
informational_embed.add_field(name = '🤝 -eqtraderule', value = "Send an informational embed to the trading channel, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '📛 -eqverifyhelp', value = "Ping unverified members to verify + info, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '✅ -eqaccepthelp', value = "Ping verified members to accept the rules + info, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '📜 -eqmemerule', value = "Send an informational rule embed to the meme channel, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '🎨 -eqartinfo', value = "Send an informational embed to the art channel, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '🏷️ -eqnickhelp', value = "Send an informational embed to bot commands channel, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '🔔 -eqrolesad', value = "Send a reaction role embed to events & qotd channel (along with rbx group ad), only Administrators can use this command", inline = True)
informational_embed.add_field(name = '<:YouTube:1374526830995832853> -eqad', value = "Showcase videos by Equinox (changes every 15mins), only Administrators can use this command", inline = True)
informational_embed.add_field(name = '👋 -eqdmunverified', value = "Send a helpful message to all Unverified Members, only Administrators can use this command", inline = True)
informational_embed.add_field(name = '📋 -eqlogmembers', value = "Log all member's roles, only Administrators can use this command", inline = True)

# Administrator Commands Embed
administrator_cmds_embed = discord.Embed(title = 'Administrator Commands', colour = 0xf1c40f)
administrator_cmds_embed.set_author(name = f"Made by @Equinox21", icon_url = equinox_pfp_url) # Author's Name and Pfp at top of embed
administrator_cmds_embed.add_field(name = '💬 -eqsay', value = "Enter any message for the bot to repeat, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '📤 -eqsend', value = "Enter a channel and message for the bot to send in that channel, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '📧 -eqdm', value = "Send a dm to a member through Solstice, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🧑‍💼 -eqmember', value = "Add the Member role to any user, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '⭕ -eqresetnick', value = "Reset all members' nicknames, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '<:troll:942866030118723614> -eqtrollnick', value = "Change all members' nicknames to <message>, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '©️ -eqtm', value = "Shows all the copyrighted faces Equinox owns, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🎲 -eqplay', value = "Change the bot's status to playing <msg>, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '👀 -eqwatch', value = "Change the bot's status to watching <msg>, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🎵 -eqlisten', value = "Change the bot's status to listening to <msg>, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🔴 -eqstream', value = "Change the bot's status to watching <msg>, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🗑️ -eqclearstatus', value = "Clears the bot's status (can use play, watch, listen, stream), only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '⚠️ /delete', value = "Delete a message in any channel, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '🚅 -eqping', value = "Check the bot's latency, only Administrators can use this command", inline = True)
administrator_cmds_embed.add_field(name = '📈 -equsage', value = "Check the bot's resource usage, only Administrators can use this command", inline = True)

# Staff Commands Embed
staff_cmds_embed = discord.Embed(title = 'Staff Commands', colour = 0xf1c40f)
staff_cmds_embed.set_author(name = f"Made by @Equinox21", icon_url = equinox_pfp_url) # Author's Name and Pfp at top of embed
staff_cmds_embed.add_field(name = '🏆 -eqwinner', value = "Add a user ID after the command to give them the Event Winner role, only Event Managers can use this command", inline = True)
staff_cmds_embed.add_field(name = '<:Champion_trophy:1380260555448909954> -eqchamp', value = "Add a user ID after the command to give them the Event Champion role, only Event Managers can use this command", inline = True)
staff_cmds_embed.add_field(name = '📋 -eqacceptrules', value = "Gives the command author the Member role, only Verified users can use this command", inline = True)
staff_cmds_embed.add_field(name = '🏷️ -eqreset', value = "Clears the command author's nickname, all Members can use this command", inline = True)
staff_cmds_embed.add_field(name = '⚠️ -eqpurge', value = "Add a user ID and amount of messages to purge, only people with Manage Message permissions can use this command", inline = True)
staff_cmds_embed.add_field(name = '<:Arcane:1132030517764690043> -eqrmvlvl', value = "Add a user ID & amount of levels after the command to fake remove levels from a user, only Omega Mods can use this command", inline = True)
staff_cmds_embed.add_field(name = '<:Arcane:1132030517764690043> -eqaddlvl', value = "Add a user ID & amount of levels after the command to fake add levels to a user, only Omega Mods can use this command", inline = True)
staff_cmds_embed.add_field(name = '💬 /say', value = "Say something with Solstice using the slash command, all Staff can use this command", inline = True)
staff_cmds_embed.add_field(name = '🔨 -eqban', value = "Add a user ID after the command to fake ban them with a countdown, only Moderators can use this command", inline = True)
staff_cmds_embed.add_field(name = '🎁 -eqblacklist', value = "Add a user ID after the command to fake blacklist them from giveaways, all Staff can use this command", inline = True)

# Member Commands Embed
member_cmds_embed = discord.Embed(title = 'Member Commands', colour = 0xf1c40f)
member_cmds_embed.set_author(name = f"Made by @Equinox21", icon_url = equinox_pfp_url) # Author's Name and Pfp at top of embed
member_cmds_embed.add_field(name = '🏷️ -eqreset', value = "Clears the command author's nickname, all Members can use this command", inline = True)
member_cmds_embed.add_field(name = '<a:loading:976985717043499078> -eqhack', value = "Add a user ID after the command to fake hack a user, all Members can use this command", inline = True)
member_cmds_embed.add_field(name = '👋 /hello', value = "Say hello to Solstice, all Members can use this command", inline = True)

# ------------------------ FULL ADMINISTRATOR VIEW ------------------------ #

class AdminSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Informational Embeds", emoji = "ℹ️"),
            discord.SelectOption(label = "Administrator Commands", emoji = "⚙️"),
            discord.SelectOption(label = "Staff Commands", emoji = "🔨"),
            discord.SelectOption(label = "Member Commands", emoji = "🙂")
            ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Informational Embeds":
            # Informational Embeds
            await interaction.response.edit_message(embed = informational_embed)
            
        elif self.values[0] == "Administrator Commands":
            # Administrator Commands
            await interaction.response.edit_message(embed = administrator_cmds_embed)

        elif self.values[0] == "Staff Commands":
            # Staff Commands
            await interaction.response.edit_message(embed = staff_cmds_embed)

        elif self.values[0] == "Member Commands":
            # Member Commands
            await interaction.response.edit_message(embed = member_cmds_embed)

class AdminSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(AdminSelect())

# ------------------------ HALF STAFF VIEW ------------------------ #
        
class StaffSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Staff Commands", emoji = "🔨"),
            discord.SelectOption(label = "Member Commands", emoji = "🙂")
            ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Staff Commands":
            # Staff Commands
            await interaction.response.edit_message(embed = staff_cmds_embed)

        elif self.values[0] == "Member Commands":
            # Member Commands
            await interaction.response.edit_message(embed = member_cmds_embed)

class StaffSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(StaffSelect())

# ------------------------ MEMBER VIEW ------------------------ #
        
class MemberSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label = "Member Commands", emoji = "🙂")
            ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Member Commands":
            # Member Commands
            await interaction.response.edit_message(embed = member_cmds_embed)

class MemberSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(MemberSelect())

# ------------------------ COMMAND TO RUN ALL ------------------------ #
        
@bot.command()
@commands.has_any_role('Member')
# Cooldown settings, 2 uses in 10 seconds per user
@commands.cooldown(2, 10, commands.BucketType.user)
async def cmd(ctx):
        await ctx.message.delete()
        moderator_role = discord.utils.find(lambda r: r.name == 'Moderator', ctx.message.guild.roles) # Set the Moderator role
        event_manager_role = discord.utils.find(lambda r: r.name == 'Event Manager', ctx.message.guild.roles) # Set the Event Manager role
        qotd_host_role = discord.utils.find(lambda r: r.name == 'Qotd Host', ctx.message.guild.roles) # Set the Qotd Host role
        giveaway_manager_role = discord.utils.find(lambda r: r.name == 'Giveaway Manager', ctx.message.guild.roles) # Set the Moderator role
        
        # Has Administrator
        if ctx.message.author.guild_permissions.administrator:
            # Will only send the full menu in Hidden channels
            if ctx.message.channel.id == 935672317512650812 or ctx.message.channel.id == 1032086398179737670 or ctx.message.channel.id == 1133886027057090560: 
                # Informational Embed
                await ctx.send(embed = informational_embed, view = AdminSelectView()) # Full Menu
            else:
                # Normal Staff Embed
                await ctx.send(embed = staff_cmds_embed, view = StaffSelectView()) # Half Menu

        # Has a Staff role
        elif moderator_role in ctx.author.roles or event_manager_role in ctx.author.roles or qotd_host_role in ctx.author.roles or giveaway_manager_role in ctx.author.roles:
            # Normal Staff Embed
            await ctx.send(embed = staff_cmds_embed, view = StaffSelectView()) # Half Menu

        # Normal Member Embed
        else: 
            await ctx.send(embed = member_cmds_embed, view = MemberSelectView()) # Member Menu
            
#------------------------------------------------ Slash Commands ------------------------------------------------------#

tree = app_commands.CommandTree

# Makes the is_owner requirement to be used in slash commands
def is_owner():
    def predicate(interaction : discord.Interaction):
        if interaction.user.id == interaction.guild.owner_id:
            return True
    return app_commands.check(predicate)

# Simple Hello Command
@bot.tree.command(name= "hello", description= "Say hello to Solstice")
# Cooldown, amount of uses, seconds for those uses
@app_commands.checks.cooldown(1, 3, key = lambda i: (i.guild_id))
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.mention}!', ephemeral= True)

# Slash Say Command
@bot.tree.command(name= "say", description= "Say something with Solstice")
@app_commands.describe(phrase = "What should I say?")
# Cooldown, amount of uses, seconds for those uses
@app_commands.checks.cooldown(1, 3, key = lambda i: (i.guild_id))
async def say(interaction: discord.Interaction, phrase: str):
    await interaction.response.send_message(f'{phrase}')

# Slash Delete Command
@bot.tree.command(name= "delete", description= "Delete a message using Solstice")
@app_commands.describe(message = "insert the message ID here", channel = "insert the channel ID here")
# Cooldown, amount of uses, seconds for those uses
@app_commands.checks.cooldown(1, 3, key = lambda i: (i.guild_id))
@is_owner()
async def delete(interaction: discord.Interaction, message: str, channel: str):
    channel = bot.get_channel(int(channel)) # Channel ID
    msg = await channel.fetch_message(int(message)) # Message ID
    await msg.delete() # Deleting
    await interaction.response.send_message(f'Deletion Successful', ephemeral= True)

#------------------------------------------------ Error Messages ------------------------------------------------------#

# Embed for errors
async def error_warning(ctx, message):
    warning_embed_icon = "https://cdn.discordapp.com/attachments/935672317512650812/1154896305320112139/warning_2.png"
    warning_embed_color = discord.Color.from_rgb(255,50,50)

    # Send warning embed
    warning_embed = discord.Embed(colour = warning_embed_color)
    warning_embed.set_author(name = message, icon_url = warning_embed_icon) 
    warning_msg = await ctx.send(embed = warning_embed)
    await asyncio.sleep(10)
    await warning_msg.delete()

@bot.event
async def on_command_error(ctx, error):
    print("Running Errors Section")

    # Cooldown error (deletes command)
    if isinstance(error, commands.CommandOnCooldown):
        error_msg_1 = "This command is on cooldown, please try again in {:.0f} seconds.".format(error.retry_after)
        await ctx.message.delete()
        print(f"Error 1, cooldown: {error}")
        await error_warning(ctx, error_msg_1)

    # Missing role error (deletes command)
    elif isinstance(error, commands.MissingRole):
        error_msg_2 = "You do not have the role needed to run this command."
        await ctx.message.delete()
        print(f"Error 2, missing role: {error}")
        await error_warning(ctx, error_msg_2)

    # Missing permissions error (deletes command)
    elif isinstance(error, commands.MissingPermissions):
        error_msg_3 = "You do not have the permissions needed to run this command."
        await ctx.message.delete()
        print(f"Error 3, missing permissions: {error}")
        await error_warning(ctx, error_msg_3)

    # Missing argument error (deletes command)
    elif isinstance(error, commands.MissingRequiredArgument):
        error_msg_4 = "You did not provide a required argument needed to run this command."
        await ctx.message.delete()
        print(f"Error 4, missing argument: {error}")
        await error_warning(ctx, error_msg_4)
    
    # Invalid command (ignore)
    elif isinstance(error, commands.CommandNotFound):
        error_msg_5 = "Command does not exist."
        await ctx.message.delete()
        print(f"Error 5, invalid command: {error}")
        await error_warning(ctx, error_msg_5)

    # Bot missing permissions error
    elif isinstance(error, commands.BotMissingPermissions):
        bot_error_msg_1 = "I do not have the permissions needed to run this command."
        await ctx.message.delete()
        print(f"Bot Error 1, missing permissions: {error}")
        await error_warning(ctx, bot_error_msg_1)

    # Bot missing role error
    elif isinstance(error, commands.BotMissingRole):
        bot_error_msg_2 = "I do not have the role needed to run this command."
        await ctx.message.delete()
        print(f"Bot Error 2, missing role: {error}")
        await error_warning(ctx, bot_error_msg_2)
    
    # There was an undefined Error
    else:
        await error_warning(ctx, "There was an error performing this action.")

#------------------------------------------------ Running the Bot ------------------------------------------------------#

# Run the Bot
bot.run(TOKEN)