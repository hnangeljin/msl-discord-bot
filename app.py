import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DICORD_TOKEN")
channel_id = '624886171553497098'
message_color = 0xffffff

client = discord.Client()

@client.event
async def on_message(message):
 if message.author == client.user:
     return
    
# a = message.content    
# if message.content == INVALID:
#     embed=discord.Embed()
#     embed.add_field(name="rpst", value= str(a), inline=True)
#     await client.send_message(client.get_channel('624888886514024481'), embed=embed)
     
##################################################################### room J

 if message.content.startswith("Newswpic") and message.channel.id ==(channel_id):
     a = ""
     b = ""
     x = ""
     invalid = False
     spacerequired = True
     info = message.content.replace("Newswpic", "")

     for i in range(0,info.find("https://")):
           x += info[i]

     a =(x)
     x = ""

     for i in range(info.find("https://"), len(info)):
           x += info[i]

     b =(x)

     embed=discord.Embed(title="", description=" ", url="", color=0xFFB6C1)
     embed.set_author(name=" ")
     embed.set_thumbnail(url="")
     embed.add_field(name=" ~ N e w s ~", value= str(a), inline=False)
     embed.set_image(url= str(b))
     await client.get_channel('544911289898500106').send(embed=embed)
     


 
 if message.content.startswith("Newssimple") and message.channel.id ==(channel_id):
     a = ""
     x = ""
     info = message.content
     for i in range(info.find("Newssimple")+10, len(info)):
           x += info[i]
     a =(x)
     embed=discord.Embed(title="", description=" ", url="", color=0xFFB6C1)
     embed.add_field(name=" ~ N e w s ~ ", value= str(a), inline=True)
     await client.get_channel('544911289898500106').send(embed=embed)
     

 if message.content.startswith("testsimple") and message.channel.id ==(channel_id):
     a = ""
     x = ""
     info = message.content
     for i in range(info.find("test")+10, len(info)):
           x += info[i]
     a =(x)
     embed=discord.Embed(title="", description=" ", url="", color=0xFFB6C1)
     embed.add_field(name=" ~ N e w s ~ ", value= str(a), inline=True)
     await message.channel.send(embed=embed)


 if message.content.startswith("testwpic") and message.channel.id ==(channel_id):
     a = ""
     b = ""
     x = ""
     invalid = False
     spacerequired = True
     info = message.content.replace("testwpic", "")

     for i in range(0,info.find("https://")):
           x += info[i]

     a =(x)
     x = ""

     for i in range(info.find("https://"), len(info)):
           x += info[i]

     b =(x)

     embed=discord.Embed(title="", description=" ", url="", color=0xFFB6C1)
     embed.set_author(name=" ")
     embed.set_thumbnail(url="")
     embed.add_field(name=" ~ N e w s ~", value= str(a), inline=False)
     embed.set_image(url= str(b))
     await message.channel.send(embed=embed)
     
