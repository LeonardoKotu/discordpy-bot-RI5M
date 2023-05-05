import disnake
from disnake.ext import commands
from keep_alive import keep_alive

bot = InteractionBot()


@bot.event
async def on_ready():
  bot.add_view(General())
  print(f"{bot.user} - connected!")
  await bot.change_presence(
    activity=disnake.Streaming(name="Памятка сервера", url="https://twich.com")
  )


"""
General - ОБЩИЙ РАЗДЕЛ

Textchannels - правила текстовых.
Voicechannels - правила голосвых.
Automode - автомод.
TeamAdmins - администрация.
ModeBots - о сервисах ботах.
WarnsBot - меры наказаний
"""
"""-----------------------------------------------"""
# Textchannels

# text_channels = discord.Embed(
# 	title="<:hashtag:1089698689804677220> Раздел: Текстовое",
# 	colour=0x2f3136
# )

# 1.0
system_1 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.0`",
  description="""
	> `🌼` **Описание - **
	```Запрещены использование твинков на сервере. В целях обхода бана / фарм валюты и т.п.```
	""",
  colour=0x2f3136)

system_1.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Бан```""",
                   inline=True)

system_1.add_field(name="`⏱` **Длительность - **",
                   value="""
	```30д```
	""",
                   inline=True)

# 1.0
system_2 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.1`",
  description="""
	> `🌼` **Описание - **
	```Копирование профилей (аватарки/баннеры) строго запрещено.```
	""",
  colour=0x2f3136)

system_2.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Пред/мьют```""",
                   inline=True)

system_2.add_field(name="`⏱` **Длительность - **",
                   value="""
	```3д/30м```
	""",
                   inline=True)

# 1.0
system_3 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.2`",
  description="""
	> `🌼` **Описание - **
	```Запрещена реклама с разных ресурсов без соглашении Администрации.```
	""",
  colour=0x2f3136)

system_3.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Бан```""",
                   inline=True)

system_3.add_field(name="`⏱` **Длительность - **",
                   value="""
	```30д```
	""",
                   inline=True)

# 1.0
system_4 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.3`",
  description="""
	> `🌼` **Описание - **
	```Запрещены деструктивные действие по отношение к серверу: призыв покинуть сервер, попытки нарушить развития сервера или любые действие способные привести к помехам сервера.```
	""",
  colour=0x2f3136)

system_4.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Пред/мьют```""",
                   inline=True)

system_4.add_field(name="`⏱` **Длительность - **",
                   value="""
	```3д/3ч```
	""",
                   inline=True)

