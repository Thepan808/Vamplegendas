from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
♞⬝ Olá meu caro usuário {}

👑 Bem vindo(a) ao {}

🎖️ Aproveite o uso do bot, e lembre-se caso remover o bot em algum canal, aperte na opção de remover!

💁🏻‍♂️ Entre no canal de notícias, para atualizações do bot, e avisos sobre ele: → Aperta em criador!

♦️
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="👑 Voltar", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("👨🏻‍💻 Criador 👨🏻‍💻", url="https://t.me/botssaved")],
        [
            InlineKeyboardButton("👀 Como funciona❔ 👀", callback_data="help"),
            InlineKeyboardButton("👑 Sobre 👑", callback_data="about")
        ],
        [InlineKeyboardButton("🎖️ Canal 🎖️", url="https://t.me/botssaved")],
        [InlineKeyboardButton("🎖️ Criador 🎖️", url="https://t.me/the_panda_official")],
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
/report - Reportar o Problema, chama-se no pv e sobre o assunto senão leva spam! @The_Panda_Official
    """

    # About Message
    ABOUT = """
**Sobre o bot** 

♦️ Bot que legenda  automaticamente nos canais. 

Baianor : [Criador](https://t.me/The_Panda_Official)

Estrutura : [Pyrogram](docs.pyrogram.org)

Linguagem : [Python](www.python.org)

Desenvolvedor : @The_Panda_Official
    """
