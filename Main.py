import discord, os, json, discord.utils
from dotenv import load_dotenv

load_dotenv()
CLIENT = discord.Client(intents=discord.Intents.all())



def printSTD(text:str):
    print("\t" + text)


@CLIENT.event
async def on_ready():
    print("Bot Online:")
    printSTD("Servers bot is currently in:")
    for guild in CLIENT.guilds: 
        printSTD("\t" + guild.name)

@CLIENT.event
async def on_message(message):
    pass


@CLIENT.event
async def on_member_join(member):

    with open('Config.json', "r") as f: 
        configJSON = json.load(f)
    roleName = configJSON[str(member.guild.id)][0]["RoleName"]
    role = discord.utils.get(member.guild.roles, name=roleName)
    await member.add_roles(role)


CLIENT.run(os.getenv("GreyAdminBot"))