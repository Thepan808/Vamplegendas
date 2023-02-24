from pyrogram import Client, filters
from ChannelBot.database.users_sql import get_channels
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.errors import ChannelInvalid

@Client.on_message((filters.regex(r'^♦️Gerenciar Canais♦️$') | filters.command('channels')) & filters.private)
async def _manage(bot: Client, msg):
    success, buttons, text = await manage_channels(msg.from_user.id, bot)
    if success:
        await msg.reply(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await msg.reply(text, reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True))


async def manage_channels(user_id, bot: Client):
    status, channels = await get_channels(user_id)
    if status:
        text = '🛸 Abaixo estão seus canais 🛸.'
        buttons = []
        for channel in channels:
            try:
                chat = await bot.get_chat(channel)
            except ChannelInvalid:
                continue
            buttons.append([InlineKeyboardButton(chat.title, callback_data=f'settings+{chat.id}')])
        return True, buttons, text
    else:
        buttons = [
                ['♦️Adicionar no canal♦️']
        ]
        return False, buttons, 'Nenhum canal encontrado. Adicione um canal usando o botão abaixo do teclado'
