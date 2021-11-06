import os
from pyrogram import Client, filters


@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    if m.media and not (m.video_note or m.sticker):
        if m.caption:
            cap = m.caption
        else:
            cap = ""
        await m.copy(
            m.chat.id,
            caption=cap,
        )
        await m.delete()
    else:
        await m.copy(m.chat.id)
        await m.delete()



bot.run()