# 1.0
system_5 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.4`",
  description="""
	> `🌼` **Описание - **
	```Запрещено распространение личной информации без соглашении владельца.```
	""",
  colour=0x2f3136)

system_5.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Пред/мьют```""",
                   inline=True)

system_5.add_field(name="`⏱` **Длительность - **",
                   value="""
	```3д/3ч```
	""",
                   inline=True)

# 1.0
system_6 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.5`",
  description="""
	> `🌼` **Описание -**
	```Запрещён обман в целях получение выгоды.```
	""",
  colour=0x2f3136)

system_6.add_field(name="> `🍥` **Нарушение - **",
                   value="""
	```Пред/мьют```""",
                   inline=True)

system_6.add_field(name="`⏱` **Длительность - **",
                   value="""
	```3д/3ч```
	""",
                   inline=True)

system_1.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
system_2.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
system_3.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
system_4.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
system_5.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
system_6.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)

#1.0
text_1 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.6`",
  description="""
	> `🌼` **Описание - **
	```Запрещено неадекватное поведение и провокация в любом виде.```
	""",
  colour=0x2f3136)

text_1.add_field(name="> `🍥` **Нарушение - **",
                 value="""
	```Пред/мьют```""",
                 inline=True)

text_1.add_field(name="`⏱` **Длительность - **",
                 value="""
	```3д/3ч```
	""",
                 inline=True)

#1.0
text_2 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.7`",
  description="""
	> `🌼` **Описание - **
	```Запрещено злоупотребление пинга участника или роли.```
	""",
  colour=0x2f3136)

text_2.add_field(name="> `🍥` **Нарушение - **",
                 value="""
	```Пред/мьют```""",
                 inline=True)

text_2.add_field(name="`⏱` **Длительность - **",
                 value="""
	```3д/3ч```
	""",
                 inline=True)

#1.0
text_3 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.8`",
  description="""
	> `🌼` **Описание - **
	```Запрещено попытка рейда, флуда или спама.```
	""",
  colour=0x2f3136)

text_3.add_field(name="> `🍥` **Нарушение - **",
                 value="""
	```Пред/мьют```""",
                 inline=True)

text_3.add_field(name="`⏱` **Длительность - **",
                 value="""
	```3д/3ч```
	""",
                 inline=True)

text_1.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
text_2.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
text_3.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)

voice_1 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `1.9`",
  description="""
	> `🌼` **Описание - **
	```Запрещено неадекватное поведение/агрессия а так же оскорбление.```
	""",
  colour=0x2f3136)

voice_1.add_field(name="> `🍥` **Нарушение - **",
                  value="""
	```Пред/мьют```""",
                  inline=True)

voice_1.add_field(name="`⏱` **Длительность - **",
                  value="""
	```3д/3ч```
	""",
                  inline=True)

voice_2 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `2.0`",
  description="""
	> `🌼` **Описание - **
	```Запрещено использование сторонних программ для воспороизведение звука.```
	""",
  colour=0x2f3136)

voice_2.add_field(name="> `🍥` **Нарушение - **",
                  value="""
	```Пред/мьют```""",
                  inline=True)

voice_2.add_field(name="`⏱` **Длительность - **",
                  value="""
	```3д/3ч```
	""",
                  inline=True)

voice_3 = disnake.Embed(
  title="<a:a_pink_dot:1096413983700959252> пункт ﹕ `2.1`",
  description="""
	> `🌼` **Описание - **
	```Запрещено быстрое перемещение по голосовым каналам.```
	""",
  colour=0x2f3136)

voice_3.add_field(name="> `🍥` **Нарушение - **",
                  value="""
	```Пред/мьют```""",
                  inline=True)

voice_3.add_field(name="`⏱` **Длительность - **",
                  value="""
	```3д/3ч```
	""",
                  inline=True)

voice_1.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
voice_2.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)
voice_3.set_image(
  url=
  "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
)

warns = disnake.Embed(colour=0x2f3136)

warns.set_image(
  url=
  "https://media.discordapp.net/attachments/1079355839523065937/1080109884550422528/image_1.png?width=846&height=475"
)


# 2.0 Сначала общий раздел, для других опцих.
class General(disnake.ui.View):

  def __init__(self):
    super().__init__(timeout=None)  # timeout of the view must be set to None

  @discord.ui.select(
    placeholder="Нажми на меня",
    custom_id="click",
    options=[
      disnake.SelectOption(label="Системное",
                           emoji="<:systemupdate1:1089739471668400209>"),
      disnake.SelectOption(label="Текстовое",
                           emoji="<:hashtag:1089698689804677220>"),
      disnake.SelectOption(label="Голосовое",
                           emoji="<:voicesearch:1089698688361844766>"),
      disnake.SelectOption(label="Виды наказаний",
                           emoji="<:warns:1089698684238839880>"),
      disnake.SelectOption(label="Снять выбор",
                           emoji="<:close1:1089754099186159659>")
    ])
  # :: - при нажатий на любый опции, выполнфется это функция.
  async def select_callback(self, select, interaction):
    if select.values[0] == "Системное":
      await interaction.response.send_message(
        embeds=[system_1, system_2, system_3, system_4, system_5, system_6],
        ephemeral=True)
    if select.values[0] == "Текстовое":
      await interaction.response.send_message(embeds=[text_1, text_2, text_3],
                                              ephemeral=True)
    if select.values[0] == "Голосовое":
      await interaction.response.send_message(
        embeds=[voice_1, voice_2, voice_3], ephemeral=True)
    if select.values[0] == "Виды наказаний":
      await interaction.response.send_message(embed=warns, ephemeral=True)
    if select.values[0] == "Снять выбор":
      await interaction.response.send_message("Done.", ephemeral=True)


# создаём слеш-команду


@bot.slash_command(description="Доступно владельцу.")
#@commands.has_permissions(administrator = True)# команду сможет использовать роль в которой включена привилегия Администратор.
@commands.is_owner(
)  # This decorator will raise commands.NotOwner if the invoking user doesn't have the owner_id
async def general(ctx):

  # image_embed - первый эмбед, с изображением.
  image_embed = disnake.Embed(colour=0x2f3136)

  image_embed.set_image(
    url=
    "https://i.pinimg.com/originals/b1/44/16/b14416985ed8b574f97cb094a50bcefe.gif"
  )

  # embed - вывод полный информации о разделах
  embed = disnake.Embed(
    title=f"<:white:1100864283883081748> Правила сообщества {ctx.guild}",
    description="""
		> `::` С помощью **меню-выбора** выберите тип правил.
		""",
    colour=0x2f3136)

  # линия -
  embed.set_image(
    url=
    "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
  )

  # отправляем всё это -
  await ctx.send(embeds=[image_embed, embed], view=General())


# запускаем бота


@general.error
async def on_application_command_error(ctx: discord.ApplicationContext,
                                       error: discord.DiscordException):
  if isinstance(error, commands.NotOwner):
    await ctx.respond(embed=disnake.Embed(
      description=f"Команда `/general` доступно только овнеру.",
      colour=0x2f3136),
                      ephemeral=True)
  else:
    raise error  # Here we raise other errors to ensure they aren't ignored


"""///////////////////////////////////////////////////////////////////////////////////////////"""

