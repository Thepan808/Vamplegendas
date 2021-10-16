from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
♦️ Olá {}

♦️ Bem vindo ao {}

♦️ Você acaba-se de se encontrar uma forma de editar? Então você chegou e achou🧐!

By @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="♦️ Voltar", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("♦️ Criador ♦️", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")],
        [
            InlineKeyboardButton("♦️ Quer saber como me usar❔ ♦️", callback_data="help"),
            InlineKeyboardButton("♦️ Sobre ♦️", callback_data="about")
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
/channels - Lista de canais que você adicinou
/add - Adicionar ao canal
/report - Reportar o Problema, chama-se no pv e sobre o assunto senão leva spam! @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx
    """

    # About Message
    ABOUT = """
**Sobre o bot** 

♦️ Bot que legenda  automaticamente nos canais. By: Baianor. 

Baianor : [Criador](https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx)

Framework : [Pyrogram](docs.pyrogram.org)

Linguagem : [Python](www.python.org)

Desenvolvedor : @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx
    """
