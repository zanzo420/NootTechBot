import aiohttp,bs4,cleverbot,discord,urbandict,configparser,math,random,urllib.parse,os,lxml
from content import imdb, steam, websterdict, player, translator, news
from datetime import datetime
from decimal import Decimal
from urllib.request import Request, urlopen
from wordclouds import word
from lxml import etree
import urllib.request as ur
#import imgurpython


# Open up settings.ini with a text-editor and enter in your API/Imgur keys and preferred settings then save the file.
settings = configparser.ConfigParser()
settings.read('content/Settings.ini')





# -------------------------------
#       Global Variables
# -------------------------------






# Sets SuperAdmin IDs (only these IDs can use "invite", "prefix" & "leave" commands.).

admin_ids = [str(settings['BOTSETTINGS']['owner-id'])]

botadmin = settings['BOTSETTINGS']['BotAdmin'] # Sets the name of the botAdmin role, anyone with this role has admin rights

Bot_Token = settings['BOTSETTINGS']['token']

command_channel = settings['BOTSETTINGS']['channel'] # Sets the name of the botAdmin role, anyone with this role has admin rights

OPUS_LIBS = ['content/libopus-0.x86.dll','content/libopus-0.x64.dll','content/libopus-0.dll','content/libopus.so.0','content/libopus.0.dylib','/usr/local/Cellar/opus/1.1.2/lib/libopus.0.dylib'] # List holding locations of opus libraries

Imgur_ID = settings['IMGUR']['ID'] # Needed for Imgur API
Imgur_Secret = settings['IMGUR']['Secret'] # Also needed by Imgur API.

# Default game played by bot. current_game = None : removes 'Playing'
cg = settings['BOTSETTINGS']['currentgame']
if cg == "None":
    current_game = None
else:
    current_game = settings['BOTSETTINGS']['currentgame']

# Set current time to variable for 'uptime' command
startTime = datetime.utcnow()

