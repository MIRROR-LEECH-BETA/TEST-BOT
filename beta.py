import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from database import *
import re
import os
from helper.database import getid

id_pattern = re.compile(r'^.\d+$')

#os.system("pip install ffmpeg -y")





API_ID = "9075917"
API_HASH = "53b16179d95eeffe4586141eda85d6b7"
TOKEN = "5498982543:AAEvNUF5MQEf-lbeshO7-3O91pB3W3F29UQ"

ZAID = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@ZAID.on_message(filters.private & filters.command("start"))
async def hello(client: ZAID, message: Message):
    await message.reply_text(
       text="Hey! I'am A First Ever Rename Bot Cloner \nClick /clone To Know More",
       reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("❣️ SUPPORT", url="https://t.me/BETA_SUPPORT"),
               InlineKeyboardButton("📢 UPDATES", url="https://t.me/Beta_Botz")
               ],[           
               InlineKeyboardButton("😉 OWNER", url="t.me/tg_bi_tch")
               ]]
               )
           )




ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

@ZAID.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@ZAID.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="weit....")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")


##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@ZAID.on_message(filters.private & filters.command("clone"))
async def clone(bot: ZAID, msg: Message):
    text = await msg.reply("Usage\n\n /clone Bot Token")
    phone = msg.command[1]
    add_user(phone)
    print(all_users())
    
    try:
        m = await text.edit("Developing Your Bot")
                   # change this Directry according to ur repo
        client = Client( ":memory:", API_ID, API_HASH, bot_token=phone, in_memory=True, plugins={"root": "plugins"})
        await client.start()
        idle()
        user = await client.get_me()
        await m.edit(f"Your Bot Has Been Successfully Started As @{user.username}! ✅\n\nThanks for Cloning. \nJoin @BETA_BOTZ")
    except Exception as e:
        print(e)
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")


op = users.find()
for kk in op:
    nam = [kk['bot_token']]
    for usr in nam:
        print(usr)
        app = Client("cache",api_id=API_ID, api_hash=API_HASH, bot_token=usr ,in_memory=True, plugins={"root": "plugins"})
        app.start()


ZAID.start()
idle()