textchannels_embed = disnake.Embed(title="", )
#FFFFFF

text = disnake.Embed(
  title="<a:aesthetic_j_star_p:1092056726968225893> Раздел: Навигация",
  description="""
    `🔎` В этом разделе показаны какие **каналы** на сервере существуют, и для чего они предназначены.
    `❗️` Следует отметить, что некоторые каналы могут измениться.
    """,
  color=0x2f3136)

text.add_field(name="⸻・Информация",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091530485919928352> - **Правила сервера**
    <:1Ew_dot:1092056728968888370> <#1091530773577867264> - **Информейшен**
    <:1Ew_dot:1092056728968888370> <#1091866867263610991> - **Команды ботов**
    """,
               inline=False)

text.add_field(name="⸻・Биография",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091871358423679039> - **Выбор ролей**
    <:1Ew_dot:1092056728968888370> <#1091871551508451349> - **Добавить информацию о себе**
    """,
               inline=False)

text.add_field(name="⸻・Контент",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091872419813265490> - **Розыгрыши на сервере**
    <:1Ew_dot:1092056728968888370> <#1091900797299732560> - **Наборы**
    <:1Ew_dot:1092056728968888370> <#1091872586377474078> - **Магазинчик сервера**
    """,
               inline=False)

text.add_field(name="⸻・Общение",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091906193531883540> - **Основной чат**
    <:1Ew_dot:1092056728968888370> <#1091908518602358835> - **Не знаю**
    <:1Ew_dot:1092056728968888370> <#1091908716003074048> - **Информация  о людей**
    <:1Ew_dot:1092056728968888370> <#1091906773302132786> - **Корзина**
    """,
               inline=False)

text.add_field(name="⸻・Боты/развлечение",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091917943635443782> - **Нейрость с ботом <@1041989228667621407>**
    <:1Ew_dot:1092056728968888370> <#1091918521287594065> - **Мемы с ботом <@270904126974590976>**
    <:1Ew_dot:1092056728968888370> <#1091920112371634206> - **Игрульки с ботом <@555772119980572687>**
    <:1Ew_dot:1092056728968888370> <#1091923433677389864> - **Тоже игрульки с ботом <@383995098754711555>**
    <:1Ew_dot:1092056728968888370> <#1091924051750047804> - **Нитро-генератор**
    """,
               inline=False)

text.add_field(name="⸻・Медиа",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091910993677910107> - **Фоточки**
    <:1Ew_dot:1092056728968888370> <#1091912659038904350> - **Селфи**
    <:1Ew_dot:1092056728968888370> <#1091912840824242287> - **Аватарки**
    <:1Ew_dot:1092056728968888370> <#1091912923988885564> - **Баннеры**
    """,
               inline=False)