NSFW = ["4r5e","5h1t","5hit","a55","anal","anus","ar5e","arrse","niggers","arse","ass-fucker","asses","assfucker","assfukka","asshole","assholes","asswhole","a_s_s","b!tch","b00bs","b17ch","b1tch","ballbag","balls","ballsack","bastard","beastial","beastiality","bellend","bestial","bestiality","bi+ch","biatch","bitch","bitcher","bitchers","bitches","bitchin","bitching","bloody","blow job","blowjob","blowjobs","boiolas","bollock","bollok","boner","boob","boobs","booobs","boooobs","booooobs","booooooobs","breasts","buceta","bugger","bum","bunny fucker","butt","butthole","buttmuch","buttplug","c0ck","c0cksucker","carpet muncher","cawk","chink","cipa","cl1t","clit","clitoris","clits","cnut","cock","cock-sucker","cockface","cockhead","cockmunch","cockmuncher","cocks","cocksuck ","cocksucked ","cocksucker","cocksucking","cocksucks ","cocksuka","cocksukka","cok","cokmuncher","coksucka","coon","cox","crap","cum","cummer","cumming","cums","cumshot","cunilingus","cunillingus","cunnilingus","cunt","cuntlick ","cuntlicker ","cuntlicking ","cunts","cyalis","cyberfuc","cyberfuck ","cyberfucked ","cyberfucker","cyberfuckers","cyberfucking ","d1ck","damn","dick","dickhead","dildo","dildos","dink","dinks","dirsa","dlck","dog-fucker","doggin","dogging","donkeyribber","doosh","duche","dyke","ejaculate","ejaculated","ejaculates ","ejaculating ","ejaculatings","ejaculation","ejakulate","f u c k","f u c k e r","f4nny","fag","fagging","faggitt","faggot","faggs","fagot","fagots","fags","fanny","fannyflaps","fannyfucker","fanyy","fatass","fcuk","fcuker","fcuking","feck","fecker","felching","fellate","fellatio","fingerfuck ","fingerfucked ","fingerfucker ","fingerfuckers","fingerfucking ","fingerfucks ","fistfuck","fistfucked ","fistfucker ","fistfuckers ","fistfucking ","fistfuckings ","fistfucks ","flange","fook","fooker","fuck","fucka","fucked","fucker","fuckers","fuckhead","fuckheads","fuckin","fucking","fuckings","fuckingshitmotherfucker","fuckme ","fucks","fuckwhit","fuckwit","fudge packer","fudgepacker","fuk","fuker","fukker","fukkin","fuks","fukwhit","fukwit","fux","fux0r","f_u_c_k","gangbang","gangbanged ","gangbangs ","gaylord","gaysex","goatse","God","god-dam","god-damned","goddamn","goddamned","hardcoresex ","hell","heshe","hoar","hoare","hoer","homo","hore","horniest","horny","hotsex","jack-off ","jackoff","jap","jerk-off ","jism","jiz ","jizm ","jizz","kawk","knob","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kum","kummer","kumming","kums","kunilingus","l3i+ch","l3itch","labia","lmfao","lust","lusting","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","masochist","master-bate","masterb8","masterbat*","masterbat3","masterbate","masterbation","masterbations","masturbate","mo-fo","mof0","mofo","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked ","mothafucker","mothafuckers","mothafuckin","mothafucking ","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","muff","mutha","muthafecker","muthafuckker","muther","mutherfucker","n1gga","n1gger","nazi","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers ","nob","nob jokey","nobhead","nobjocky","nobjokey","numbnuts","nutsack","orgasim ","orgasims ","orgasm","orgasms ","p0rn","pawn","pecker","penis","penisfucker","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","pigfucker","pimpis","piss","pissed","pisser","pissers","pisses ","pissflaps","pissin ","pissing","pissoff ","poop","porn","porno","pornography","pornos","prick","pricks ","pron","pube","pusse","pussi","pussies","pussy","pussys ","rectum","retard","rimjaw","rimming","s hit","s.o.b.","sadist","schlong","screwing","scroat","scrote","scrotum","semen","sh!+","sh!t","sh1t","shag","shagger","shaggin","shagging","shemale","shi+","shit","shitdick","shite","shited","shitey","shitfuck","shitfull","shithead","shiting","shitings","shits","shitted","shitter","shitters ","shitting","shittings","shitty ","skank","slut","sluts","smegma","smut","snatch","son-of-a-bitch","spac","spunk","s_h_i_t","t1tt1e5","t1tties","teets","teez","testical","testicle","tit","titfuck","tits","titt","tittie5","tittiefucker","titties","tittyfuck","tittywank","titwank","tosser","turd","tw4t","twat","twathead","twatty","twunt","twunter","v14gra","v1gra","vagina","viagra","vulva","w00se","wang","wank","wanker","wanky","whoar","whore","willies","willy","xrated","xxx","childporn","ch1ldp0rn","child-porn","rape","r4pe","r4p3","snuff","necrophillia","necro-porn","n3cr0","r4p3","gore","g0r3","g0re","gor3","lolita","l0l1tA","l0lita","l0lit4","jailbait","underage","necro","cp","incest","scat","fist me","fistme","cumshot","masturbation","hitler","h1tl3r","nazigermany","nazi germany","ear rape","35r r4p3","cumpilation","ahole","anus","ash0le","ash0les","asholes","AssMonkey","Assface","assh0le","assh0lez","assholz","asswipe","azzhole","bassterds","bastardz","basterds","basterdz","boffing","butthole","buttwipe","c0ck","c0cks","c0k","CarpetMuncher","cawk","cawks","Clit","cnts","cntz","cock","cockhead","cockhead","cocks","CockSucker","cocksucker","cum","cunt","cunts","cuntz","dild0","dild0s","dildo","dildos","dilld0","dilld0s","dominatricks","dominatrics","dominatrix","dyke","enema","fag1t","faget","fagg1t","faggit","faggot","fagit","fags","fagz","faig","faigs","fart","flipping","FudgePacker","fuk","Fukah","Fuken","fuker","Fukin","Fukk","Fukkah","Fukken","Fukker","Fukkin","g00k","gaybor","gayboy","gaygirl","gays","gayz","Goddamned","h00r","h0ar","h0re","hells","hoar","hoor","hoore","jackoff","jap","japs","jerkoff","jisim","jiss","jizm","jizz","knob","knobs","knobz","kunt","kunts","kuntz","Lesbian","Lezzian","Lipshits","Lipshitz","masochist","masokist","massterbait","masstrbait","masstrbate","masterbaiter","masterbate","masterbates","mutha","fuker","motha","fucker","fuker","fukka","fukkah","fucka","fuchah","fukker","fukah","MothaFucker","MothaFuker","MothaFukkah","MothaFukker","MotherFucker","MotherFukah","MotherFuker","MotherFukkah","MotherFukker","motherfucker","MuthaFucker","MuthaFukah","MuthaFuker","MuthaFukkah","MuthaFukker","mutha","n1gr","nastt","nasty","nigur","niiger","niigr","orafis","oriface","orifice","orifiss","packi","packie","packy","paki","pakie","paky","pecker","peeenus","peeenusss","peenus","peinus","pen1s","penas","penis","penisbreath","penus","penuus","Phuc","Phuck","Phuk","Phuker","Phukker","polac","polack","polak","Poonani","pr1c","pr1ck","pr1k","pusse","pussee","puuke","puuker","queer","queers","queerz","qweers","qweerz","qweir","recktum","rectum","retard","sadist","scank","schlong","screwing","semen","shitz","Shyt","Shyte","Shytty","Shyt","skanck","skank","skankee","skankey","skanks","Skanky","sonofabitch","tit","turd","va1jina","vag1na","vagiina","vagina","vaj1na","vajina","vullva","vulva","w0p","wh00r","wh0re","whore","xrated","xxx","bch","blowjob","clit","arschloch","boiolas","buceta","c0ck","cawk","chink","cipa","clits","cock","cum","cunt","dildo","dirsa","ejakulate","fatass","fcuk","fuk","fux0r","hoer","hore","jism","kawk","l3itch","l3i+ch","lesbian","masturbate","masterbat","masterbat3","motherfucker","s.o.b.","mofo","nazi","nigger","scrotum","shemale","shi+","testical","testicle","titt","w00se","jackoff","wank","whoar","whore","damn","dyke","amcik","andskota","arse","assrammer","ayir","bi7ch","bitch","bollock","breasts","buttpirate","cabron","cazzo","chraa","chuj","Cock","cunt","d4mn","daygo","dego","dick","dike","dupa","dziwka","ejackulate","Ekrem","Ekto","enculer","faen","fag","fanculo","fanny","feces","feg","Felcher","ficken","fitt","Flikker","foreskin","Fotze","Fu","fuk","futkretzn","gay","gook","guiena","h0r","h4x0r","hell","helvete","hoer","honkey","Huevon","hui","injun","jizz","kanker","kike","klootzak","kraut","knulle","kuk","kuksuger","Kurac","kurwa","kusi","kyrpa","lesbo","mamhoon","masturbat","merd","mibun","monkleigh","mouliewop","muie","mulkku","muschi","nazis","nepesaurio","nigger","orospu","paska","perse","picka","pierdol","pillu","pimmel","piss","pizda","poontsee","poop","porn","p0rn","pr0n","preteen","pula","pule","puta","puto","qahbeh","queef","rautenberg","schaffer","scheiss","schlampe","schmuck","screw","sharmuta","sharmute","shipal","shiz","skrib", "big black","titties"]

