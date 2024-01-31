import discord
from discord.ext import commands
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
bot = commands.Bot(command_prefix=".", intents=permissoes)

@bot.event
async def on_ready():
    print("Estou pronto!")

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    canal = ctx.channel
    await ctx.reply(f"Olá, {usuario.display_name}\nVocê está no canal: {canal.name}")

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    res = num1 + num2
    await ctx.reply(f"A soma de {num1} + {num2} é igual a {res}")

@bot.command()
async def falar(ctx:commands.Context, *,frase):
    await ctx.send(frase)

@bot.command()
async def enviar_embed(ctx:commands.Context):
    meu_embed = discord.Embed(title='Olá, Mundo!', description='Descrição :D')
    
    imagem_arquivo = discord.File('imagens/imagem.jpg', 'imagem.jpg')
    meu_embed.set_image(url="attachment://imagem.jpg")

    thumb_arquivo = discord.File('imagens/thumb.jpg', 'thumb.png')
    meu_embed.set_thumbnail(url='attachment://thumb.png')

    meu_embed.set_footer(text='Este é o footer')

    meu_embed.color = discord.Color.dark_blue()

    canal_foto = discord.File('imagens/foto_canal.png', 'foto_canal.png')
    meu_embed.set_author(name='Lan Code', icon_url='attachment://foto_canal.png')

    meu_embed.add_field(name='Moedas', value=10, inline=False)
    meu_embed.add_field(name='Filme Favorito', value='DBS: Broly', inline=False)
    meu_embed.add_field(name='Rank', value='Prata', inline=False)


    await ctx.reply(files=[imagem_arquivo, thumb_arquivo, canal_foto], embed=meu_embed)

@bot.command()
async def botao(ctx:commands.Context):
    async def resposta_botao(interact:discord.Interaction):
        await interact.response.send_message('Botão Pressionado!', ephemeral=True)
        await interact.followup.send('Segunda resposta :D')
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label='canal', url='https://www.youtube.com/channel/UCD72t672otDUxeJViXu3gwA'))
    botao = discord.ui.Button(label='Botão')
    botao.callback = resposta_botao
    view.add_item(botao)
    await ctx.reply(view=view)

@bot.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f"Novo canal criado: {canal.name}")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1196465713465008208)
    meu_embed = discord.Embed(title=f'Bem vindo, {membro.name}!')
    meu_embed.description = "Aproveite a estadia!"
    meu_embed.set_thumbnail(url=membro.avatar)
    await canal.send(embed=meu_embed)

@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1196465713465008208)
    await canal.send(f"{membro.display_name} Saiu no servidor...\nAté Breve!")
bot.run("")