text.add_field(name="⸻・🌴 Help",
               value="""
    <:1Ew_dot:1092056728968888370> <#1091913902238990406> - **Тикеты**
    <:1Ew_dot:1092056728968888370> <#1091914050973220874> - **Бампы**
    """,
               inline=False)

text.set_footer(text="Увидели баг? Обратитесь к euphoria#8699")

roles = disnake.Embed(
  title="<:protection:1093127731224526909> **LMNS** **`Администрация`**",
  description="""
    > <:turndown1:1093134655491944489><:tph_pink_dot:1092051639914999838> <@&1091914406222381176> - **Владелец**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1091914410672537610> - **Заместитель**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1091914412253790288> - **Администратор**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1091914413512085514> - **Модератор**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1091914414376099912> - **Помощник**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1091914415986704424> - **Организатор**
    > <:line6:1093136187356610664> <:tph_pink_dot:1092051639914999838>  <@&1093146571312472134> - **Дизайнер**
    > <:turndown:1093134653398982686> <:tph_pink_dot:1092051639914999838> <@&1093146616183140373> - **Разработчик ботов**
    
    ⚡️ Чтобы стать один из нас необходимо подать **анкету** - [перейти!](https://discord.com/channels/1091518244755619850/1091900797299732560)
    """,
  colour=0x2f3136)

roles.set_footer(text="Увидели баг? Обратитесь к euphoria#8699")


class InfoChannels(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @disnake.ui.select(
    placeholder="Что будем смотреть?",
    custom_id="info",
    options=[
      disnake.SelectOption(label="Навигация",
                           emoji="<:compass:1089764870418874389>"),
      disnake.SelectOption(label="Администрация",
                           emoji="<:setting2:1089764864391655445>"),
      disnake.SelectOption(label="Команды бота",
                           emoji="<:bot:1089764868703399977>"),
      disnake.SelectOption(label="Экономика",
                           emoji="<:coins:1089764861279469588>"),
      disnake.SelectOption(label="Снять выбор",
                           emoji="<:close1:1089754099186159659>")
    ])
  async def select_callback(self, select, interaction):
    if select.values[0] == "Навигация":
      await interaction.response.send_message(embed=text, ephemeral=True)

    if select.values[0] == "Администрация":
      await interaction.response.send_message(embed=roles, ephemeral=True)

    if select.values[0] == "Сервис боты":
      pass

    if select.values[0] == "Экономика":
      pass

    if select.values[0] == "Снять выбор":
      #pass
      await interaction.response.send_message("Done!")


@bot.slash_command()
@commands.is_owner()
async def information(ctx):
  image = disnake.Embed(colour=0x2f3136)

  image.set_image(
    url=
    "https://media.discordapp.net/attachments/1100945663283437578/1102939752656814171/21d673fc35c314717c54e6a89c63bf3b.gif"
  )

  embed = disnake.Embed(
    title=
    f"<:white_heart:1091699308111347852> Информация о сообществе {ctx.guild}",
    description="""
		> `::` Здесь вы сможете ознакомиться **полезную** информацию, чтобы у вас вопрос не возникало!
		""",
    colour=0x2f3136)

  embed.set_image(
    url=
    "https://cdn.discordapp.com/attachments/1080131439154176010/1087096393698660503/ScreenShot_20230319223256.jpeg"
  )
  #text_3.set_image(url="")

  await ctx.respond(embeds=[image, embed], view=InfoChannels())


import os


bot.run(os.environ["DISCORD_TOKEN"])