spamlist = ["vine","kazoo","hours","hourlong","hour","montage","pewds","pewdiepie","keemsta","keeem","meme","compilation","KEEMSTAR","keemstar","memestar","shrek","cod","meme-star","keem","k33mst4r","k33mstar","nigger","niggers","leafy","pewdiepie","minecraft","pingu","ecks dee","cancer","meems","meem","faggot","f4gg0t","f4550t","nazi","n4zi","anal","4n4l","ecks de","fist me","fistme","cumshot","masturbation","hitler","h1tl3r","nazigermany","nazi germany","ear rape","35r r4p3","cumpilation","ahole","anus","ash0le","ash0les","asholes","AssMonkey","Assface","assh0le","assh0lez","assholz","asswipe","azzhole","bassterds","bastardz","basterds","basterdz","boffing","butthole","buttwipe","c0ck","c0cks","c0k","CarpetMuncher","cawk","cawks","Clit","cnts","cntz","cock","cockhead","cockhead","cocks","CockSucker","cocksucker","cum","cunt","cunts","cuntz","dild0","dild0s","dildo","dildos","dilld0","dilld0s","dominatricks","dominatrics","dominatrix","dyke","enema","fag1t","faget","fagg1t","faggit","faggot","fagit","fags","fagz","faig","faigs","fart","flipping","FudgePacker","fuk","Fukah","Fuken","fuker","Fukin","Fukk","Fukkah","Fukken","Fukker","Fukkin","g00k","gaybor","gayboy","gaygirl","gays","gayz","Goddamned","h00r","h0ar","h0re","hells","hoar","hoor","hoore","jackoff","jap","japs","jerkoff","jisim","jiss","jizm","jizz","knob","knobs","knobz","kunt","kunts","kuntz","Lesbian","Lezzian","Lipshits","Lipshitz","masochist","masokist","massterbait","masstrbait","masstrbate","masterbaiter","masterbate","masterbates","mutha","fuker","motha","fucker","fuker","fukka","fukkah","fucka","fuchah","fukker","fukah","MothaFucker","MothaFuker","MothaFukkah","MothaFukker","MotherFucker","MotherFukah","MotherFuker","MotherFukkah","MotherFukker","motherfucker","MuthaFucker","MuthaFukah","MuthaFuker","MuthaFukkah","MuthaFukker","mutha","n1gr","nastt","nasty","nigur","niiger","niigr","orafis","oriface","orifice","orifiss","packi","packie","packy","paki","pakie","paky","pecker","peeenus","peeenusss","peenus","peinus","pen1s","penas","penis","penisbreath","penus","penuus","Phuc","Phuck","Phuk","Phuker","Phukker","polac","polack","polak","Poonani","pr1c","pr1ck","pr1k","pusse","pussee","puuke","puuker","queer","queers","queerz","qweers","qweerz","qweir","recktum","rectum","retard","sadist","scank","schlong","screwing","semen","shitz","Shyt","Shyte","Shytty","Shyt","skanck","skank","skankee","skankey","skanks","Skanky","sonofabitch","tit","turd","va1jina","vag1na","vagiina","vagina","vaj1na","vajina","vullva","vulva","w0p","wh00r","wh0re","whore","xrated","xxx","bch","blowjob","clit","arschloch","boiolas","buceta","c0ck","cawk","chink","cipa","clits","cock","cum","cunt","dildo","dirsa","ejakulate","fatass","fcuk","fuk","fux0r","hoer","hore","jism","kawk","l3itch","l3i+ch","lesbian","masturbate","masterbat","masterbat3","motherfucker","s.o.b.","mofo","nazi","nigger","scrotum","shemale","shi+","testical","testicle","titt","w00se","jackoff","wank","whoar","whore","damn","dyke","amcik","andskota","arse","assrammer","ayir","bi7ch","bitch","bollock","breasts","buttpirate","cabron","cazzo","chraa","chuj","Cock","cunt","d4mn","daygo","dego","dick","dike","dupa","dziwka","ejackulate","Ekrem","Ekto","enculer","faen","fag","fanculo","fanny","feces","feg","Felcher","ficken","fitt","Flikker","foreskin","Fotze","Fu","fuk","futkretzn","gay","gook","guiena","h0r","h4x0r","hell","helvete","hoer","honkey","Huevon","hui","injun","jizz","kanker","kike","klootzak","kraut","knulle","kuk","kuksuger","Kurac","kurwa","kusi","kyrpa","lesbo","mamhoon","masturbat","merd","mibun","monkleigh","mouliewop","muie","mulkku","muschi","nazis","nepesaurio","nigger","orospu","paska","perse","picka","pierdol","pillu","pimmel","piss","pizda","poontsee","poop","porn","p0rn","pr0n","preteen","pula","pule","puta","puto","qahbeh","queef","rautenberg","schaffer","scheiss","schlampe","schmuck","screw","sharmuta","sharmute","shipal","shiz","skrib"]




# -------------------------------
#       Global Functions
# -------------------------------


# Function for loading Opus Voice libraries
def load_opus_lib(opus_libs=OPUS_LIBS):  # Load Opus for voice
    if discord.opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            # opus path for OSX
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass


# -------------------------------
#       denBot class
# -------------------------------


