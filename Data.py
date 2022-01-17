from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
(ಥ﹏ಥ) Olá {}

(￣▽￣)ノ Bem vindo(a) ao {}

(⌒_⌒;) Você acaba-se de se encontrar uma forma de editar? Então você chegou e achou seu destino!

💁🏻‍♂️ Entre nos canais, para atualizações do bot, e avisos sobre ele: → [Aperta aqui](https://telegra.ph/-01-17-630) 
♦️

By @The_Panda_Ofc ←(>▽<)ﾉ
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🤨 Voltar", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("👨🏻‍💻 Criador 👨🏻‍💻", url="https://t.me/The_Panda_Ofc")],
        [
            InlineKeyboardButton("👀 Quer saber como me usar❔ 👀", callback_data="help"),
            InlineKeyboardButton("💁🏻‍♂️ Sobre 💁🏻‍♂️", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Canal ♥", url="https://t.me/GR4V3_S4D_CRAZZY")],
        [InlineKeyboardButton("♦️ Grupo ♦️", url="https://t.me/blazer808_Stay")],
    ]

    # Help Message
    HELP = """
♦️ Bom a forma mais fácil de me usar ♦️.
♦️ Para me adicionar no seu canal, use o botão 'Add Channel' ou, use `/add` comando. ♦️

♦️ **Comandos do bot** ♦️

/about - Sobre o Bot
/help - Mensagem de ajuda
/start - Iniciar o bot

♦️ Comandos Alternativos ♦️
/channels - Lista de canais que você adicionou
/add - Adicionar ao canal
/report - Reportar o Problema, chama-se no pv e sobre o assunto senão leva spam! @The_Panda_Ofc
    """

    # About Message
    ABOUT = """
**Sobre o bot** 

♦️ Bot que legenda  automaticamente nos canais. By: Baianor. 

Baianor : [Criador](https://t.me/The_Panda_Ofc)

Estrutura : [Pyrogram](docs.pyrogram.org)

Linguagem : [Python](www.python.org)

Desenvolvedor : @The_Panda_Ofc
    """