##################################################################### ju-bot

 if " " in message.content:
     return

 if "." in message.content:
     return

    
 if "?" in message.content:
     return

    
 if "!" in message.content:
     return
    
 if any([message.content.startswith (item) for item in ['Knuc','FireKnuc']]):
     a = 27996
     b = 3344
     c = 2009
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#1 Knuckles (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Soni','WaterSoni']]):
     a = 26927
     b = 3344
     c = 2384
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#2 Sonic (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tail','WoodTail']]):
     a = 26440
     b = 2812
     c = 2856
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#3 Tails (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)

 if message.content.startswith("Tail"):
     return
  

 if any([message.content.startswith (item) for item in ['Silv','LightSilv']]):
     a = 32160
     b = 2696
     c = 3128
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#4 Silver (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shad','DarkShad']]):
     a = 24380
     b = 3916
     c = 2377
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#5 Shadow (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)

 if message.content.startswith("Shad"):
     return
     

 if any([message.content.startswith (item) for item in ['Alpa','FireAlpa']]):
     a = 30921
     b = 1826
     c = 1942
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#6 Alpaca (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)
     


 if any([message.content.startswith (item) for item in ['Alpa','WaterAlpa']]):
     a = 24965
     b = 3051
     c = 1648
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#7 Alpaca (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Alpa','WoodAlpa']]):
     a = 26893
     b = 2847
     c = 1498
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#8 Alpaca (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Alpa','LightAlpa']]):
     a = 32024
     b = 2389
     c = 2685
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#9 Alpaca (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Alpa','DarkAlpa']]):
     a = 22555
     b = 3173
     c = 2670
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#10 Alpaca (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ammo','FireAmmo']]):
     a = 41143
     b = 1506
     c = 1125
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#11 Ammonore (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ammo','WaterAmmo']]):
     a = 29484
     b = 1742
     c = 1800
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#12 Ammonore (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ammo','WoodAmmo']]):
     a = 25272
     b = 1784
     c = 2813
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#13 Ammonore (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ammo','LightAmmo']]):
     a = 30403
     b = 1892
     c = 1889
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#14 Ammonore (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ammo','DarkAmmo']]):
     a = 26327
     b = 2615
     c = 1573
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#15 Ammonore (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','FireAnu ']]):
     a = 38684
     b = 2112
     c = 2439
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#16 Anu (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','FireAnu ','SAnu ','FireSAnu ']]):
     a = 42722
     b = 2324
     c = 2684
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#17 Anu SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','WaterAnu ']]):
     a = 22739
     b = 3296
     c = 2111
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#18 Anu (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','WaterAnu ','SAnu ','WaterSAnu ']]):
     a = 25020
     b = 3657
     c = 2329
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#19 Anu SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','WoodAnu ']]):
     a = 23494
     b = 3092
     c = 2322
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#20 Anu (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','WoodAnu ','SAnu ','WoodSAnu ']]):
     a = 25851
     b = 3432
     c = 2561
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#21 Anu SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','LightAnu ']]):
     a = 39604
     b = 2351
     c = 1772
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#22 Anu (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','LightAnu ','SAnu ','LightSAnu ']]):
     a = 43730
     b = 2589
     c = 1949
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#23 Anu SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','DarkAnu ']]):
     a = 29617
     b = 2288
     c = 3296
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#24 Anu (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Anu ','DarkAnu ','SAnu ','DarkSAnu ']]):
     a = 32586
     b = 2527
     c = 3657
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#25 Anu SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arc ','FireArc ']]):
     a = 29412
     b = 1321
     c = 2642
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#26 Arc (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arc ','WaterArc ']]):
     a = 28439
     b = 1668
     c = 2486
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#27 Arc (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arc ','WoodArc ']]):
     a = 43220
     b = 1506
     c = 1172
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#28 Arc (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Arte','FireArte']]):
     a = 37247
     b = 2746
     c = 2807
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#31 Artemis (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arte','WaterArte']]):
     a = 30856
     b = 3173
     c = 2833
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#32 Artemis (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arte','WoodArte']]):
     a = 28016
     b = 3575
     c = 2492
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#33 Artemis (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arte','LightArte']]):
     a = 27826
     b = 3575
     c = 2458
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#34 Artemis (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arte','DarkArte']]):
     a = 31946
     b = 2533
     c = 3650
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#35 Artemis (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arth','FireArth']]):
     a = 27948
     b = 3466
     c = 2717
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#36 Arthur (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arth','WaterArth']]):
     a = 32453
     b = 2784
     c = 2930
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#37 Arthur (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arth','WoodArth']]):
     a = 28166
     b = 3766
     c = 2479
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#38 Arthur (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arth','LightArth']]):
     a = 26416
     b = 3936
     c = 2411
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#39 Arthur (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Arth','DarkArth']]):
     a = 49696
     b = 1976
     c = 2487
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#40 Arthur (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Balr','FireBalr']]):
     a = 25684
     b = 3152
     c = 3216
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#41 Balrona (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Balr','WaterBalr']]):
     a = 28813
     b = 3562
     c = 2452
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#42 Balrona (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Balr','WoodBalr']]):
     a = 31115
     b = 2683
     c = 3466
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#43 Balrona (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Balr','LightBalr']]):
     a = 32698
     b = 2866
     c = 2842
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#44 Balrona (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Balr','DarkBalr']]):
     a = 48212
     b = 2133
     c = 2507
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#45 Balrona (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bans','FireBans']]):
     a = 29382
     b = 2362
     c = 2433
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#46 Banshee (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bans','WaterBans']]):
     a = 40040
     b = 2364
     c = 1976
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#47 Banshee (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bans','WoodBans']]):
     a = 29760
     b = 3092
     c = 2152
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#48 Banshee (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bans','LightBans']]):
     a = 31575
     b = 2321
     c = 2631
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#49 Banshee (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bans','DarkBans']]):
     a = 42001
     b = 2405
     c = 1744
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#50 Banshee (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bast','FireBast']]):
     a = 30591
     b = 2343
     c = 3201
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#51 Bast (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bast','WaterBast']]):
     a = 43662
     b = 2705
     c = 2112
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#52 Bast (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bast','WoodBast']]):
     a = 31973
     b = 1914
     c = 2581
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#53 Bast (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bast','LightBast']]):
     a = 28779
     b = 2860
     c = 3562
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#54 Bast (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bast','DarkBast']]):
     a = 42546
     b = 2487
     c = 2487
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#55 Bast (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beat','FireBeat']]):
     a = 27172
     b = 2588
     c = 3099
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#56 Beatel (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beat','WaterBeat']]):
     a = 41374
     b = 2105
     c = 2037
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#57 Beatel (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beat','WoodBeat']]):
     a = 29998
     b = 2377
     c = 3221
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#58 Beatel (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beat','LightBeat']]):
     a = 30223
     b = 2166
     c = 3133
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#59 Beatel (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beat','DarkBeat']]):
     a = 24148
     b = 3194
     c = 2234
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#60 Beatel (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Beec','LightBeec']]):
     a = 28731
     b = 2356
     c = 1559
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#64 Beecomb (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beec','DarkBeec']]):
     a = 34837
     b = 1404
     c = 1683
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#65 Beecomb (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bell','FireBell']]):
     a = 23685
     b = 1696
     c = 1559
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#66 Bellpup (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bell','WaterBell']]):
     a = 26222
     b = 2001
     c = 1991
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#67 Bellpup (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bell','WoodBell']]):
     a = 31026
     b = 1566
     c = 1444
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#68 Bellpup (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Benj','FireBenj']]):
     a = 30556
     b = 3085
     c = 1907
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#71 Benjamin (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Benj','WaterBenj']]):
     a = 30454
     b = 1920
     c = 3187
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#72 Benjamin (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Benj','WoodBenj']]):
     a = 41388
     b = 2085
     c = 2439
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#73 Benjamin (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Benj','LightBenj']]):
     a = 26389
     b = 3364
     c = 2343
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#74 Benjamin (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Benj','DarkBenj']]):
     a = 27243
     b = 2886
     c = 2774
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#75 Benjamin (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beth','FireBeth']]):
     a = 28871
     b = 1994
     c = 1793
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#76 Beth (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beth','WaterBeth']]):
     a = 25367
     b = 2595
     c = 1818
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#77 Beth (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Beth','WoodBeth']]):
     a = 43901
     b = 1676
     c = 1295
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#78 Beth (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Bird','FireBird']]):
     a = 28752
     b = 1784
     c = 2527
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#81 Birdie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bird','WaterBird']]):
     a = 30451
     b = 1763
     c = 1943
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#82 Birdie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bird','WoodBird']]):
     a = 36812
     b = 1758
     c = 1247
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#83 Birdie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bird','LightBird']]):
     a = 27029
     b = 3133
     c = 2159
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#84 Birdie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bird','DarkBird']]):
     a = 44643
     b = 2010
     c = 1942
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#85 Birdie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bolt','FireBolt']]):
     a = 24291
     b = 3058
     c = 2138
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#86 Boltwing (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bolt','WaterBolt']]):
     a = 24250
     b = 2424
     c = 3173
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#87 Boltwing (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bolt','WoodBolt']]):
     a = 26096
     b = 3085
     c = 2281
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#88 Boltwing (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Bon ','WaterBon']]):
     a = 29589
     b = 1559
     c = 2506
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#92 Bon (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Bon ','LightBon']]):
     a = 29494
     b = 2663
     c = 1457
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#94 Bon (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Bron','FireBron']]):
     a = 28568
     b = 2404
     c = 1512
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#96 Bron (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bron','WaterBron']]):
     a = 29048
     b = 1681
     c = 1807
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#97 Bron (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bron','WoodBron']]):
     a = 29331
     b = 1321
     c = 2554
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#98 Bron (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Bulb','FireBulb']]):
     a = 33032
     b = 1881
     c = 1874
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#101 Bulbie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bulb','WaterBulb']]):
     a = 21499
     b = 3357
     c = 2363
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#102 Bulbie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bulb','WoodBulb']]):
     a = 27427
     b = 2192
     c = 2372
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#103 Bulbie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bulb','LightBulb']]):
     a = 32225
     b = 2023
     c = 3139
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#104 Bulbie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Bulb','DarkBulb']]):
     a = 24475
     b = 3378
     c = 2349
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#105 Bulbie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cand','FireCand']]):
     a = 28813
     b = 2595
     c = 1975
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#106 Candling (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cand','WaterCand']]):
     a = 24795
     b = 2601
     c = 1832
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#107 Candling (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cand','WoodCand']]):
     a = 29457
     b = 1742
     c = 1963
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#108 Candling (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Cann','FireCann']]):
     a = 34053
     b = 2267
     c = 2277
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#111 Canna (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cann','WaterCann']]):
     a = 28752
     b = 1948
     c = 3235
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#112 Canna (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cann','WoodCann']]):
     a = 29484
     b = 2396
     c = 2447
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#113 Canna (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cann','LightCann']]):
     a = 35443
     b = 1956
     c = 2316
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#114 Canna (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cann','DarkCann']]):
     a = 25776
     b = 3262
     c = 2349
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#115 Canna (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chir','FireChir']]):
     a = 27049
     b = 2527
     c = 1403
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#116 Chiroptie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chir','WaterChir']]):
     a = 36675
     b = 1710
     c = 1206
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#117 Chiroptie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chir','WoodChir']]):
     a = 29334
     b = 1933
     c = 1895
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#118 Chiroptie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chir','LightChir']]):
     a = 29249
     b = 1321
     c = 2527
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#119 Chiroptie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chir','DarkChir']]):
     a = 26041
     b = 2343
     c = 1566
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#120 Chiroptie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chlo','FireChlo']]):
     a = 39873
     b = 1976
     c = 2323
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#121 Chloe (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chlo','WaterChlo']]):
     a = 26675
     b = 2240
     c = 3173
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#122 Chloe (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chlo','WoodChlo']]):
     a = 23712
     b = 3323
     c = 2309
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#123 Chloe (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chlo','LightChlo']]):
     a = 30175
     b = 2261
     c = 3323
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#124 Chloe (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Chlo','DarkChlo']]):
     a = 26733
     b = 2716
     c = 2658
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#125 Chloe (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Coco','FireCoco']]):
     a = 29419
     b = 1437
     c = 2847
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#126 Cocomaru (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Coco','WaterCoco']]):
     a = 23706
     b = 2384
     c = 1709
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#127 Cocomaru (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Coco','WoodCoco']]):
     a = 31646
     b = 2642
     c = 1784
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#128 Cocomaru (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Coco','LightCoco']]):
     a = 37520
     b = 2235
     c = 1751
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#129 Cocomaru (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Coco','DarkCoco']]):
     a = 33141
     b = 2812
     c = 2365
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#130 Cocomaru (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Colt','LightColte']]):
     a = 30417
     b = 1749
     c = 1895
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#134 Colte (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Colt','DarkColte']]):
     a = 26430
     b = 2384
     c = 1818
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#135 Colte (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Cosm','LightCosmo']]):
     a = 32991
     b = 2076
     c = 2106
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#139 Cosmo (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cosm','DarkCosmo']]):
     a = 45522
     b = 1411
     c = 1445
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#140 Cosmo (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cott','FireCott']]):
     a = 27696
     b = 1362
     c = 1702
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#141 Cotteen (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cott','WaterCott']]):
     a = 30216
     b = 1457
     c = 1730
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#142 Cotteen (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cott','WoodCott']]):
     a = 31054
     b = 1532
     c = 1430
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#143 Cotteen (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Crow','FireCrow']]):
     a = 29368
     b = 2015
     c = 1684
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#146 Crowhook (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Crow','WaterCrow']]):
     a = 25926
     b = 2581
     c = 1777
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#147 Crowhook (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Crow','WoodCrow']]):
     a = 25565
     b = 2486
     c = 1784
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#148 Crowhook (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Cupi','FireCupi']]):
     a = 32456
     b = 2159
     c = 1989
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#151 Cupid (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cupi','WaterCupi']]):
     a = 30693
     b = 2036
     c = 2452
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#152 Cupid (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cupi','WoodCupi']]):
     a = 29875
     b = 2179
     c = 1989
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#153 Cupid (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cupi','LightCupi']]):
     a = 29630
     b = 2118
     c = 2513
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#154 Cupid (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cupi','DarkCupi']]):
     a = 37731
     b = 1806
     c = 2323
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#155 Cupid (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cura','FireCura']]):
     a = 30679
     b = 2036
     c = 2452
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#156 Cura (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cura','WaterCura']]):
     a = 38378
     b = 1928
     c = 2024
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#157 Cura (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cura','WoodCura']]):
     a = 37533
     b = 1962
     c = 2316
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#158 Cura (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cura','LightCura']]):
     a = 26178
     b = 2281
     c = 3194
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#159 Cura (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Cura','DarkCura']]):
     a = 29014
     b = 2532
     c = 2345
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#160 Cura (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ["D'art","FireD'art","Dart","FireDart"]]):
     a = 27220
     b = 3092
     c = 2418
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#161 Dartagnan (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ["D'art","WaterD'art","Dart","WaterDart"]]):
     a = 35579
     b = 2282
     c = 2058
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#162 Dartagnan (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ["D'art","WoodD'art","Dart","WoodDart"]]):
     a = 29933
     b = 2253
     c = 2386
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#163 Dartagnan (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ["D'art","LightD'art","Dart","LightDart"]]):
     a = 24734
     b = 3269
     c = 2254
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#164 Dartagnan (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ["D'art","DarkD'art","Dart","DarkDart"]]):
     a = 26736
     b = 2322
     c = 3194
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#165 Dartagnan (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drak','FireDrak']]):
     a = 24856
     b = 3902
     c = 2520
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#166 Draka (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drak','WaterDrak']]):
     a = 28643
     b = 3568
     c = 2622
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#167 Draka (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drak','WoodDrak']]):
     a = 50098
     b = 2010
     c = 2827
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#168 Draka (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drak','LightDrak']]):
     a = 30556
     b = 4038
     c = 2206
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#169 Draka (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drak','DarkDrak']]):
     a = 28946
     b = 3104
     c = 3162
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#170 Draka (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drow','FireDrow']]):
     a = 41688
     b = 2126
     c = 2487
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#171 Drowsey (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drow','WaterDrow']]):
     a = 26971
     b = 2682
     c = 2672
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#172 Drowsey (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drow','WoodDrow']]):
     a = 25394
     b = 3255
     c = 2261
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#173 Drowsey (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drow','LightDrow']]):
     a = 27492
     b = 3194
     c = 2206
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#174 Drowsey (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Drow','DarkDrow']]):
     a = 26041
     b = 3323
     c = 2281
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#175 Drowsey (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Fenn','FireFenn']]):
     a = 27179
     b = 2527
     c = 1566
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#176 Fennec (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Fenn','WaterFenn']]):
     a = 26940
     b = 2629
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#177 Fennec (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Fenn','WoodFenn']]):
     a = 23733
     b = 2574
     c = 1818
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#178 Fennec (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Fenn','LightFenn']]):
     a = 26293
     b = 3269
     c = 2281
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#179 Fennec (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Fenn','DarkFenn']]):
     a = 45951
     b = 1874
     c = 1874
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#180 Fennec (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Flor','WoodFlor']]):
     a = 30866
     b = 2131
     c = 2032
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#183 Flora (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Flor','LightFlor']]):
     a = 37527
     b = 2133
     c = 1874
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#184 Flora (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Flor','DarlFlor']]):
     a = 29675
     b = 2389
     c = 2535
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#185 Flora (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garg','FireGarg']]):
     a = 32923
     b = 1593
     c = 1521
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#186 Gargor (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garg','WaterGarg']]):
     a = 33488
     b = 1452
     c = 1670
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#187 Gargor (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garg','WoodGarg']]):
     a = 25374
     b = 1702
     c = 2581
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#188 Gargor (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Gati','FireGati']]):
     a = 28272
     b = 2267
     c = 2106
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#191 Gatito (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gati','WaterGati']]):
     a = 24210
     b = 1730
     c = 2697
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#192 Gatito (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gati','WoodGati']]):
     a = 26212
     b = 2588
     c = 1737
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#193 Gatito (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gati','LightGati']]):
     a = 34203
     b = 2221
     c = 2391
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#194 Gatito (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gati','DarkGati']]):
     a = 23283
     b = 3255
     c = 2363
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#195 Gatito (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garu','FireGaru']]):
     a = 30965
     b = 2247
     c = 3609
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#196 Garuda (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garu','WaterGaru']]):
     a = 24938
     b = 3643
     c = 2901
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#197 Garuda (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garu','WoodGaru']]):
     a = 31976
     b = 3036
     c = 2787
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#198 Garuda (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garu','LightGaru']]):
     a = 25367
     b = 3616
     c = 2670
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#199 Garuda (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Garu','DarkGaru']]):
     a = 28313
     b = 3207
     c = 2658
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#200 Garuda (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gemi','FireGemi']]):
     a = 28881
     b = 2615
     c = 1777
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#201 Gemini (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Gemi','LightGemi']]):
     a = 36301
     b = 2221
     c = 2432
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#204 Gemini (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Gemi','DarkGemi']]):
     a = 30832
     b = 2362
     c = 2481
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#205 Gemini (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Ghos','LightGhos']]):
     a = 35375
     b = 1554
     c = 1758
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#209 Ghos (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ghos','DarkGhos']]):
     a = 26041
     b = 2343
     c = 1566
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#210 Ghos (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Grab','FireGrab']]):
     a = 28878
     b = 2137
     c = 1923
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#211 Grabag (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Grab','WaterGrab']]):
     a = 33802
     b = 1704
     c = 1881
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#212 Grabag (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Grab','WoodGrab']]):
     a = 26327
     b = 1873
     c = 1580
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#213 Grabag (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Grab','LightGrab']]):
     a = 37459
     b = 1384
     c = 1881
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#214 Grabag (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Grab','DarkGrab']]):
     a = 34292
     b = 1663
     c = 1697
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#215 Grabag (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Gupp','WaterGupp']]):
     a = 26225
     b = 2343
     c = 1696
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#217 Gupp (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Hade','FireHade']]):
     a = 27281
     b = 3480
     c = 2492
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#221 Hades (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hade','WaterHade']]):
     a = 31922
     b = 2703
     c = 2747
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#222 Hades (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hade','WoodHade']]):
     a = 41109
     b = 2296
     c = 2609
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#223 Hades (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hade','LightHade']]):
     a = 33137
     b = 3548
     c = 2418
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#224 Hades (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hade','DarkHade']]):
     a = 32967
     b = 3677
     c = 2595
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#225 Hades (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hana','FireHana']]):
     a = 30468
     b = 2036
     c = 2431
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#226 Hana (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hana','WaterHana']]):
     a = 32463
     b = 2125
     c = 1954
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#227 Hana (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hana','WoodHana']]):
     a = 32443
     b = 2138
     c = 1989
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#228 Hana (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hana','LightHana']]):
     a = 36805
     b = 1976
     c = 1996
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#229 Hana (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hana','DarkHana']]):
     a = 29624
     b = 2125
     c = 1982
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#230 Hana (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Herm','WaterHerm']]):
     a = 29787
     b = 2343
     c = 3139
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#232 Hermite (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Hohe','FireHohe']]):
     a = 43213
     b = 2378
     c = 2630
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#236 Hohenheim (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hohe','WaterHohe']]):
     a = 32242
     b = 3009
     c = 2999
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#237 Hohenheim (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hohe','WoodHohe']]):
     a = 27233
     b = 3582
     c = 2901
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#238 Hohenheim (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hohe','LightHohe']]):
     a = 28105
     b = 3841
     c = 2499
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#239 Hohenheim (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hohe','DarkHohe']]):
     a = 28357
     b = 3718
     c = 2567
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#240 Hohenheim (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hunt','FireHunt']]):
     a = 25776
     b = 2595
     c = 1573
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#241 Hunter (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hunt','WaterHunt']]):
     a = 29164
     b = 1960
     c = 1684
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#242 Hunter (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hunt','WoodHunt']]):
     a = 30420
     b = 1539
     c = 2554
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#243 Hunter (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hunt','LightHunt']]):
     a = 30808
     b = 3064
     c = 1873
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#244 Hunter (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Hunt','DarkHunt']]):
     a = 30114
     b = 2309
     c = 3139
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#245 Hunter (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Incu','FireIncu']]):
     a = 31711
     b = 2648
     c = 2535
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#246 Incubus (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Incu','WaterIncu']]):
     a = 36505
     b = 2180
     c = 2432
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#247 Incubus (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Incu','WoodIncu']]):
     a = 25095
     b = 3173
     c = 2547
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#248 Incubus (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Incu','LightIncu']]):
     a = 27962
     b = 3167
     c = 2254
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#249 Incubus (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Incu','DarkIncu']]):
     a = 24822
     b = 3221
     c = 2492
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#250 Incubus (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Indr','FireIndr']]):
     a = 31694
     b = 3650
     c = 2288
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#251 Indra (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Indr','WaterIndr']]):
     a = 27768
     b = 3043
     c = 3033
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#252 Indra (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Indr','WoodIndr']]):
     a = 32841
     b = 2846
     c = 2910
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#253 Indra (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Indr','LightIndr']]):
     a = 23317
     b = 3977
     c = 2479
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#254 Indra (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Indr','DarkIndr']]):
     a = 28166
     b = 3677
     c = 2554
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#255 Indra (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jack','FireJack']]):
     a = 37091
     b = 2391
     c = 2099
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#256 Jack-O-Little (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jack','WaterJack']]):
     a = 25374
     b = 1954
     c = 2894
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#257 Jack-O-Little (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jack','WoodJack']]):
     a = 23781
     b = 2418
     c = 1696
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#258 Jack-O-Little (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jack','LightJack']]):
     a = 25143
     b = 3173
     c = 2281
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#259 Jack-O-Little (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jack','DarkJack']]):
     a = 38759
     b = 1813
     c = 2316
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#260 Jack-O-Little (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jean','FireJean']]):
     a = 37942
     b = 2194
     c = 1853
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#261 Jeanne (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jean','WaterJean']]):
     a = 27049
     b = 2220
     c = 3208
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#262 Jeanne (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jean','WoodJean']]):
     a = 23842
     b = 3262
     c = 2091
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#263 Jeanne (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jean','LightJean']]):
     a = 43560
     b = 1472
     c = 2337
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#264 Jeanne (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jean','DarkJean']]):
     a = 31544
     b = 2206
     c = 3153
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#265 Jeanne (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jell','FireJell']]):
     a = 25306
     b = 2615
     c = 1784
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#266 Jellai (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jell','WaterJell']]):
     a = 35599
     b = 1717
     c = 1915
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#267 Jellai (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jell','WoodJell']]):
     a = 30206
     b = 1763
     c = 1929
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#268 Jellai (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jell','LightJell']]):
     a = 22793
     b = 3405
     c = 2077
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#269 Jellai (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jell','DarkJell']]):
     a = 32698
     b = 2267
     c = 2311
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#270 Jellai (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jian','FireJian']]):
     a = 24918
     b = 1832
     c = 2772
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#271 Jiangshi (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jian','WaterJian']]):
     a = 38855
     b = 1799
     c = 1806
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#272 Jiangshi (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jian','WoodJian']]):
     a = 26345
     b = 2219
     c = 2358
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#273 Jiangshi (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jian','LightJian']]):
     a = 26552
     b = 3201
     c = 2247
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#274 Jiangshi (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jian','DarkJian']]):
     a = 27322
     b = 3255
     c = 2309
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#275 Jiangshi (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jinn','FireJinn']]):
     a = 26927
     b = 3337
     c = 2193
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#276 Jinn (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jinn','WaterJinn']]):
     a = 29957
     b = 2322
     c = 2595
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#277 Jinn (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jinn','WoodJinn']]):
     a = 28919
     b = 3018
     c = 1976
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#278 Jinn (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jinn','LightJinn']]):
     a = 25156
     b = 2404
     c = 2990
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#279 Jinn (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Jinn','DarkJinn']]):
     a = 38827
     b = 2294
     c = 1889
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#280 Jinn (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kiki','FireKiki']]):
     a = 25316
     b = 2335
     c = 2345
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#281 Kiki (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kiki','WaterKiki']]):
     a = 28742
     b = 1885
     c = 2038
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#282 Kiki (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kiki','WoodKiki']]):
     a = 25897
     b = 2751
     c = 1621
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#283 Kiki (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kiki','LightKiki']]):
     a = 26246
     b = 2452
     c = 3568
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#284 Kiki (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kiki','DarkKiki']]):
     a = 27744
     b = 3357
     c = 2309
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#285 Kiki (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Kilo','LightKilo']]):
     a = 29249
     b = 1321
     c = 2527
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#289 Kilobat (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Kilo','DarkKilo']]):
     a = 25776
     b = 2302
     c = 1471
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#290 Kilobat (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Latt','FireLatt']]):
     a = 26838
     b = 2622
     c = 1532
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#291 Latt (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Latt','WaterLatt']]):
     a = 38140
     b = 1574
     c = 1506
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#292 Latt (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Latt','WoodLatt']]):
     a = 30015
     b = 1620
     c = 1766
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#293 Latt (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Latt','LightLatt']]):
     a = 29688
     b = 2389
     c = 2501
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#294 Latt (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Latt','DarkLatt']]):
     a = 30652
     b = 2996
     c = 1907
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#295 Latt (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','FireLeo ']]):
     a = 26348
     b = 3173
     c = 2281
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#296 Leo (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','FireLeo ','SLeo ','FireSLeo ']]):
     a = 28990
     b = 3521
     c = 2520
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#297 Leo SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','WaterLeo ']]):
     a = 36941
     b = 2364
     c = 1813
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#298 Leo (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','WaterLeo ','SLeo ','WaterSLeo ']]):
     a = 40801
     b = 2603
     c = 1997
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#299 Leo SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','WoodLeo ']]):
     a = 30059
     b = 2363
     c = 3139
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#300 Leo (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','WoodLeo ','SLeo ','WoodSLeo ']]):
     a = 33069
     b = 2608
     c = 3487
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#301 Leo SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','LightLeo ']]):
     a = 27281
     b = 3139
     c = 2261
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#302 Leo (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','LightLeo ','SLeo ','LightSLeo ']]):
     a = 30018
     b = 3487
     c = 2492
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#303 Leo SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','DarkLeo ']]):
     a = 28091
     b = 3276
     c = 2002
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#304 Leo (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Leo ','DarkLeo ','SLeo ','DarkSLeo ']]):
     a = 30911
     b = 3637
     c = 2206
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#305 Leo SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Loki','FireLoki']]):
     a = 33856
     b = 2253
     c = 2229
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#306 Loki (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Loki','WaterLoki']]):
     a = 30556
     b = 3139
     c = 2023
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#307 Loki (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Loki','WoodLoki']]):
     a = 24496
     b = 2418
     c = 3391
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#308 Loki (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Loki','LightLoki']]):
     a = 31391
     b = 2430
     c = 2474
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#309 Loki (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Loki','DarkLoki']]):
     a = 36757
     b = 2180
     c = 2405
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#310 Loki (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lucy','FireLucy']]):
     a = 23494
     b = 3378
     c = 2349
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#311 Lucy (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lucy','WaterLucy']]):
     a = 28098
     b = 3276
     c = 2009
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#312 Lucy (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lucy','WoodLucy']]):
     a = 30689
     b = 2376
     c = 2481
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#313 Lucy (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lucy','LightLucy']]):
     a = 38984
     b = 2084
     c = 2405
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#314 Lucy (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lucy','DarkLucy']]):
     a = 27349
     b = 3439
     c = 2288
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#315 Lucy (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lumo','FireLumo']]):
     a = 25497
     b = 1648
     c = 1682
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#316 Lumo (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lumo','WaterLumo']]):
     a = 28977
     b = 1743
     c = 2384
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#317 Lumo (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lumo','WoodLumo']]):
     a = 29290
     b = 1410
     c = 1832
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#318 Lumo (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Lupi','FireLupi']]):
     a = 25122
     b = 3262
     c = 2295
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#321 Lupin (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lupi','WaterLupi']]):
     a = 41402
     b = 2391
     c = 1785
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#322 Lupin (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Lupi','WoodLupi']]):
     a = 30151
     b = 2614
     c = 2440
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#323 Lupin (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Lupi','DarkLupi']]):
     a = 27451
     b = 3310
     c = 2261
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#325 Lupin (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mamm','FireMamm']]):
     a = 35313
     b = 2364
     c = 2092
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#326 Mammont (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mamm','WaterMamm']]):
     a = 22793
     b = 3126
     c = 1989
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#327 Mammont (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mamm','WoodMamm']]):
     a = 30134
     b = 1907
     c = 3173
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#328 Mammont (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mamm','LightMamm']]):
     a = 34115
     b = 2253
     c = 2195
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#329 Mammont (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mamm','DarkMamm']]):
     a = 30611
     b = 3017
     c = 1982
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#330 Mammont (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mand','FireMand']]):
     a = 29385
     b = 2608
     c = 1886
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#331 Mandragora (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mand','WaterMand']]):
     a = 26838
     b = 2622
     c = 1512
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#332 Mandragora (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mand','WoodMand']]):
     a = 29603
     b = 1430
     c = 2833
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#333 Mandragora (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mand','LightMand']]):
     a = 30611
     b = 1907
     c = 3439
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#334 Mandragora (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mand','DarkMand']]):
     a = 30441
     b = 3187
     c = 1880
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#335 Mandragora (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mane','FireMane']]):
     a = 27049
     b = 2527
     c = 1403
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#336 Manelant (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mane','WaterMane']]):
     a = 36675
     b = 1710
     c = 1206
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#337 Manelant (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mane','WoodMane']]):
     a = 29334
     b = 1933
     c = 1895
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#338 Manelant (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Mari','FireMari']]):
     a = 20219
     b = 3037
     c = 2036
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#341 Mari (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mari','WaterMari']]):
     a = 28749
     b = 2521
     c = 2473
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#342 Mari (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mari','WoodMari']]):
     a = 26825
     b = 2581
     c = 1907
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#343 Mari (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mari','LightMari']]):
     a = 27649
     b = 2009
     c = 3568
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#344 Mari (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mari','DarkMari']]):
     a = 29549
     b = 3092
     c = 2118
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#345 Mari (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Medu','FireMedu']]):
     a = 34523
     b = 1642
     c = 1942
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#346 Medusa (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Medu','WaterMedu']]):
     a = 30403
     b = 2049
     c = 2025
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#347 Medusa (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Medu','WoodMedu']]):
     a = 29732
     b = 1580
     c = 2472
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#348 Medusa (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Medu','LightMedu']]):
     a = 27546
     b = 2956
     c = 2288
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#349 Medusa (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Medu','DarkMedu']]):
     a = 36056
     b = 1942
     c = 2432
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#350 Medusa (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mera','FireMera']]):
     a = 26212
     b = 3187
     c = 2261
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#351 Mera (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mera','WaterMera']]):
     a = 24445
     b = 2812
     c = 2828
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#352 Mera (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mera','WoodMera']]):
     a = 36757
     b = 2228
     c = 1881
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#353 Mera (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mera','LightMera']]):
     a = 30822
     b = 2043
     c = 2962
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#354 Mera (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mera','DarkMera']]):
     a = 39059
     b = 1853
     c = 2303
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#355 Mera (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Merl','FireMerl']]):
     a = 28037
     b = 3398
     c = 2554
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#356 Merlin (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Merl','WaterMerl']]):
     a = 31537
     b = 3494
     c = 2213
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#357 Merlin (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Merl','WoodMerl']]):
     a = 31037
     b = 2982
     c = 2787
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#358 Merlin (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Merl','LightMerl']]):
     a = 32222
     b = 3002
     c = 2924
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#359 Merlin (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Merl','DarkMerl']]):
     a = 40298
     b = 2398
     c = 2834
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#360 Merlin (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','FireMiho']]):
     a = 37363
     b = 2180
     c = 1806
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#361 Miho (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','FireMiho','SMiho','FireSMiho']]):
     a = 41265
     b = 2398
     c = 1990
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#362 Miho SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','WaterMiho']]):
     a = 31234
     b = 2096
     c = 2072
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#363 Miho (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','WaterMiho','SMiho','WaterSMiho']]):
     a = 34380
     b = 2318
     c = 2289
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#364 Miho SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','WoodMiho']]):
     a = 28207
     b = 2676
     c = 1798
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#365 Miho (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','WoodMiho','SMiho','WoodSMiho']]):
     a = 31033
     b = 2976
     c = 1982
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#366 Miho SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','LightMiho']]):
     a = 31701
     b = 2023
     c = 3085
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#367 Miho (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','LightMiho','SMiho','LightSMiho']]):
     a = 34881
     b = 2234
     c = 3425
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#368 Miho SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','DarkMiho']]):
     a = 37261
     b = 1806
     c = 2303
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#369 Miho (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Miho','DarkMiho','SMiho','DarkSMiho']]):
     a = 41156
     b = 1990
     c = 2535
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#370 Miho SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mild','FireMild']]):
     a = 26498
     b = 1730
     c = 1444
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#371 Mildeu (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mild','WaterMild']]):
     a = 25953
     b = 1614
     c = 2343
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#372 Mildeu (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mild','WoodMild']]):
     a = 28003
     b = 1342
     c = 1702
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#373 Mildeu (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mild','LightMild']]):
     a = 27975
     b = 1491
     c = 2499
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#374 Mildeu (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mild','DarkMild']]):
     a = 24768
     b = 1777
     c = 1662
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#375 Mildeu (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mimi','FireMimi']]):
     a = 26246
     b = 2206
     c = 1607
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#376 Mimic (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mimi','WaterMimi']]):
     a = 38555
     b = 1193
     c = 1792
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#377 Mimic (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mimi','WoodMimi']]):
     a = 28881
     b = 1668
     c = 2404
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#378 Mimic (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mimi','LightMimi']]):
     a = 27955
     b = 1403
     c = 1662
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#379 Mimic (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mimi','DarkMimi']]):
     a = 27816
     b = 1831
     c = 1664
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#380 Mimic (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Minica','FireMinica']]):
     a = 35279
     b = 1744
     c = 1452
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#381 Minicat (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Minica','WaterMinica']]):
     a = 28561
     b = 1648
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#382 Minicat (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Minica','WoodMinica']]):
     a = 23563
     b = 1818
     c = 1668
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#383 Minicat (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)







 if any([message.content.startswith (item) for item in ['MiniC','LightMiniC','Minicam','LightMinicam','Camilla','LightCami']]):
     a = 40046
     b = 2105
     c = 2242
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#389 Mini Camilla (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['MiniC','DarkMiniC','Minicam','DarkMinicam','Camilla','DarkCami']]):
     a = 41272
     b = 2119
     c = 2167
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#390 Mini Camilla (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['MiniS','LightMiniS','Minis','LightMinis','Seira','LightSeira']]):
     a = 24216
     b = 3425
     c = 2390
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#394 Mini Seira (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['MiniS','DarkMiniS','Minis','DarkMinis','Seira','DarkSeira']]):
     a = 24216
     b = 3425
     c = 2390
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#395 Mini Seira (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['MiniT','LightMiniT','Minit','LightMinit','Tina','LightTina']]):
     a = 21492
     b = 3357
     c = 2384
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#399 Mini Tina (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['MiniT','DarkMiniT','Minit','DarkMinit','Tina','DarkTina']]):
     a = 24816
     b = 3378
     c = 2479
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#400 Mini Tina (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mino','FireMino']]):
     a = 24713
     b = 2452
     c = 1682
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#401 Mino (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mino','WaterMino']]):
     a = 25885
     b = 2370
     c = 1498
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#402 Mino (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mino','WoodMino']]):
     a = 26246
     b = 2172
     c = 1696
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#403 Mino (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mino','LightMino']]):
     a = 22384
     b = 2642
     c = 1539
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#404 Mino (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mino','DarkMino']]):
     a = 29188
     b = 2336
     c = 1308
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#405 Mino (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mish','FireMish']]):
     a = 35395
     b = 1922
     c = 1622
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#406 Misha (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mish','WaterMish']]):
     a = 29293
     b = 2083
     c = 2011
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#407 Misha (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mish','WoodMish']]):
     a = 25476
     b = 1866
     c = 2969
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#408 Misha (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mish','LightMish']]):
     a = 40312
     b = 2221
     c = 2364
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#409 Misha (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mish','DarkMish']]):
     a = 26287
     b = 2663
     c = 3105
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#410 Misha (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mole','FireMole']]):
     a = 28731
     b = 1709
     c = 2486
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#411 Moler (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mole','WaterMole']]):
     a = 36069
     b = 1622
     c = 1329
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#412 Moler (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mole','WoodMole']]):
     a = 28857
     b = 1831
     c = 1637
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#413 Moler (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Mona','FireMona']]):
     a = 42627
     b = 1431
     c = 1418
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#416 Mona (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mona','WaterMona']]):
     a = 25081
     b = 2853
     c = 2016
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#417 Mona (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mona','WoodMona']]):
     a = 27860
     b = 1491
     c = 2554
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#418 Mona (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mona','LightMona']]):
     a = 30686
     b = 2486
     c = 3051
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#419 Mona (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mona','DarkMona']]):
     a = 28030
     b = 3228
     c = 1954
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#420 Mona (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Monk','FireMonk']]):
     a = 27676
     b = 2867
     c = 1914
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#421 Monkiki (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Monk','WaterMonk']]):
     a = 28697
     b = 1852
     c = 2588
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#422 Monkiki (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Monk','WoodMonk']]):
     a = 28476
     b = 1892
     c = 1963
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#423 Monkiki (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Monk','LightMonk']]):
     a = 26917
     b = 2662
     c = 2658
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#424 Monkiki (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Monk','DarkMonk']]):
     a = 28731
     b = 1941
     c = 3167
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#425 Monkiki (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mowg','FireMowg']]):
     a = 26900
     b = 2717
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#426 Mowgli (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mowg','WaterMowg']]):
     a = 28670
     b = 2615
     c = 1648
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#427 Mowgli (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mowg','WoodMowg']]):
     a = 26900
     b = 2847
     c = 1532
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#428 Mowgli (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mowg','LightMowg']]):
     a = 28016
     b = 3133
     c = 2036
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#429 Mowgli (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mowg','DarkMowg']]):
     a = 27288
     b = 3085
     c = 2193
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#430 Mowgli (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mush','FireMush']]):
     a = 29092
     b = 1321
     c = 2540
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#431 Mushi (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mush','WaterMush']]):
     a = 28054
     b = 1879
     c = 1725
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#432 Mushi (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Mush','WoodMush']]):
     a = 23862
     b = 2445
     c = 1539
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#433 Mushi (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Nezh','FireNezh']]):
     a = 38643
     b = 2323
     c = 1806
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#436 Nezha (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nezh','WaterNezh']]):
     a = 30199
     b = 2444
     c = 2542
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#437 Nezha (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nezh','WoodNezh']]):
     a = 27696
     b = 3092
     c = 2329
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#438 Nezha (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nezh','LightNezh']]):
     a = 38752
     b = 1853
     c = 2323
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#439 Nezha (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nezh','DarkNezh']]):
     a = 25640
     b = 3153
     c = 2431
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#440 Nezha (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Nifa','LightNifa']]):
     a = 25292
     b = 3024
     c = 2288
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#444 Nifa (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nifa','DarkNifa']]):
     a = 47027
     b = 1853
     c = 1915
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#445 Nifa (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nigh','FireNigh']]):
     a = 32000
     b = 3616
     c = 2172
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#446 Nightmare (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nigh','WaterNigh']]):
     a = 27247
     b = 2601
     c = 3514
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#447 Nightmare (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nigh','WoodNigh']]):
     a = 26906
     b = 2595
     c = 3602
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#448 Nightmare (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nigh','LightNigh']]):
     a = 28221
     b = 2561
     c = 3875
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#449 Nightmare (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Nigh','DarkNigh']]):
     a = 41143
     b = 2316
     c = 2534
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#450 Nightmare (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Odin','FireOdin']]):
     a = 43077
     b = 2010
     c = 3066
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#451 Odin (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Odin','WaterOdin']]):
     a = 25378
     b = 3172
     c = 3155
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#452 Odin (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Odin','WoodOdin']]):
     a = 28473
     b = 3909
     c = 2595
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#453 Odin (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Odin','LightOdin']]):
     a = 41919
     b = 2099
     c = 2916
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#454 Odin (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Odin','DarkOdin']]):
     a = 32024
     b = 2975
     c = 2828
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#455 Odin (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Onmy','FireOnmy']]):
     a = 37772
     b = 2521
     c = 2705
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#456 Onmyouji (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Onmy','WaterOnmy']]):
     a = 31626
     b = 3677
     c = 2070
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#457 Onmyouji (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Onmy','WoodOnmy']]):
     a = 29569
     b = 2363
     c = 3562
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#458 Onmyouji (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Onmy','LightOnmy']]):
     a = 25068
     b = 2792
     c = 3609
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#459 Onmyouji (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Onmy','DarkOnmy']]):
     a = 25878
     b = 3698
     c = 2479
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#460 Onmyouji (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Otar','FireOtar']]):
     a = 35048
     b = 1635
     c = 1302
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#461 Otari (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Otar','WaterOtar']]):
     a = 28687
     b = 1742
     c = 1854
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#462 Otari (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Otar','WoodOtar']]):
     a = 28820
     b = 1478
     c = 2336
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#463 Otari (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Otar','LightOtar']]):
     a = 25667
     b = 2574
     c = 1709
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#464 Otari (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Otar','DarkOtar']]):
     a = 28473
     b = 1873
     c = 2724
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#465 Otari (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pebb','FirePebb']]):
     a = 29773
     b = 2240
     c = 3058
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#466 Pebbol (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)






 if any([message.content.startswith (item) for item in ['Pega','FirePega']]):
     a = 25619
     b = 3208
     c = 2309
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#471 Pegasus (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pega','WaterPega']]):
     a = 27666
     b = 2328
     c = 2610
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#472 Pegasus (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pega','WoodPega']]):
     a = 30522
     b = 2261
     c = 3099
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#473 Pegasus (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pega','LightPega']]):
     a = 30849
     b = 2036
     c = 3221
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#474 Pegasus (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pega','DarkPega']]):
     a = 27560
     b = 3242
     c = 2193
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#475 Pegasus (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Penp','FirePenp']]):
     a = 31033
     b = 1199
     c = 2581
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#476 Penpen (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Penp','WaterPenp']]):
     a = 27969
     b = 1342
     c = 2506
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#477 Penpen (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Penp','WoodPenp']]):
     a = 39951
     b = 1506
     c = 1145
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#478 Penpen (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Penp','LightPenp']]):
     a = 28806
     b = 1866
     c = 2418
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#479 Penpen (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Penp','DarkPenp']]):
     a = 26041
     b = 2588
     c = 1696
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#480 Penpen (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pers','FirePers']]):
     a = 30110
     b = 3077
     c = 2801
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#481 Persephone (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pers','WaterPers']]):
     a = 32494
     b = 2784
     c = 2883
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#482 Persephone (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pers','WoodPers']]):
     a = 32800
     b = 2737
     c = 2903
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#483 Persephone (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pers','LightPers']]):
     a = 31094
     b = 2649
     c = 3548
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#484 Persephone (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pers','DarkPers']]):
     a = 27151
     b = 3834
     c = 2704
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#485 Persephone (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Peyo','FirePeyo']]):
     a = 36451
     b = 1418
     c = 1411
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#486 Peyote (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Peyo','WaterPeyo']]):
     a = 24090
     b = 2171
     c = 2147
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#487 Peyote (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Peyo','WoodPeyo']]):
     a = 29453
     b = 1342
     c = 2445
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#488 Peyote (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Peyo','LightPeyo']]):
     a = 27972
     b = 1892
     c = 1725
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#489 Peyote (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Peyo','DarkPeyo']]):
     a = 35375
     b = 1554
     c = 1758
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#490 Peyote (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Phib','FirePhib']]):
     a = 29889
     b = 2860
     c = 1709
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#491 Phibian (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Phib','WaterPhib']]):
     a = 46993
     b = 1499
     c = 1479
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#492 Phibian (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Phib','WoodPhib']]):
     a = 35974
     b = 1953
     c = 1889
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#493 Phibian (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Phib','LightPhib']]):
     a = 26096
     b = 2424
     c = 3269
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#494 Phibian (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Phib','DarkPhib']]):
     a = 32017
     b = 2580
     c = 2576
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#495 Phibian (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pinc','FirePinc']]):
     a = 38678
     b = 1247
     c = 1683
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#496 Pinchee (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pinc','WaterPinc']]):
     a = 29147
     b = 2302
     c = 1328
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#497 Pinchee (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pinc','WoodPinc']]):
     a = 29930
     b = 1471
     c = 2275
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#498 Pinchee (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)






 if any([message.content.startswith (item) for item in ['Pino','WoodPino']]):
     a = 21308
     b = 2315
     c = 1730
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#503 Pinolo (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
     a = 11724
     b = 1063
     c = 1063
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#504 Pinolo (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
     a = 10770
     b = 1102
     c = 1112
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#505 Pinolo (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Pino','WoodPino']]):
     a = 2152
     b = 402
     c = 197
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#508 Pinolo Lie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
     a = 2149
     b = 103
     c = 103
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#509 Pinolo Lie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
     a = 1195
     b = 142
     c = 152
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#510 Pinolo Lie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pixi','FirePixi']]):
     a = 33202
     b = 2099
     c = 2180
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#511 Pixie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pixi','WaterPixi']]):
     a = 29753
     b = 2125
     c = 2002
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#512 Pixie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pixi','WoodPixi']]):
     a = 28262
     b = 2431
     c = 2138
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#513 Pixie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pixi','LightPixi']]):
     a = 29113
     b = 1907
     c = 2322
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#514 Pixie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pixi','DarkPixi']]):
     a = 24543
     b = 2343
     c = 2125
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#515 Pixie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pose','FirePose']]):
     a = 40312
     b = 2187
     c = 2677
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#516 Poseidon (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pose','WaterPose']]):
     a = 28513
     b = 3391
     c = 2588
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#517 Poseidon (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pose','WoodPose']]):
     a = 27281
     b = 2792
     c = 3773
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#518 Poseidon (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pose','LightPose']]):
     a = 24216
     b = 3854
     c = 2635
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#519 Poseidon (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Pose','DarkPose']]):
     a = 29732
     b = 2281
     c = 3602
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#520 Poseidon (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Rabb','WoodRabb']]):
     a = 28840
     b = 1784
     c = 2717
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#523 Rabbitle (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Rabb','LightRabb']]):
     a = 29208
     b = 3139
     c = 2152
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#524 Rabbitle (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Rabb','DarkRabb']]):
     a = 35906
     b = 2439
     c = 2146
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#525 Rabbitle (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Radi','FireRadi']]):
     a = 26709
     b = 2527
     c = 1811
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#526 Radis (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Radi','WaterRadi']]):
     a = 34353
     b = 1874
     c = 1540
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#527 Radis (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Radi','WoodRadi']]):
     a = 28936
     b = 1832
     c = 2411
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#528 Radis (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Radi','LightRadi']]):
     a = 24380
     b = 3126
     c = 2581
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#529 Radis (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Radi','DarkRadi']]):
     a = 29998
     b = 2111
     c = 3187
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#530 Radis (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ramu','FireRamu']]):
     a = 26552
     b = 2792
     c = 1682
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#531 Ramu (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ramu','WaterRamu']]):
     a = 25204
     b = 1954
     c = 2983
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#532 Ramu (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ramu','WoodRamu']]):
     a = 28817
     b = 2137
     c = 1970
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#533 Ramu (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ramu','LightRamu']]):
     a = 30335
     b = 2784
     c = 2399
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#534 Ramu (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Ramu','DarkRamu']]):
     a = 37281
     b = 2044
     c = 2487
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#535 Ramu (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Robo','LightRobo']]):
     a = 27165
     b = 2547
     c = 1403
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#539 Robobot (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Robo','DarkRobo']]):
     a = 27972
     b = 1892
     c = 1725
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#540 Robobot (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Roca','FireRoca']]):
     a = 36451
     b = 1418
     c = 1411
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#541 Roca (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Roca','WaterRoca']]):
     a = 24090
     b = 2171
     c = 2147
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#542 Roca (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Roca','WoodRoca']]):
     a = 29453
     b = 1342
     c = 2445
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#543 Roca (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)







 if any([message.content.startswith (item) for item in ['Rock','LightRock']]):
     a = 24271
     b = 2458
     c = 3187
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#549 Rocky (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Rock','DarkRobo']]):
     a = 24414
     b = 3024
     c = 2138
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#550 Rocky (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Rowa','WoodRowa']]):
     a = 37602
     b = 1193
     c = 1840
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#553 Rowan (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)






 if any([message.content.startswith (item) for item in ['Rudo','WoodRudo']]):
     a = 26389
     b = 2642
     c = 1539
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#558 Rudolph (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Rudo','LightRudo']]):
     a = 26470
     b = 2492
     c = 3269
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#559 Rudolph (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Rudo','DarkRudo']]):
     a = 28084
     b = 3208
     c = 2023
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#560 Rudolph (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sand','FireSand']]):
     a = 22568
     b = 2077
     c = 2935
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#561 Sand Wraith (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sand','WaterSand']]):
     a = 23566
     b = 2362
     c = 2331
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#562 Sand Wraith (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sand','WoodSand']]):
     a = 31391
     b = 1942
     c = 2092
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#563 Sand Wraith (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sand','LightSand']]):
     a = 37493
     b = 2473
     c = 2214
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#564 Sand Wraith (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sand','DarkSand']]):
     a = 26634
     b = 3391
     c = 2424
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#565 Sand Wraith (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sanz','FireSanz']]):
     a = 29671
     b = 2520
     c = 3562
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#566 Sanzang (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sanz','WaterSanz']]):
     a = 24611
     b = 2492
     c = 3698
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#567 Sanzang (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sanz','WoodSanz']]):
     a = 35770
     b = 2739
     c = 2568
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#568 Sanzang (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sanz','LightSanz']]):
     a = 34803
     b = 2716
     c = 2624
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#569 Sanzang (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sanz','DarkSanz']]):
     a = 24141
     b = 3848
     c = 2601
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#570 Sanzang (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seas','FireSeas']]):
     a = 22650
     b = 2622
     c = 1852
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#571 Seastar (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seas','WaterSeas']]):
     a = 24346
     b = 2472
     c = 1771
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#572 Seastar (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seas','WoodSeas']]):
     a = 28687
     b = 1981
     c = 1773
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#573 Seastar (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seas','LightSeas']]):
     a = 38174
     b = 2017
     c = 1983
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#574 Seastar (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seas','DarkSeas']]):
     a = 31442
     b = 2036
     c = 2962
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#575 Seastar (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seed','FireSeed']]):
     a = 28030
     b = 1873
     c = 2676
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#576 Seedler (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seed','WaterSeed']]):
     a = 27931
     b = 2165
     c = 2066
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#577 Seedler (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seed','WoodSeed']]):
     a = 37173
     b = 1792
     c = 1976
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#578 Seedler (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seed','LightSeed']]):
     a = 28806
     b = 1954
     c = 3344
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#579 Seedler (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seed','DarkSeed']]):
     a = 27560
     b = 3064
     c = 2159
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#580 Seedler (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seir','FireSeir']]):
     a = 30822
     b = 1696
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#581 Seiren (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seir','WaterSeir']]):
     a = 27982
     b = 1920
     c = 2016
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#582 Seiren (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seir','WoodSeir']]):
     a = 26327
     b = 1900
     c = 1559
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#583 Seiren (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seir','LightSeir']]):
     a = 24713
     b = 2424
     c = 3337
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#584 Seiren (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Seir','DarkSeir']]):
     a = 24523
     b = 2322
     c = 2118
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#585 Seiren (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sha','FireSha']]):
     a = 30059
     b = 3596
     c = 2206
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#586 Sha Wujing (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sha','WaterSha']]):
     a = 31295
     b = 2934
     c = 2944
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#587 Sha Wujing (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sha','WoodSha']]):
     a = 32698
     b = 2907
     c = 2856
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#588 Sha Wujing (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sha','LightSha']]):
     a = 30883
     b = 2622
     c = 3596
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#589 Sha Wujing (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sha','DarkSha']]):
     a = 28643
     b = 3732
     c = 2465
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#590 Sha Wujing (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shel','FireShel']]):
     a = 29293
     b = 2001
     c = 1705
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#591 Shellie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shel','WaterShel']]):
     a = 29440
     b = 2996
     c = 1641
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#592 Shellie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shel','WoodShel']]):
     a = 25360
     b = 1784
     c = 2663
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#593 Shellie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Sher','FireSher']]):
     a = 25878
     b = 2724
     c = 1580
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#596 Sherlock (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sher','WaterSher']]):
     a = 28507
     b = 2622
     c = 1641
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#597 Sherlock (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sher','WoodSher']]):
     a = 26300
     b = 2813
     c = 1696
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#598 Sherlock (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sher','LightSher']]):
     a = 29794
     b = 3221
     c = 2091
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#599 Sherlock (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Shin','FireShin']]):
     a = 32106
     b = 3057
     c = 2883
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#601 Shinobi (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shin','WaterShin']]):
     a = 25483
     b = 3303
     c = 3071
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#602 Shinobi (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shin','WoodShin']]):
     a = 41436
     b = 2017
     c = 2807
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#603 Shinobi (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shin','LightShin']]):
     a = 26334
     b = 3889
     c = 2935
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#604 Shinobi (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shin','DarkShin']]):
     a = 27063
     b = 3296
     c = 2704
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#605 Shinobi (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shiv','FireShiv']]):
     a = 27689
     b = 2295
     c = 3494
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#606 Shiva (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shiv','WaterShiv']]):
     a = 49104
     b = 2214
     c = 2398
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#607 Shiva (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shiv','WoodShiv']]):
     a = 28541
     b = 3902
     c = 2819
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#608 Shiva (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shiv','LightShiv']]):
     a = 49376
     b = 2568
     c = 2126
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#609 Shiva (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Shiv','DarkShiv']]):
     a = 32273
     b = 2349
     c = 3562
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#610 Shiva (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sieg','FireSieg']]):
     a = 24625
     b = 4018
     c = 2629
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#611 Siegfried (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sieg','WaterSieg']]):
     a = 28221
     b = 3269
     c = 2629
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#612 Siegfried (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sieg','WoodSieg']]):
     a = 39747
     b = 2677
     c = 2235
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#613 Siegfried (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sieg','LightSieg']]):
     a = 31295
     b = 3023
     c = 2692
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#614 Siegfried (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sieg','DarkSieg']]):
     a = 31578
     b = 2213
     c = 3807
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#615 Siegfried (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['SlimeSo','FireSlimeSo','Slimeso','FireSlimeso']]):
     a = 25783
     b = 3044
     c = 2029
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#621 Slimesoldier (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['SlimeSo','WaterSlimeSo','Slimeso','WaterSlimeso']]):
     a = 24182
     b = 2370
     c = 3064
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#622 Slimesoldier (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['SlimeSo','WoodSlimeSo','Slimeso','WoodSlimeso']]):
     a = 27117
     b = 2738
     c = 2179
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#623 Slimesoldier (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['SlimeSo','LightSlimeSo','Slimeso','LightSlimeso']]):
     a = 27070
     b = 3058
     c = 2275
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#624 Slimesoldier (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['SlimeSo','DarkSlimeSo','Slimeso','DarkSlimeso']]):
     a = 37288
     b = 1887
     c = 2180
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#625 Slimesoldier (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)

     
 if message.content.startswith("SlimeSo"):
     return
     
 if message.content.startswith("FireSlimeSo"):
     return
     
 if message.content.startswith("WaterSlimeSo"):
     return
     
 if message.content.startswith("WoodSlimeSo"):
     return
     
 if message.content.startswith("LightSlimeSo"):
     return
     
 if message.content.startswith("DarkSlimeSo"):
     return
     
 if message.content.startswith("Slimeso"):
     return
     
 if message.content.startswith("FireSlimeso"):
     return
     
 if message.content.startswith("WaterSlimeso"):
     return
     
 if message.content.startswith("WoodSlimeso"):
     return
     
 if message.content.startswith("LightSlimeso"):
     return
     
 if message.content.startswith("DarkSlimeso"):
     return



 if any([message.content.startswith (item) for item in ['Slim','FireSlim']]):
     a = 26246
     b = 1702
     c = 1444
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#616 Slime (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Slim','WaterSlim']]):
     a = 24516
     b = 1777
     c = 2343
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#617 Slime (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Slim','WoodSlim']]):
     a = 26144
     b = 2322
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#618 Slime (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Slim','LightSlim']]):
     a = 28946
     b = 1708
     c = 1766
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#619 Slime (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Slim','DarkSlim']]):
     a = 37792
     b = 1411
     c = 1370
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#620 Slime (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)



 if any([message.content.startswith (item) for item in ['Snow','WaterSnow']]):
     a = 43240
     b = 1622
     c = 1261
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#627 Snowee (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Snow','LightSnow']]):
     a = 26368
     b = 3276
     c = 2247
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#629 Snowee (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Snow','DarkSnow']]):
     a = 32337
     b = 2614
     c = 2672
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#630 Snowee (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','FireSpar']]):
     a = 36587
     b = 1962
     c = 2316
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#631 Sparkitt (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','WaterSpar']]):
     a = 30672
     b = 3173
     c = 1900
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#632 Sparkitt (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','WoodSpar']]):
     a = 24737
     b = 2805
     c = 2576
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#633 Sparkitt (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','LightSpar']]):
     a = 30815
     b = 3303
     c = 1920
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#634 Sparkitt (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','DarkSpar']]):
     a = 37152
     b = 2024
     c = 2432
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#635 Sparkitt (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','FireSpar']]):
     a = 35531
     b = 1363
     c = 1772
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#636 Sparkler (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','WaterSpar']]):
     a = 29082
     b = 1538
     c = 1793
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#637 Sparkler (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','WoodSpar']]):
     a = 25102
     b = 1682
     c = 1600
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#638 Sparkler (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','LightSpar']]):
     a = 27860
     b = 1355
     c = 2418
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#639 Sparkler (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Spar','DarkSpar']]):
     a = 23433
     b = 2275
     c = 1662
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#640 Sparkler (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sphy','FireSphy']]):
     a = 35586
     b = 2494
     c = 2044
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#641 Sphynx (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sphy','WaterSphy']]):
     a = 25442
     b = 2390
     c = 3235
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#642 Sphynx (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sphy','WoodSphy']]):
     a = 25415
     b = 3221
     c = 2452
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#643 Sphynx (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sphy','LightSphy']]):
     a = 30890
     b = 3391
     c = 1968
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#644 Sphynx (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sphy','DarkSphy']]):
     a = 27768
     b = 3002
     c = 2753
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#645 Sphynx (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Squi','FireSqui']]):
     a = 29906
     b = 1654
     c = 1752
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#646 Squirrus (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Squi','WaterSqui']]):
     a = 24720
     b = 1607
     c = 2322
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#647 Squirrus (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Squi','WoodSqui']]):
     a = 22514
     b = 2574
     c = 1539
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#648 Squirrus (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Star','FireStar']]):
     a = 26041
     b = 2486
     c = 1457
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#651 Starrov (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Star','WaterStar']]):
     a = 29947
     b = 1593
     c = 1766
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#652 Starrov (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Star','WoodStar']]):
     a = 26518
     b = 2377
     c = 1696
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#653 Starrov (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Succ','FireSucc']]):
     a = 26327
     b = 3167
     c = 2288
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#656 Succubus (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','FireSucc','SSucc','FireSSucc']]):
     a = 28970
     b = 3514
     c = 2527
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#657 Succubus SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','WaterSucc']]):
     a = 37057
     b = 2146
     c = 2473
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#658 Succubus (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','WaterSucc','SSucc','WaterSSucc']]):
     a = 40931
     b = 2364
     c = 2725
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#659 Succubus SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','WoodSucc']]):
     a = 31329
     b = 2321
     c = 2352
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#660 Succubus (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','WoodSucc','SSucc','WoodSSucc']]):
     a = 34488
     b = 2563
     c = 2596
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#661 Succubus SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','LightSucc']]):
     a = 36812
     b = 1976
     c = 2323
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#662 Succubus (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','LightSucc','SSucc','LightSSucc']]):
     a = 40658
     b = 2174
     c = 2562
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#663 Succubus SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','DarkSucc']]):
     a = 30012
     b = 2343
     c = 3173
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#664 Succubus (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Succ','DarkSucc','SSucc','DarkSSucc']]):
     a = 33022
     b = 2581
     c = 3521
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#665 Succubus SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sun','FireSun','Wukong','FireWukong']]):
     a = 28262
     b = 3473
     c = 2479
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#666 Sun Wukong (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sun','WaterSun','Wukong','WaterWukong']]):
     a = 29801
     b = 3323
     c = 2799
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#667 Sun Wukong (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sun','WoodSun','Wukong','WoodWukong']]):
     a = 33328
     b = 3405
     c = 2213
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#668 Sun Wukong (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sun','LightSun','Wukong','LightWukong']]):
     a = 38494
     b = 2705
     c = 2364
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#669 Sun Wukong (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sun','DarkSun','Wukong','DarkWukong']]):
     a = 32153
     b = 2743
     c = 2747
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#670 Sun Wukong (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sura','FireSura']]):
     a = 22984
     b = 3262
     c = 2084
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#671 Sura (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sura','WaterSura']]):
     a = 38412
     b = 2044
     c = 2017
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#672 Sura (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sura','WoodSura']]):
     a = 29787
     b = 2288
     c = 3105
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#673 Sura (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sura','LightSura']]):
     a = 31772
     b = 2532
     c = 2542
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#674 Sura (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Sura','DarkSura']]):
     a = 25367
     b = 3126
     c = 2343
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#675 Sura (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Tai ','LightTai']]):
     a = 28667
     b = 1722
     c = 1854
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#679 Tai (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tai ','DarkTai']]):
     a = 29324
     b = 1369
     c = 2418
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#680 Tai (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tany','FireTany']]):
     a = 24414
     b = 2622
     c = 1832
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#681 Tanya (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Tany','LightTany']]):
     a = 27608
     b = 3058
     c = 2309
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#684 Tanya (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tany','DarkTany']]):
     a = 30822
     b = 2050
     c = 3099
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#685 Tanya (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Thor','FireThor']]):
     a = 26865
     b = 2220
     c = 3037
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#686 Thor (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Thor','WaterThor']]):
     a = 26484
     b = 3003
     c = 2111
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#687 Thor (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Thor','WoodThor']]):
     a = 30819
     b = 2648
     c = 2535
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#688 Thor (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Thor','LightThor']]):
     a = 41374
     b = 1717
     c = 2494
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#689 Thor (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Thor','DarkThor']]):
     a = 25538
     b = 2887
     c = 2411
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#690 Thor (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tiga','FireTiga']]):
     a = 24445
     b = 2832
     c = 2862
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#691 Tigar (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tiga','WaterTiga']]):
     a = 26729
     b = 2193
     c = 3051
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#692 Tigar (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tiga','WoodTiga']]):
     a = 30625
     b = 3139
     c = 1900
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#693 Tigar (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tiga','LightTiga']]):
     a = 29521
     b = 3126
     c = 2118
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#694 Tigar (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Tiga','DarkTiga']]):
     a = 37009
     b = 1983
     c = 2010
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#695 Tigar (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Toad','LightToad']]):
     a = 28817
     b = 2491
     c = 2311
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#699 Toadora (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Toad','DarkToad']]):
     a = 30761
     b = 1920
     c = 3187
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#700 Toadora (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Truf','FireTruf']]):
     a = 34898
     b = 1499
     c = 1806
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#701 Truffel (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Truf','DarkTruf']]):
     a = 28387
     b = 1750
     c = 2744
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#705 Truffel (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Valk','FireValk']]):
     a = 35443
     b = 2703
     c = 2842
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#706 Valkyrie (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Valk','WaterValk']]):
     a = 25408
     b = 3671
     c = 2581
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#707 Valkyrie (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Valk','WoodValk']]):
     a = 30288
     b = 2893
     c = 2937
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#708 Valkyrie (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Valk','LightValk']]):
     a = 31003
     b = 3104
     c = 2808
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#709 Valkyrie (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Valk','DarkValk']]):
     a = 48498
     b = 2167
     c = 2357
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#710 Valkyrie (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vamp','FireVamp']]):
     a = 26368
     b = 3024
     c = 2254
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#711 Vampire (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vamp','WaterVamp']]):
     a = 26416
     b = 3262
     c = 2043
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#712 Vampire (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vamp','WoodVamp']]):
     a = 31629
     b = 2205
     c = 2352
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#713 Vampire (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vamp','LightVamp']]):
     a = 27969
     b = 3310
     c = 2002
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#714 Vampire (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vamp','DarkVamp']]):
     a = 30672
     b = 1873
     c = 3167
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#715 Vampire (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Venu','LightVenu']]):
     a = 37452
     b = 1881
     c = 2521
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#719 Venus (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Venu','DarkVenu']]):
     a = 26859
     b = 2118
     c = 3153
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#720 Venus (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Verd','FireVerd']]):
     a = 27713
     b = 2573
     c = 2576
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#721 Verde (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Verd','WaterVerd']]):
     a = 32051
     b = 2491
     c = 2501
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#722 Verde (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Verd','WoodVerd']]):
     a = 44160
     b = 1894
     c = 1881
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#723 Verde (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Verd','LightVerd']]):
     a = 38848
     b = 1813
     c = 2337
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#724 Verde (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Verd','DarkVerd']]):
     a = 30979
     b = 2813
     c = 2533
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#725 Verde (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','FireVict']]):
     a = 30516
     b = 1900
     c = 3310
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#726 Victoria (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','FireVict','SVict','FireSVict']]):
     a = 33573
     b = 2097
     c = 3671
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#727 Victoria SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','WaterVict']]):
     a = 27097
     b = 3126
     c = 2213
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#728 Victoria (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','WaterVict','SVict','WaterSVict']]):
     a = 29814
     b = 3473
     c = 2445
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#729 Victoria SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','WoodVict']]):
     a = 42478
     b = 2085
     c = 1860
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#730 Victoria (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','WoodVict','SVict','WoodSVict']]):
     a = 46890
     b = 2296
     c = 2051
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#731 Victoria SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','LightVict']]):
     a = 29889
     b = 2295
     c = 3296
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#732 Victoria (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','LightVict','SVict','LightSVict']]):
     a = 32885
     b = 2533
     c = 3657
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#733 Victoria SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','DarkVict']]):
     a = 30580
     b = 2165
     c = 2481
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#734 Victoria (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Vict','DarkVict','SVict','DarkSVict']]):
     a = 33664
     b = 2392
     c = 2739
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#735 Victoria SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wend','FireWend']]):
     a = 27077
     b = 2547
     c = 1559
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#736 Wendigo (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wend','WaterWend']]):
     a = 27758
     b = 1668
     c = 2615
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#737 Wendigo (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wend','WoodWend']]):
     a = 27182
     b = 2396
     c = 1582
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#738 Wendigo (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wend','LightWend']]):
     a = 27063
     b = 3105
     c = 2247
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#739 Wendigo (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wend','DarkWend']]):
     a = 30492
     b = 2478
     c = 2406
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#740 Wendigo (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','FireWild']]):
     a = 27015
     b = 3058
     c = 2295
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#741 Wildfang (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','FireWild','SWild','FireSWild']]):
     a = 29726
     b = 3398
     c = 2533
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#742 Wildfang SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','WaterWild']]):
     a = 39611
     b = 2221
     c = 1840
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#743 Wildfang (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','WaterWild','SWild','WaterSWild']]):
     a = 43737
     b = 2446
     c = 2024
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#744 Wildfang SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','WoodWild']]):
     a = 31496
     b = 2254
     c = 2921
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#745 Wildfang (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','WoodWild','SWild','WoodSWild']]):
     a = 34646
     b = 2486
     c = 3248
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#746 Wildfang SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','LightWild']]):
     a = 30730
     b = 2607
     c = 2488
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#747 Wildfang (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','LightWild','SWild','LightSWild']]):
     a = 33828
     b = 2876
     c = 2745
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#748 Wildfang SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','DarkWild']]):
     a = 27240
     b = 2996
     c = 2281
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#749 Wildfang (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wild','DarkWild','SWild','DarkSWild']]):
     a = 29971
     b = 3330
     c = 2520
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#750 Wildfang SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)





 if any([message.content.startswith (item) for item in ['Wool','LightWool']]):
     a = 28731
     b = 1873
     c = 2765
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#754 Woolf (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wool','DarkWool']]):
     a = 35817
     b = 1676
     c = 1996
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#755 Woolf (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Worm','FireWorm']]):
     a = 34898
     b = 1404
     c = 1445
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#756 Wormtail (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Worm','WaterWorm']]):
     a = 37792
     b = 1132
     c = 1853
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#757 Wormtail (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Worm','WoodWorm']]):
     a = 25742
     b = 2281
     c = 1525
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#758 Wormtail (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Wumo','FireWumo']]):
     a = 28377
     b = 1696
     c = 2615
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#761 Wumoo (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wumo','WaterWumo']]):
     a = 28561
     b = 1737
     c = 2404
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#762 Wumoo (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Wumo','WoodWumo']]):
     a = 35838
     b = 1275
     c = 1751
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#763 Wumoo (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)




 if any([message.content.startswith (item) for item in ['Yaks','FireYaks']]):
     a = 30093
     b = 2322
     c = 3037
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#766 Yaksha (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yaks','WaterYaks']]):
     a = 29589
     b = 3153
     c = 2152
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#767 Yaksha (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yaks','WoodYaks']]):
     a = 29869
     b = 3126
     c = 2125
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#768 Yaksha (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yaks','LightYaks']]):
     a = 26559
     b = 3269
     c = 2084
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#769 Yaksha (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yaks','DarkYaks']]):
     a = 30696
     b = 2641
     c = 2542
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#770 Yaksha (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yeti','FireYeti']]):
     a = 28200
     b = 2785
     c = 1614
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#771 Yeti (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yeti','WaterYeti']]):
     a = 28840
     b = 1989
     c = 2581
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#772 Yeti (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yeti','WoodYeti']]):
     a = 33434
     b = 1894
     c = 1976
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#773 Yeti (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yeti','LightYeti']]):
     a = 28241
     b = 2418
     c = 3133
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#774 Yeti (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yeti','DarkYeti']]):
     a = 35245
     b = 2192
     c = 2134
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#775 Yeti (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','FireYuki']]):
     a = 26947
     b = 3105
     c = 2240
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#776 Yuki (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','FireYuki','SYuki','FireSYuki']]):
     a = 29651
     b = 3446
     c = 2472
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#777 Yuki SE (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','WaterYuki']]):
     a = 36982
     b = 2024
     c = 1976
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#778 Yuki (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','WaterYuki','SYuki','WaterSYuki']]):
     a = 40849
     b = 2228
     c = 2174
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#779 Yuki SE (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','WoodYuki']]):
     a = 28857
     b = 2546
     c = 2345
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#780 Yuki (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','WoodYuki','SYuki','WoodSYuki']]):
     a = 31764
     b = 2808
     c = 2589
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#781 Yuki SE (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','LightYuki']]):
     a = 25156
     b = 3153
     c = 2309
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#782 Yuki (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','LightYuki','SYuki','LightSYuki']]):
     a = 27676
     b = 3500
     c = 2547
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#783 Yuki SE (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','DarkYuki']]):
     a = 39869
     b = 2364
     c = 1772
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#784 Yuki (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Yuki','DarkYuki','SYuki','DarkSYuki']]):
     a = 44023
     b = 2603
     c = 1949
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#785 Yuki SE (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zari','FireZari']]):
     a = 22514
     b = 2574
     c = 1539
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#786 Zarid (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zari','WaterZari']]):
     a = 29092
     b = 1321
     c = 2540
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#787 Zarid (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zari','WoodZari']]):
     a = 28054
     b = 1879
     c = 1725
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#788 Zarid (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zari','LightZari']]):
     a = 35375
     b = 1554
     c = 1758
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#789 Zarid (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zari','DarkZari']]):
     a = 26041
     b = 2343
     c = 1566
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#790 Zarid (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zhu','FireZhu']]):
     a = 35201
     b = 3664
     c = 2390
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#791 Zhu Bajie  (Fire)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zhu','WaterZhu']]):
     a = 29971
     b = 2860
     c = 3848
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#792 Zhu Bajie  (Water)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zhu','WoodZhu']]):
     a = 29596
     b = 2928
     c = 3943
     d = 0.5
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#793 Zhu Bajie  (Wood)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zhu','LightZhu']]):
     a = 29521
     b = 2813
     c = 3957
     d = 0.5
     e = 0.2
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#794 Zhu Bajie  (Light)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)


 if any([message.content.startswith (item) for item in ['Zhu','DarkZhu']]):
     a = 45147
     b = 2548
     c = 2786
     d = 1
     e = 0.1
     f = (a/(1-(c/(c+1200))))
     g = (a*1.68/(1-(c/(c+1200))))
     h = (a*1.68/(1-(c*1.68/(c*1.68+1200))))
     i = (a*2.36/(1-(c*1.68/(c*1.68+1200))))
     j = (a*3.04/(1-(c/(c+1200))))
     k = ((5.5*b*3.04*(1+d*e))*0.5) 
     l = ((5.5*b*2.36*(1+(d+0.7)*e))*0.5) 
     m = ((5.5*b*2.36*(1+d*(e+0.54)))*0.5) 
     n = ((5.5*b*2.36*(1+d*e))*0.5) 
     o = ((5.5*b*1.68*(1+(d+0.7)*e))*0.5) 
     p = ((5.5*b*1.68*(1+d*(e+0.54)))*0.5) 
     q = ((5.5*b*1.68*(1+d*e))*0.5) 
     r = ((5.5*b*(1+d*e))*0.5) 
     embed=discord.Embed(title="", url='', color=message_color)
     embed.set_author(name='**#795 Zhu Bajie  (Dark)**')
     embed.set_thumbnail(url='')
     embed.add_field(name='★★★★★', value="gems = eHP : damage\n3xAtt = " + str(round(f)) + " : " + str(round(k)) + "\nAtt/Att/CD = " + str(round(f)) + " : " + str(round(l)) + "\nAtt/Att/CR = " + str(round(f)) + " : " + str(round(m)) + "\n\nAtt/Att/HP = " + str(round(g)) + " : " + str(round(n)) + "\nAtt/CD/HP = " + str(round(g)) + " : " + str(round(o)) + "\nAtt/CR/HP = " + str(round(g)) + " : " + str(round(p)) + "\n\nAtt/def/HP = " + str(round(h)) + " : " + str(round(q)) + "\nHP/HP/Def = " + str(round(i)) + " : " + str(round(r)) + "\n3xHP = " + str(round(j)) + " : " + str(round(r)), inline=False)
     await message.channel.send(embed=embed)

#####################################################################

@client.event
async def on_ready():
 print(client.user.name)
 print( "[ON]")
 print('- - - - - - - -')

client.run(TOKEN)
