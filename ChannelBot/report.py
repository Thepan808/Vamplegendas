from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex(r'^♦️Reportar o Problema♦️$') | filters.command('report'))
async def _manage(_, msg):
    how = '**Reportar o Problema** \n\n'
    how += "Se caso algo acontecer, ou não sabe oque está fazendo **Doido da cabeça** bom, me comunique\n\n"
    how += '**Próximo passo** \n'
    how += '1) Tente o que você fez novamente. Se mostrar a mesma coisa inesperada, vá para a etapa 2 \n'
    how += '2) Entre em contato comigo e define seu problema **completamente** Bom, aguardo e espero que te ajude.'
    how += "♦️ Boa sorte ♦️."
    await msg.reply(
        how,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Entre em Contato', url='https://t.me/the_panda_official')]
        ]),
        quote=True
    )