class denBot(discord.Client):
    # -------------------------------
    #       Bot Initialization
    # -------------------------------
    def __init__(self):
        super().__init__()
        self.servers_dict = {}
        self.token = Bot_Token
        self.pepe_list = []
        self.slav_list = []
        self.set_dict = {}
        #self.get_imgur()
        self.command_prefix = settings['PREFIX']['CommandPrefix']
        self.music_players = {}
        self.currentgame = current_game
        self.days = 0


    #def get_imgur(self):
        #client = imgurpython.ImgurClient(Imgur_ID, Imgur_Secret)
        #self.pepe_list = client.get_album_images('PI6Co')
        #self.slav_list = client.get_album_images('XSUvB')

        # Read help file and format for discord


    def print_commands(self,file):
        string = ''
        fc = open(file, 'r')
        help_file = fc.read()
        fc.close()
        help = help_file.split('\n')
        for i in range(0, (len(help) - 1)):
            temp = help[i].format(self.command_prefix)
            string = string + temp + '\n'
        return '```' + string + '```'



    # Replace discord.py's built-in run command to include bot token
    def run(self):
        return super().run(self.token)

    # When bot is ready and logged in
    async def on_ready(self):
        print('------------')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        self.bot_id = '<@' + self.user.id + '>'
        self.nick_id = '<@!' + self.user.id + '>'

        for server in self.servers:
            mp = player.Player(self, server)
            self.music_players[server.id] = mp

        # On Launch set current game bot is playing
        await self.change_status(discord.Game(name=self.currentgame))


    #def pepe_of_the_day(self):
    #    randominteger = random.randint(0, len(self.pepe_list))
    #    return self.pepe_list[randominteger].link

    #def slav_of_the_day(self):
    #    random_integer = random.randint(0, len(self.slav_list))
    #    return self.slav_list[random_integer].link

    async def on_message(self, message):
        # -------------------------------
        #       Wordcloud Writing Code
        # -------------------------------

        mp = None
        days = 0
        private = False
        admin = False
        Mod = False
        subMod = False

        # Checks if the message being sent is a PM. If not, music player can be used.
        if message.channel.is_private:
            try:
                private = True
                cb2 = cleverbot.Cleverbot()
                answer = cb2.ask(message.content)
                await self.send_message(message.author, str(answer))

            except:
                print("Cleverbot message sent")
        if message.author.bot == False and private == False:

            # Checks if the message author is a BotAdmin.
            for role in message.author.roles:
                if "denBot" in role.name or "Loser" in role.name:
                    admin = True

                elif "Fag" in role.name:
                    Mod = True

                elif "Retard" in role.name:
                    subMod = True
            try:
                mp = self.music_players[message.server.id]
            except:
                print('Failed to time-out from '+message.server.name+" ["+str(message.server.id)+"]")
                print("Bot may get error 403 because of this.")

            # Checks if message is from a Bot.
            if message.content.startswith(self.command_prefix):
                # Removes prefix from user message
                message.content.replace(self.command_prefix,'')
            path = 'wordclouds/'+str(message.server.id) + '.txt'
            # Writes entire message to server text file and then closes the file.
            file = open(path, 'a')
            file.write(' '+message.content)
            file.close()

        # -------------------------------
        #       SuperAdmin Bot Commands
        # -------------------------------

        if message.content.startswith(self.command_prefix):

            cmd = message.content[1:]

            if command_channel in message.channel.name.lower():


                if cmd.lower().startswith('invite'):
                    if message.author.id in admin_ids and message.author.id == str(settings['BOTSETTINGS']['owner-id']):
                        invite = 'https://discordapp.com/oauth2/authorize?&client_id='+str(settings['BOTSETTINGS']['bot-id'])+'&scope=bot&permissions=0'
                        await self.send_message(message.author, invite)
                    else:
                        await self.send_message(message.channel, 'Sorry, only a SuperAdmin can do this.')


                elif cmd.lower().startswith('leave'):
                    if message.author.id in admin_ids and message.author.id == str(settings['BOTSETTINGS']['owner-id']):
                        await self.leave_server(message.server)
                    else:
                        await self.send_message(message.channel, 'Sorry, only SuperAdmins can do this.')


                elif cmd.startswith('game '):
                    if message.author.id in admin_ids or admin == True:
                        tempgame = cmd[5:]
                        print(tempgame)
                        if len(tempgame) > 86:
                            await self.send_message(message.channel, 'Game name is too long. Try something shorter.')
                        else:
                            if tempgame.lower() == "none":
                                settings['BOTSETTINGS']['currentgame'] = "None"
                            else:
                                settings['BOTSETTINGS']['currentgame'] = tempgame
                            with open("content/Settings.ini", "w") as settingsfile:
                                settings.write(settingsfile)
                            settings2 = configparser.ConfigParser()
                            settings2.read('content/Settings.ini')
                            if settings2['BOTSETTINGS']['currentgame'] == "None":
                                await self.change_status(discord.Game(name=None))
                                await self.send_message(message.channel,self.user.name + "'s current game has been `removed`.")
                            else:
                                await self.change_status(discord.Game(name=settings['BOTSETTINGS']['currentgame']))
                                await self.send_message(message.channel,
                                                        self.user.name + "'s current game has been changed to: `" +
                                                        settings['BOTSETTINGS']['currentgame'] + "`")
                    else:
                        await self.send_message(message.channel, 'Sorry, only a BotAdmin can do this.')




                if cmd.lower().startswith('prefix '):
                    if message.author.id in admin_ids or admin:
                        cmd = cmd[7:]
                        if len(cmd) != 1:
                            await self.send_message(message.channel,
                                                    "Sorry, the command prefix can only be 1 character long (e.g. !, *, ^)")
                        elif cmd.isalpha() or cmd.isdigit() or cmd == ' ':
                            await self.send_message(message.channel,
                                                    "Sorry, You can't use letters/numbers as a prefix. Try a special character like '!, * or ^')")
                        else:
                            settings['PREFIX']['CommandPrefix'] = cmd
                            with open("content/Settings.ini", "w") as settingsfile:
                                settings.write(settingsfile)
                            await self.send_message(message.channel,
                                                    self.user.name + "'s command prefix has been changed to: `" + cmd + "`")
                            settings2 = configparser.ConfigParser()
                            settings2.read('content/Settings.ini')
                            self.command_prefix = settings2['PREFIX']['CommandPrefix']

                            alert = (self.user.name + "'s command prefix has been changed to: `" + cmd + "`"+ ' by '+message.author.name)
                            for userid in admin_ids:
                                user = discord.utils.get(self.get_all_members(), id=userid)
                                await self.send_message(user, alert)

                            for server in self.servers:
                                await self.send_message(server, alert+'type in `'+cmd+'help` to get the full list of bot commands!')



                    else:
                        await self.send_message(message.channel, 'Sorry, only botAdmins can do this.')


                elif cmd.lower().startswith('avatar '):
                    if message.author.id in admin_ids or admin == True:
                        url = cmd[7:]
                        avatar_data = None
                        aioclient = aiohttp.ClientSession()
                        try:
                            async with aioclient.get(url) as resp:
                                avatar_data = await resp.read()
                                with open("temp.png", "wb") as f:
                                    f.write(avatar_data)
                                    f.close()
                            aioclient.close()
                            if os.path.isfile("temp.png"):
                                fp = open("temp.png", 'rb')
                                newavatar = fp.read()
                                fp.close()
                                await self.edit_profile(avatar=newavatar)
                                os.remove("temp.png")
                                await self.send_message(message.channel, self.user.name + "'s avatar has been updated.")
                        except:
                            await self.send_message(message.channel,
                                                    "Failed to download avatar. Please check the link and try again.")
                    else:
                        await self.send_message(message.channel, 'Sorry, only botAdmins can do this.')

                elif cmd.lower().startswith('name '):
                    if message.author.id in admin_ids or admin == True:
                        name = cmd[4:]
                        if name == "none" or name == "reset":
                            await self.send_message(message.channel,'`' + message.server.me.nick + ' has been reset to ' + self.user.name + '`')
                            await self.change_nickname(message.server.me, self.user.name)
                        else:
                            await self.send_message(message.channel, '`'+self.user.name+' has been changed to '+name+'`')
                            await self.change_nickname(message.server.me, name)
                    else:
                        await self.send_message(message.channel, 'Sorry, only botAdmins can do this.')








                # -------------------------------
                #    Music Player Bot Commands
                # -------------------------------

                elif cmd.lower().startswith('connect'):
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        try:
                            await mp.get_voice_client(message.author.voice_channel, True)
                            await self.send_message(message.channel, 'Connected to voice channel.')
                        except discord.errors.InvalidArgument:
                            await self.send_message(message.channel, 'You need to be in a channel for me to connect to it.')
                    else:
                        await self.send_message(message.channel, 'Sorry, only a BotAdmin can do this.')

                elif cmd.lower().startswith('disconnect'):
                    if message.author.id in admin_ids or admin == True or Mod == True:
                        await mp.disconnect_voice_client()
                        await self.change_status(discord.Game(name=self.currentgame))
                        await self.send_message(message.channel, 'Disconnected from voice channel.')
                    else:
                        await self.send_message(message.channel, 'Sorry, only a BotAdmin can do this.')




                elif cmd.lower().startswith('add '):
                    Spam = False

                    if "youtube" in cmd.lower():
                        youtube = etree.HTML(ur.urlopen(cmd[4:]).read())
                        phrase = youtube.xpath("//span[@id='eow-title']/@title")[0].lower().split(' ')
                        print(phrase)
                    elif "soundcloud" in cmd.lower():
                        phrasex = cmd.replace("https://soundcloud.com/","")
                        phrasex = phrasex.replace("-"," ")
                        phrasex = phrasex.split("/")
                        phrase = phrasex[1]+" - "+phrasex[0]
                    else:
                        phrase = cmd.split(' ')

                    cmd = cmd.replace(' ','+')
                    rejections = []
                    for item in phrase:
                        if item in spamlist:
                            Spam = True
                            rejections.append(item)

                    rejects = ""
                    for item in rejections:
                        rejects += " `" + item + "` "

                    if Spam == True:
                        await self.send_message(message.channel,
                                                'Lol no. The words' + rejects + ' arent allowed, you tit.')
                    else:
                        if message.author.voice_channel == mp.voice_client.channel:
                            if not private:
                                link = cmd[4:]
                                if 'http://' in link or 'https://' in link:
                                    args = link
                                else:
                                    query = urllib.parse.quote(link)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    soup = bs4.BeautifulSoup(urlopen(url).read(), "lxml")
                                    L = []

                                    for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                                        if len(video['href']) < 25:
                                            L.append('https://www.youtube.com' + video['href'])

                                    args = L[0]



                                print(args)
                                voice = await mp.get_voice_client()
                                if 'youtube' in args:
                                    player = await mp.get_player(voice.channel)
                                    if (len(mp.playlist) == 0 and player is None) or \
                                            (len(mp.playlist) == 0 and player.is_done()):
                                        await mp.add_playlist(args, message)
                                        await mp.audio_player(new=True)
                                    else:
                                        await mp.add_playlist(args, message)
                                elif 'soundcloud' in args:
                                    player = await mp.get_player(voice.channel)
                                    if (len(mp.playlist) == 0 and player is None) or (len(mp.playlist) == 0 and player.is_done()):
                                        await mp.add_playlist(args, message, type='s')
                                        await mp.audio_player(new=True)

                                    else:
                                        await mp.add_playlist(args, message, type='s')
                                else:
                                    msg = '{0.author.mention} : Invalid Link.'
                                    await self.send_message(message.channel, msg.format(message))
                            else:
                                msg = "{0.author.mention} : Sorry, you can't do that in a PM :("
                                await self.send_message(message.channel, msg.format(message))
                        else:
                            await self.send_message(message.channel, "You need to be in the same channel as the bot to add a song!")









                elif cmd.lower().startswith('skip'):
                    if message.author.voice_channel == mp.voice_client.channel:
                        if message.author.id in admin_ids or admin == True:
                            await mp.do_skip(message, True)
                        else:
                            await mp.do_skip(message)
                    else:
                        await self.send_message(message.channel, "You need to be in the same channel as the bot to skip a song!")


                elif cmd.lower().startswith('remove'):

                    song_int = cmd.replace("remove ","")

                    if message.author.voice_channel == mp.voice_client.channel:
                        if message.author.id in admin_ids or admin == True:
                            await mp.remove_song(message,song_int,True)
                        else:
                            await mp.remove_song(message,song_int)
                    else:
                        await self.send_message(message.channel,
                                                "You need to be in the same channel as the bot to remove a song!")




                elif cmd.lower().startswith('block '):
                    cmd = cmd.lower().replace('block ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        if "<@" in cmd and self.user.id not in cmd and (len(cmd)>19 and len(cmd)<23):
                            path = 'content/blacklists/' + str(message.server.id) + '_blacklist.txt'
                            file = open(path, 'a')
                            occur = False
                            with open(path) as f:
                                for line in f:
                                    if cmd in line:
                                        occur = True
                            if occur == True:
                                await self.send_message(message.channel,"The user " + cmd + " is already blacklisted.")
                            else:
                                member_id = cmd.replace("<@", "").replace(">", "")
                                member = discord.utils.get(message.server.members, id=member_id)
                                if member_id in admin_ids:
                                    await self.send_message(message.channel,"You cannot blacklist a server owner/bot admin.")
                                else:
                                    file.write(cmd+" - "+member.name+'\n')
                                    file.close()
                                    server = member.server
                                    bot_role = discord.Role

                                    for role in server.roles:
                                        if 'bot-ban' in role.name:
                                            bot_role = role
                                            break

                                    await client.add_roles(member, bot_role)

                                    await self.send_message(message.channel, "The user "+cmd+" has been `added` to the "+message.server.name+" blacklist.")
                        else:
                            await self.send_message(message.channel,
                                                    "Please use the @ prefix when adding someone to the blacklist, e.g. @denBot")

                    else:
                        await self.send_message(message.channel, "Only admins can add users to the bot blacklist.")





                elif cmd.lower().startswith('blacklist'):
                    cmd = cmd.lower().replace('block ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        try:
                            blacklist = open('content/blacklists/'+str(message.server.id)+'_blacklist.txt')
                            strng = ""
                            for line in blacklist:
                                strng += line
                            await self.send_message(message.channel, "Sent "+message.server.name+" Blacklist via DM.")
                            await self.send_message(message.author, "```python\n "+message.server.name+" Blacklist:\n"+strng+"```")
                        except:
                            await self.send_message(message.channel, "There was an error loading the blacklist.")

                    else:
                        await self.send_message(message.channel, "Only admins can view the servers blacklist.")






                elif cmd.lower().startswith('unblock '):
                    cmd = cmd.lower().replace('unblock ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        if "<@" in cmd and self.user.id not in cmd and (len(cmd)>19 and len(cmd)<23):
                            path = 'content/blacklists/' + str(message.server.id) + '_blacklist.txt'
                            file = open(path, 'a')
                            occur = False
                            output = []
                            with open(path) as f:
                                for line in f:
                                    if cmd in line:
                                        occur = True
                                    else:
                                        output.append(line)
                            f.close()



                            writer = open(path, 'w')
                            writer.writelines(output)
                            writer.close()

                            if occur == True:

                                member_id = cmd.replace("<@", "").replace(">", "")
                                member = discord.utils.get(message.server.members, id=member_id)
                                if member_id in admin_ids:
                                    await self.send_message(message.channel,
                                                            "You cannot blacklist a server owner/bot admin.")
                                else:
                                    server = member.server
                                    bot_role = discord.Role

                                    for role in server.roles:
                                        if 'bot-ban' in role.name:
                                            bot_role = role
                                            break

                                    await client.remove_roles(member, bot_role)

                                    await self.send_message(message.channel,
                                                            "The user " + cmd + " has been `removed` to the " + message.server.name + " blacklist.")
                            else:
                                await self.send_message(message.channel,
                                                        "The requested user is not in the blacklist.")
                        else:
                            await self.send_message(message.channel,
                                                    "Please use the @ prefix when adding someone to the blacklist, e.g. @denBot")

                    else:
                        await self.send_message(message.channel, "Only admins can remove users to the bot blacklist.")





                elif cmd.lower().startswith('volume '):

                    cmd = cmd.lower().replace('volume ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        await mp.change_volume(cmd, message.channel)
                    else:
                        await self.send_message(message.channel, "Please ask a moderator or admin to change the volume for you! :wink:")


                elif cmd.lower().startswith('currentsong') or cmd.lower().startswith('playing') or cmd.lower().startswith('song'):
                    await mp.current_song(message)
















                # -------------------------------
                #      Normal Bot Commands
                # -------------------------------

                elif cmd.lower().startswith('wordcloud'):
                    temp_msg = await self.send_message(message.channel, 'Generating wordcloud for ' + message.server.name)
                    path = str(message.server.id) + '.txt'
                    word.get_wordcloud(path)
                    file.close()
                    await self.delete_message(temp_msg)
                    try:
                        await self.send_file(message.channel, 'result.png')
                    except:
                        self.send_message(message.channel, "I can't upload images to " + message.server.name + ":frowning:")
                    os.remove('result.png')





                elif cmd.lower().startswith('uptime'):
                    uptime = (datetime.utcnow() - startTime)
                    uptime = str(uptime).split(':')
                    hours = uptime[0]
                    minutes = uptime[1]
                    full_seconds = uptime[2].split('.')
                    seconds = full_seconds[0]
                    if minutes[0] == '0':
                        minutes = minutes[:1]
                    if seconds[0] == '0':
                        seconds = seconds[:1]
                    if int(hours) > 24:
                        days += 1
                        int_hours = int(hours) - 24
                        hours = str(int_hours)
                    up = ('I have been online for: ' + str(
                        days) + " Days, " + hours + " Hours, " + minutes + " Minutes and " + seconds + " Seconds. :thinking:")
                    await self.send_message(message.channel, up.format(message))


                elif cmd.lower().startswith('playlist'):
                    if not private:
                        await mp.get_queue(message)
                    else:
                        msg = '{0.author.mention} : This command can not be done in a PM'
                        await self.send_message(self, message.channel, msg.format(message))


                elif cmd.lower().startswith('bosh'):
                    victim = cmd.replace("bosh ","")
                    if "<@" in victim:
                        await self.send_message(message.channel, victim+' just got boshd')

                elif cmd.lower().startswith('bosh'):
                    victim = cmd.replace("bosh ", "")
                    if "<@" in victim:
                        await self.send_message(message.channel, victim + ' just got boshd')

                elif cmd.lower().startswith('ping'):
                    await self.send_message(message.channel, 'Pong!')

                elif cmd.lower().startswith('ding'):
                    await self.send_message(message.channel, 'Dong!')

                elif cmd.lower().startswith('bing'):
                    await self.send_message(message.channel, 'Bong!')

                elif cmd.lower().startswith('lenny'):
                    await self.send_message(message.channel, '( ͡° ͜ʖ ͡°)')


                elif cmd.lower().startswith('imdb'):
                    cmd = cmd.lower()
                    film = str(await imdb.imdb(cmd))
                    title = cmd.replace('imdb ','')
                    await self.send_message(message.channel, 'Sent IMDB Results for "' + title + '" :film_frames: ')
                    await self.send_message(message.author, film)


                elif cmd.lower().startswith('bd'):
                    await self.send_message(message.channel, 'Sent information about BetterDiscord :cd:')
                    BetterDiscord = "BetterDiscord enhances Discord with several features.\n\nIt improves several aspects of the vanilla discord client"\
                    " including custom Themes, Plugins, Display Modes and Twitch.tv, FrankerFaceZ and BetterTTV emotes.\n"\
                    "\nYou can download and install BetterDiscord at https://betterdiscord.net/home/"\
                    "\n\nTutorial on installing themes:"\
                    "\n 1 - Download and install BetterDiscord. Restart your discord client after installation."\
                    "\n 2 - Download your desired theme (in theme.css format) that you want to use with Discord (links below)."\
                    "\n 3 - Open up discord, click on the Settings button and navigate to BetterDiscord > Themes"\
                    "\n 4 - Click on the 'Open Theme Folder' button and a file new explorer window will pop up."\
                    "\n 5 - Drag your desired themes into the explorer window that has just appeared."\
                    "\n 6 - Restard discord and navigate back to Settings > BetterDiscord > Themes."\
                    "\n 7 - Select the time you want to use and it will enable itself. Voila!"\
                    "\n\nYou can find themes in the #theme-repo section of the BetterDiscord's Discord Server"\
                    "\nYou can a selection of themes made by den at: https://github.com/denBot/Simplistic-CSS"
                    await self.send_message(message.author, BetterDiscord)



                elif cmd.lower().startswith('steam '):
                    cmd = cmd.lower()
                    temp_message = await self.send_message(message.channel,
                                                           'Getting join link for "' + cmd.replace('steam ','') + '", Please wait...')
                    await steam.finder(self, cmd, message)
                    await steam.join(self, cmd, message)
                    await self.delete_message(temp_message)

                elif cmd.lower().startswith('steam?'):
                    helpmessage = (
                    '1. Visit your steam profile and grab the URL \nExample: :arrow_right: http://steamcommunity.com/id/denBot/ :arrow_left:  \n2. Copy the custom URL **or** Steam number following /id/ or /profiles/ \n3. In a discord channel, type '+self.command_prefix+'steam followed by the end of the URL. :grinning:\nLike this: **!steam denBot** (remove any /)')
                    await self.send_message(message.channel, helpmessage)

                elif cmd.lower().startswith('define '):
                    cmd = cmd[7:]
                    await self.send_message(message.channel, 'Sent Merriam-Webster Results for "' + cmd + '" :writing_hand:')
                    await self.send_message(message.author, websterdict.get_xml_definition(cmd))

                elif cmd.lower().startswith('urban '):
                    cmd = cmd[6:]
                    try:
                        urban = urbandict.define(cmd)
                        await self.send_message(message.channel, 'Sent Urban Dictionary Results for "' + cmd + '" :wink:')
                        string = ''
                        for item in urban:
                            definition = item['def'].replace('\n','')
                            if len(definition) < 200:
                                string = string +'- '+ definition + '\n'

                        await self.send_message(message.author, 'Results for "' + cmd + '"')
                        try:
                            await self.send_message(message.author, string + '\n')
                        except:
                            await self.send_message(message.author, 'Sorry, too much text to send as one message. :confused:')
                    except:
                        await self.send_message(message.author, "Couldn't find any Urban Dictionary results for "+cmd)


                elif cmd.lower().startswith('bbc'):
                    await self.send_message(message.channel, news.bbc())

                elif cmd.lower().startswith('cnn'):
                    await self.send_message(message.channel, news.cnn())

                elif cmd.lower().startswith('google '):
                    cmd = cmd[6:]
                    NotSafe = False
                    phrase = cmd.split(' ')
                    cmd = cmd.replace(' ','+')
                    rejections = []
                    for item in phrase:
                        if item in NSFW:
                            NotSafe = True
                            rejections.append(item)

                    rejects = ""
                    for item in rejections:
                        rejects += " `" + item + "` "

                    if NotSafe == True:
                        await self.send_message(message.channel,
                                                'Sorry, the words ' + rejects + ' are considered NSFW. Naughty! :smirk:')
                    else:
                        req = Request("https://www.google.com/search?q="+cmd)
                        req.add_header('User-agent',
                                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
                        response = urlopen(req)
                        soup = bs4.BeautifulSoup(response.read(), "html.parser")
                        title = []
                        desc = []
                        for i in soup.find_all("h3", class_="r"):
                            title.append(i.text)

                        for i in soup.find_all("div", class_="s"):
                            desc.append(i.text)

                        await self.send_message(message.channel, (message.author.mention + ' `'+title[0]+'`\n'+desc[0]))

                elif cmd.lower().startswith('translate?'):
                    cmd = self.print_commands('content/txt/translate.txt')
                    await self.send_message(message.channel, "Sent Translate commands via PM.")
                    await self.send_message(message.author, cmd)

                elif cmd.lower().startswith('translate '):
                    await self.send_message(message.channel, translator.translate(cmd.lower()))

                elif cmd.lower().startswith('youtube '):
                    youtube_link = cmd[8:]
                    NotSafe = False
                    phrase = cmd.split(' ')


                    query = urllib.parse.quote(youtube_link)
                    url = "https://www.youtube.com/results?search_query=" + query
                    soup = bs4.BeautifulSoup(urlopen(url).read(), "lxml")
                    L = []

                    rejections = []
                    for item in phrase:
                        if item in NSFW:
                            NotSafe = True
                            rejections.append(item)

                    rejects = ""
                    for item in rejections:
                        rejects += " `"+item + "` "

                    if NotSafe == True:
                        await self.send_message(message.channel, 'Sorry, the words '+ rejects +' are considered NSFW. Naughty! :smirk:')
                    else:
                        for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                            if len(video['href']) < 25:
                                L.append('https://www.youtube.com' + video['href'])
                        await self.send_message(message.channel, message.author.mention + ' `Result for "'+youtube_link+'"` \n'+L[0])



                elif cmd.lower().startswith('help'):
                    help = self.print_commands('content/txt/help.txt')
                    await self.send_message(message.channel, "Sent help commands via PM.")
                    await self.send_message(message.author, help)

                elif cmd.lower().startswith('music'):
                    help = self.print_commands('content/txt/music.txt')
                    await self.send_message(message.channel, "Sent music commands via PM.")
                    await self.send_message(message.author, help)

                elif cmd.lower().startswith('admin'):
                    if message.author.id in admin_ids and (message.author.id == str(settings['BOTSETTINGS']['owner-id']) or admin or Mod or subMod):
                        admin = self.print_commands('content/txt/admin.txt')
                        superadmin = self.print_commands('content/txt/owner.txt')
                        await self.send_message(message.channel, "Sent Admin commands via PM.")
                        await self.send_message(message.author, admin + superadmin)
                    else:
                        await self.send_message(message.channel, 'Sorry, only an Admin/Mod can do this.')












                # --------------------------------
                #    Meme commands (in #memes only)
                # --------------------------------




                #elif "meme" in message.channel.name.lower()  and cmd.lower().startswith('pepe') or "memes" in message.channel.name.lower() and cmd.lower().startswith('pepe'):
                #    await self.send_message(message.channel, self.pepe_of_the_day())


                #elif "meme" in message.channel.name.lower() and cmd.lower().startswith('slav') or "memes" in message.channel.name.lower() and cmd.lower().startswith('slav'):
                #    await self.send_message(message.channel, self.slav_of_the_day())




                elif cmd.lower().startswith('froggo') and message.author.id == '140193899602771968':
                    await self.send_message(message.channel, (
                    ':regional_indicator_r: :regional_indicator_e:  :regional_indicator_e:  :regional_indicator_e:  :regional_indicator_e:  :regional_indicator_e:  :regional_indicator_e:  :regional_indicator_e: '))








                elif cmd.lower().startswith('coinflip'):
                    outcome = random.randint(0, 1)
                    if outcome == 0:
                        outcome = "Heads"

                        await self.send_message(message.channel, 'http://cointoss.co/heads1.png')
                        await self.send_message(message.channel, outcome)
                    else:
                        outcome = "Tails"
                        await self.send_message(message.channel, 'http://cointoss.co/tails1.png')
                        await self.send_message(message.channel, outcome)

                # Commands/Wordfilters that don't require the command prefix






                elif message.content.lower().startswith('?prefix') or message.content.lower().startswith('prefix?'):
                    pfx = self.command_prefix
                    await self.send_message(message.channel, 'The current prefix is `'+pfx+'`. Use `'+pfx+'help` to get a list of all commands.')


            # Commands that dont require a special channel name:

            elif cmd.lower().startswith('stream') and (admin or Mod or subMod):
                try:
                    await self.send_message(message.channel, "Come visit MamaMax's Live Stream!")
                    await self.send_message(message.channel, "https://www.youtube.com/c/MamaMaxxy/live")
                except:
                    print('Couldnt post stream link in user channel.')






# Load Opus Libraries
load_opus_lib()
# Create Bot
client = denBot()
# Run Bot
client.run()