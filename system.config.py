#from http import client
import discord
import random

client = discord.Client()

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    

    user = "stockupdate123456@gmail.com"
    msg['from'] = user
    password = "idrrbyfxiimhuife"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    

@client.event
async def on_ready():
    print("bot is ready")

Muny_quotes = ["that’s no fun...u admitted defeat so quickly", "MY HEAD IS SO FUCKING BIG", "lesssgaurrr yaur yaurrr", 
        "we have lil expectations of u now franz😔😔..i send messages knowing i’ll never get a reply", "thank u sammy i love u💗😔", "ITS FUCKING GOOD", "johann?..being able to read?", "you're not that important johann",
        "last time i held johann's hand he and franz threw me into the ocean", "i’m tired of franz’s and johann’s bs", "johann leaves me on read too😔😔", "franz is a lil shit",
        "starting to think i’m seeing shit", "u annoying piece of shit", "OMG YAURRR SAMMMY", "omg wtf that was hot", "naurrrr cuz that sound was literally playing in my head when jp left",
        "brute what r u still doing here", "it’s okay brute ...we’re all victims of johann and franz’s stalking", "😔😔😔it’s tough out here at least ik i always got u sammy", "send help sammy if i don’t say anything in 2 hours", "ayeee sammy i love u sm😔 💗", "I like kids VERY much", "i dont love u even as a friend" , "U DONT LIKE SOJU?",
        "https://cdn.discordapp.com/attachments/937994635861708850/942294086847721472/unknown.png", "that’s not what u were saying last night😏😏", 
        "ever heard of don’t have anything nice to say keep it to urself? 😊😊😊", "😭😭😭damn bro don’t come for me like that", "bruh it’s hard to trust brute’s memory just throw anything at him atp😔😔", "yaurrr naurrr haurr haurr", "😭😭NAUR" ]


@client.event
async def on_message(message):

    print(f'{message.author} said {message.content}')

    if message.author == client.user:
        
        return

    if message.content.startswith('ayo'):
        print(f'{message.author} said ayo')
        
        random_integer = random.randint(0, len(Muny_quotes) - 1)

        random_Muny_quote = Muny_quotes[random_integer]

        await message.channel.send(random_Muny_quote)

    if message.content.startswith('ayo'):
        await message.add_reaction('\U0001F60F')

    if message.content.startswith('naur'):
        print(f'{message.author} said naur')
        
        random_integer = random.randint(0, len(Muny_quotes) - 1)

        random_Muny_quote = Muny_quotes[random_integer]

        await message.channel.send(random_Muny_quote)

    if message.content.startswith('naur'):
        await message.add_reaction('\U0001F9CD')

    if message.content.startswith('daddy'):
        print(f'{message.author} said naur')
        
        random_integer = random.randint(0, len(Muny_quotes) - 1)

        random_Muny_quote = Muny_quotes[random_integer]

        await message.channel.send(random_Muny_quote)

    if message.content.startswith('daddy'):
        await message.add_reaction('\U0001F9CD')
        

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}\n'
    )

@client.event
async def on_message_delete(deleted):
    print(f'{deleted.author} deleted a message: {deleted.content}')
    await deleted.channel.send('https://cdn.discordapp.com/attachments/892284203775979541/943358345073537124/Screenshot_2022-02-15_200859.png')
    await deleted.channel.send('https://tenor.com/view/caught-in4k-gif-24567243')
    await deleted.channel.send(
        
        f'{deleted.author} GOT CAUGHT LACKING IN 4K. 📷 💯 😈 🤡 😩\n'
        f'\n'
        f'\n'
        f'DELETED MESSAGE: ```{deleted.content}```\n'
        
    )
    
    email_alert(f'Message Deleted By: {deleted.author}', f'Deleted Message: {deleted.content}', "9493467793@vtext.com")
    print("Sent SMS Successfully to JP")

    email_alert(f'Message Deleted By: {deleted.author}', f'Deleted Message: {deleted.content}', "9497356031@txt.att.net")
    print("Sent SMS Successfully to Johann")


    
        

client.run('OTIxMTQ1MjY1MTg3MDc0MDc4.YbupYQ.mx-vDsEI7wMiBFlQhvHI99v0xGg')


