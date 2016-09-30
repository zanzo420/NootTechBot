import aiohttp, bs4, cleverbot, discord, urbandict, configparser, random, urllib.parse, os, sys, asyncio, imgurpython, git, wolframalpha, time
from content.pyfiles import imdb, steam, websterdict, player, translator, news, word
from datetime import datetime as dt
from urllib.request import Request, urlopen
from lxml import etree


# Open up settings.ini with a text-editor and enter in your API/Imgur keys and preferred settings then save the file.
settings = configparser.ConfigParser()
settings.read('Settings.ini')
startTime = dt.utcnow()






# -------------------------------
#       Global Variables
# -------------------------------

Bot_Token = settings['BOTSETTINGS']['token']
admin_ids = [str(settings['BOTSETTINGS']['owner-id'])]
botadmin = settings['BOTSETTINGS']['BotAdmin']
command_channel = settings['BOTSETTINGS']['DefaultChannel']
meme_channel = settings['BOTSETTINGS']['MemeChannel']
music_channel = settings['BOTSETTINGS']['MusicChannel']
playlist_channel =  settings['BOTSETTINGS']['PlaylistChannel']
Imgur_ID = settings['IMGUR']['ID']
Imgur_Secret = settings['IMGUR']['Secret']
vote_wipe = bool(settings['VOTESETTINGS']['VoteWipe'])
vote_channel = settings['VOTESETTINGS']['VoteChannel'].lower()
if settings['BOTSETTINGS']['currentgame'] == "None":
    current_game = None







# -------------------------------
#   Lists (Locations/Words)
# -------------------------------

# Location of Opus Libraries
OPUS_LIBS = ['content/libraries/libopus-0.x86.dll','content/libraries/libopus-0.x64.dll','content/libraries/libopus-0.dll','content/libopus.0.dylib','/usr/local/Cellar/opus/1.1.2/lib/libopus.0.dylib']
# Wordlist for google, youtube and add/play commands to prevent NSFW Results
NSFW = ["4r5e","rape","5h1t","5hit","a55","anal","anus","ar5e","arrse","niggers","arse","ass-fucker","asses","assfucker","assfukka","asshole","assholes","asswhole","a_s_s","b!tch","b00bs","b17ch","b1tch","ballbag","balls","ballsack","bastard","beastial","beastiality","bellend","bestial","bestiality","bi+ch","biatch","bitch","bitcher","bitchers","bitches","bitchin","bitching","bloody","blow job","blowjob","blowjobs","boiolas","bollock","bollok","boner","boob","boobs","booobs","boooobs","booooobs","booooooobs","breasts","buceta","bugger","bum","bunny fucker","butt","butthole","buttmuch","buttplug","c0ck","c0cksucker","carpet muncher","cawk","chink","cipa","cl1t","clit","clitoris","clits","cnut","cock","cock-sucker","cockface","cockhead","cockmunch","cockmuncher","cocks","cocksuck ","cocksucked ","cocksucker","cocksucking","cocksucks ","cocksuka","cocksukka","cok","cokmuncher","coksucka","coon","cox","crap","cum","cummer","cumming","cums","cumshot","cunilingus","cunillingus","cunnilingus","cunt","cuntlick ","cuntlicker ","cuntlicking ","cunts","cyalis","cyberfuc","cyberfuck ","cyberfucked ","cyberfucker","cyberfuckers","cyberfucking ","d1ck","damn","dick","dickhead","dildo","dildos","dink","dinks","dirsa","dlck","dog-fucker","doggin","dogging","donkeyribber","doosh","duche","dyke","ejaculate","ejaculated","ejaculates ","ejaculating ","ejaculatings","ejaculation","ejakulate","f u c k","f u c k e r","f4nny","fag","fagging","faggitt","faggot","faggs","fagot","fagots","fags","fanny","fannyflaps","fannyfucker","fanyy","fatass","fcuk","fcuker","fcuking","feck","fecker","felching","fellate","fellatio","fingerfuck ","fingerfucked ","fingerfucker ","fingerfuckers","fingerfucking ","fingerfucks ","fistfuck","fistfucked ","fistfucker ","fistfuckers ","fistfucking ","fistfuckings ","fistfucks ","flange","fook","fooker","fuck","fucka","fucked","fucker","fuckers","fuckhead","fuckheads","fuckin","fuckingshitmotherfucker","fuckme ","fucks","fuckwhit","fuckwit","fudge packer","fudgepacker","fuk","fuker","fukker","fukkin","fuks","fukwhit","fukwit","fux","fux0r","f_u_c_k","gangbang","gangbanged ","gangbangs ","gaylord","gaysex","goatse","God","god-dam","god-damned","goddamn","goddamned","hardcoresex ","heshe","hoar","hoare","hoer","homo","hore","horniest","horny","hotsex","jack-off ","jackoff","jap","jerk-off ","jism","jiz ","jizm ","jizz","kawk","knob","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kum","kummer","kumming","kums","kunilingus","l3i+ch","l3itch","labia","lmfao","lust","lusting","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","masochist","master-bate","masterb8","masterbat*","masterbat3","masterbate","masterbation","masterbations","masturbate","mo-fo","mof0","mofo","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked ","mothafucker","mothafuckers","mothafuckin","mothafucks","mother fucker","motherfuck","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","muff","mutha","muthafecker","muthafuckker","muther","mutherfucker","n1gga","n1gger","nazi","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers ","nob","nob jokey","nobhead","nobjocky","nobjokey","numbnuts","nutsack","orgasim ","orgasims ","orgasm","orgasms ","p0rn","pawn","pecker","penis","penisfucker","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","pigfucker","pimpis","piss","pissed","pisser","pissers","pisses ","pissflaps","pissin ","pissing","pissoff ","poop","porn","porno","pornography","pornos","prick","pricks ","pron","pube","pusse","pussi","pussies","pussy","pussys ","rectum","retard","rimjaw","rimming","s hit","s.o.b.","sadist","schlong","screwing","scroat","scrote","scrotum","semen","sh!+","sh!t","sh1t","shag","shagger","shaggin","shagging","shemale","shi+","shit","shitdick","shite","shited","shitey","shitfuck","shitfull","shithead","shiting","shitings","shits","shitted","shitter","shitters ","shitting","shittings","shitty ","skank","slut","sluts","smegma","smut","snatch","son-of-a-bitch","spac","spunk","s_h_i_t","t1tt1e5","t1tties","teets","teez","testical","testicle","tit","titfuck","tits","titt","tittie5","tittiefucker","titties","tittyfuck","tittywank","titwank","tosser","turd","tw4t","twat","twathead","twatty","twunt","twunter","v14gra","v1gra","vagina","viagra","vulva","w00se","wang","wank","wanker","wanky","whoar","whore","willies","willy","xrated","xxx","childporn","ch1ldp0rn","child-porn","rape","r4pe","r4p3","snuff","necrophillia","necro-porn","n3cr0","r4p3","gore","g0r3","g0re","gor3","lolita","l0l1tA","l0lita","l0lit4","jailbait","underage","necro","cp","incest","scat","fist me","fistme","cumshot","masturbation","hitler","h1tl3r","nazigermany","nazi germany","ear rape","35r r4p3","cumpilation","ahole","anus","ash0le","ash0les","asholes","AssMonkey","Assface","assh0le","assh0lez","assholz","asswipe","azzhole","bassterds","bastardz","basterds","basterdz","boffing","butthole","buttwipe","c0ck","c0cks","c0k","CarpetMuncher","cawk","cawks","Clit","cnts","cntz","cock","cockhead","cockhead","cocks","CockSucker","cocksucker","cum","cunt","cunts","cuntz","dild0","dild0s","dildo","dildos","dilld0","dilld0s","dominatricks","dominatrics","dominatrix","dyke","enema","fag1t","faget","fagg1t","faggit","faggot","fagit","fags","fagz","faig","faigs","fart","flipping","FudgePacker","fuk","Fukah","Fuken","fuker","Fukin","Fukk","Fukkah","Fukken","Fukker","Fukkin","g00k","gaybor","gayboy","gaygirl","gays","gayz","Goddamned","h00r","h0ar","h0re","hoar","hoor","hoore","jackoff","jerkoff","kunt","kunts","kuntz","Lesbian","Lezzian","Lipshits","Lipshitz","masochist","masokist","massterbait","masstrbait","masstrbate","masterbaiter","masterbate","masterbates","mutha","fuker","motha","fucker","fuker","fukka","fukkah","fucka","fuchah","fukker","fukah","MothaFucker","MothaFuker","MothaFukkah","MothaFukker","MotherFucker","MotherFukah","MotherFuker","MotherFukkah","MotherFukker","motherfucker","MuthaFucker","MuthaFukah","MuthaFuker","MuthaFukkah","MuthaFukker","mutha","n1gr","nastt","nasty","nigur","niiger","niigr","orafis","oriface","orifice","orifiss","packi","packie","packy","paki","pakie","paky","pecker","peeenus","peeenusss","peenus","peinus","pen1s","penas","penis","penisbreath","penus","penuus","Phuc","Phuck","Phuk","Phuker","Phukker","polac","polack","polak","Poonani","pr1c","pr1ck","pr1k","pusse","pussee","puuke","puuker","queer","queers","queerz","qweers","qweerz","qweir","recktum","rectum","retard","sadist","scank","schlong","screwing","semen","shitz","Shyt","Shyte","Shytty","Shyt","skanck","skank","skankee","skankey","skanks","Skanky","sonofabitch","tit","turd","va1jina","vag1na","vagiina","vagina","vaj1na","vajina","vullva","vulva","w0p","wh00r","wh0re","whore","xrated","xxx","bch","blowjob","clit","arschloch","boiolas","buceta","c0ck","cawk","chink","cipa","clits","cock","cum","cunt","dildo","dirsa","ejakulate","fatass","fcuk","fuk","fux0r","hoer","hore","jism","kawk","l3itch","l3i+ch","lesbian","masturbate","masterbat","masterbat3","motherfucker","s.o.b.","mofo","nazi","nigger","scrotum","shemale","shi+","testical","testicle","titt","w00se","jackoff","wank","whoar","whore","damn","dyke","amcik","andskota","arse","assrammer","ayir","breasts","buttpirate","cabron","cazzo","chraa","chuj","Cock","cunt","d4mn","daygo","dego","dick","dike","dupa","dziwka","ejackulate","Ekrem","Ekto","enculer","faen","fag","fanculo","fanny","feces","feg","Felcher","ficken","fitt","Flikker","foreskin","Fotze","Fu","fuk","futkretzn","gay","gook","guiena","h0r","h4x0r","helvete","hoer","honkey","Huevon","hui","injun","kanker","kike","klootzak","kraut","knulle","kuk","kuksuger","Kurac","kurwa","kusi","kyrpa","lesbo","mamhoon","masturbat","merd","mibun","monkleigh","mouliewop","muie","mulkku","muschi","nazis","nepesaurio","nigger","orospu","paska","perse","picka","pierdol","pillu","pimmel","piss","pizda","poontsee","poop","porn","p0rn","pr0n","preteen","pula","pule","puta","puto","qahbeh","queef","rautenberg","schaffer","scheiss","schlampe","schmuck","screw","sharmuta","sharmute","shipal","shiz","skrib", "big black","titties"]
spamlist = ["vine","vines","vinecompilation","kazoo","kazookid","rape","earrape","hours","hourlong","hour","montage","pewds","pewdiepie","keemsta","keeem","meme","compilation","KEEMSTAR","keemstar","memestar","shrek","cod","meme-star","keem","k33mst4r","k33mstar","nigger","#dramaalert","dramaalert","niggers","leafy","pewdiepie","minecraft","pingu","ecks dee","meems","meem","faggot","f4gg0t","f4550t","nazi","n4zi","anal","4n4l","ecks de","fist me","fistme","cumshot","masturbation","hitler","h1tl3r","nazigermany","nazi germany","ear rape","35r r4p3","cumpilation","ahole","anus","ash0le","ash0les","asholes","AssMonkey","Assface","assh0le","assh0lez","assholz","asswipe","azzhole","bassterds","bastardz","basterds","basterdz","boffing","butthole","buttwipe","c0ck","c0cks","c0k","CarpetMuncher","cawk","cawks","Clit","cnts","cntz","cock","cockhead","cockhead","cocks","CockSucker","cocksucker","cum","cunt","cunts","cuntz","dild0","dild0s","dildo","dildos","dilld0","dilld0s","dominatricks","dominatrics","dominatrix","dyke","enema","fag1t","faget","fagg1t","faggit","faggot","fagit","fags","fagz","faig","faigs","fart","flipping","FudgePacker","fuk","Fukah","Fuken","fuker","Fukin","Fukk","Fukkah","Fukken","Fukker","Fukkin","g00k","gaybor","gayboy","gaygirl","gays","gayz","Goddamned","h00r","h0ar","h0re","hoar","hoor","hoore","jackoff","jap","japs","jerkoff","jisim","jiss","jizm","jizz","knob","knobs","knobz","kunt","kunts","kuntz","Lesbian","Lezzian","Lipshits","Lipshitz","masochist","masokist","massterbait","masstrbait","masstrbate","masterbaiter","masterbate","masterbates","mutha","fuker","motha","fucker","fuker","fukka","fukkah","fucka","fuchah","fukker","fukah","MothaFucker","MothaFuker","MothaFukkah","MothaFukker","MotherFucker","MotherFukah","MotherFuker","MotherFukkah","MotherFukker","motherfucker","MuthaFucker","MuthaFukah","MuthaFuker","MuthaFukkah","MuthaFukker","mutha","n1gr","nastt","nasty","nigur","niiger","niigr","orafis","oriface","orifice","orifiss","packi","packie","packy","paki","pakie","paky","pecker","peeenus","peeenusss","peenus","peinus","pen1s","penas","penis","penisbreath","penus","penuus","Phuc","Phuck","Phuk","Phuker","Phukker","polac","polack","polak","Poonani","pr1c","pr1ck","pr1k","pusse","pussee","puuke","puuker","queer","queers","queerz","qweers","qweerz","qweir","recktum","rectum","retard","sadist","scank","schlong","screwing","semen","shitz","Shyt","Shyte","Shytty","Shyt","skanck","skank","skankee","skankey","skanks","Skanky","sonofabitch","tit","turd","va1jina","vag1na","vagiina","vagina","vaj1na","vajina","vullva","vulva","w0p","wh00r","wh0re","whore","xrated","xxx","bch","blowjob","clit","arschloch","boiolas","buceta","c0ck","cawk","chink","cipa","clits","cock","cum","cunt","dildo","dirsa","ejakulate","fatass","fcuk","fuk","fux0r","hore","jism","kawk","l3itch","l3i+ch","lesbian","masturbate","masterbat","masterbat3","motherfucker","s.o.b.","mofo","nazi","nigger","scrotum","shemale","shi+","testical","testicle","titt","w00se","jackoff","wank","whoar","whore","damn","dyke","amcik","andskota","arse","assrammer","ayir","bi7ch","bollock","breasts","buttpirate","cabron","cazzo","chraa","chuj","Cock","cunt","d4mn","daygo","dego","dick","dike","dupa","dziwka","ejackulate","Ekrem","Ekto","enculer","faen","fag","fanculo","fanny","feces","feg","Felcher","ficken","fitt","Flikker","foreskin","Fotze","Fu","fuk","futkretzn","gay","gook","guiena","h0r","h4x0r","helvete","hoer","honkey","Huevon","hui","injun","jizz","kanker","kike","klootzak","kraut","knulle","kuk","kuksuger","Kurac","kurwa","kusi","kyrpa","lesbo","mamhoon","masturbat","merd","mibun","monkleigh","mouliewop","muie","mulkku","muschi","nazis","nepesaurio","nigger","orospu","paska","perse","picka","pierdol","pillu","pimmel","piss","pizda","poontsee","poop","porn","p0rn","pr0n","preteen","pula","pule","puta","puto","qahbeh","queef","rautenberg","schaffer","scheiss","schlampe","schmuck","screw","sharmuta","sharmute","shipal","shiz","skrib"]






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
#       NootBot class
# -------------------------------

class NootBot(discord.Client):

    def __init__(self):
        super().__init__()
        self.servers_dict = {}
        self.token = Bot_Token
        self.pepe = []
        self.slav = []
        self.doggo = []
        self.music_players = {}
        self.get_imgur()
        self.command_prefix = settings['PREFIX']['CommandPrefix']
        self.currentgame = settings['BOTSETTINGS']['currentgame']
        self.wolfram_client = wolframalpha.Client(settings['WOLFRAM']['app_id'])
        self.days = 0

        self.lock_status = False



        # Voting variables
        self.yes_votes = []
        self.no_votes = []
        self.abstained = []
        self.vote_status = False
        self.vote_topic = ""
        self.vote_author = ""
        self.results = ""
        self.isPublic = False
        self.vote_type = "Private"


    # Loads imgur client and specific album variables
    def get_imgur(self):
        client = imgurpython.ImgurClient(Imgur_ID, Imgur_Secret)
        self.pepe = client.get_album_images('PI6Co')
        self.slav = client.get_album_images('Yx4sw')
        self.doggo = client.get_album_images('k43YN')


    # Returns string format for displaying a list of commands (such as !help, !music etc...)
    def print_commands(self,file):
        string = ''
        fc = open(file, 'r')
        help_file = fc.read()
        fc.close()
        help = help_file.split('\n')
        for i in range(0, (len(help) - 1)):
            temp = help[i].format(self.command_prefix)
            string = string + temp + '\n'
        return '```markdown\n' + string + '```'



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
        print('Noot Noot!')
        print('')
        print('Visit: https://noot.tech/')

        for server in self.servers:
            mp = player.Player(self, server)
            self.music_players[server.id] = mp

        # On Launch set current game bot is playing
        await self.change_status(discord.Game(name=self.currentgame))

        self.bot_id = '<@' + self.user.id + '>'
        self.nick_id = '<@!' + self.user.id + '>'





    def meme_of_the_day(self,meme):
        if meme == 'pepe':
            return self.pepe[random.randint(0, len(self.pepe))].link
        if meme == 'slav':
            return self.slav[random.randint(0, len(self.slav))].link
        if meme == 'doggo':
            return self.doggo[random.randint(0, len(self.doggo))].link











    async def on_message(self, message):

        mp = None
        private = False
        admin = False
        Mod = False
        subMod = False
        directory = 'content/servers/' + message.server.id + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = directory + str(message.server.id) + '_blacklist.txt'

        file = open(path, 'a')
        blacklisted = False
        with open(path) as f:
            for line in f:
                if message.author.id in line:
                    blacklisted = True


        # Checks if the message being sent is a PM. If not, music player can be used.
        if message.channel.is_private:
            private = True

        if private:
            try:
                cb2 = cleverbot.Cleverbot()
                answer = cb2.ask(message.content)
                await self.send_message(message.author, str(answer))
            except:
                print("Private message sent")




        # Checks if the message author is a BotAdmin.
        for role in message.author.roles:
            if "denBot" in role.name or "Loser" in role.name or "Server Owner" in role.name:
                admin = True
            elif "Fag" in role.name or "Admin" in role.name:
                Mod = True
            elif "Retard" in role.name or "Mod" in role.name:
                subMod = True












        try:
            mp = self.music_players[message.server.id]
        except:
            print('Failed to time-out from ' + message.server.name + " [" + str(message.server.id) + "]")
            print("Bot may get error 403 because of this.")






        if message.author.bot == False and private == False:

            # Checks if message is from a Bot.
            if message.content.startswith(self.command_prefix) == False:
                if ("<@" not in message.content):
                    directory = 'content/servers/' + message.server.id + "/"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    wcpath = directory + str(message.server.id) + '_wordcloud.txt'
                    file = open(wcpath, 'a')
                    file.write(' '+message.content)
                    file.close()







        if message.content.lower().startswith('!lock') and admin:
            self.lock_status = True
            await self.send_message(message.channel,
                                    message.author.mention + ' has locked the bot for maintenance.')

        if message.content.lower().startswith('!unlock') and admin:
            self.lock_status = False
            await self.send_message(message.channel, message.author.mention + ' has unlocked the bot.')







        # -------------------------------
        #       SuperAdmin Bot Commands
        # -------------------------------


        if message.content.startswith(self.command_prefix) and blacklisted == False and self.lock_status==False:

            cmd = message.content[1:]

            # --------------------------------
            #    Meme commands (in #meme only)
            # --------------------------------




            if meme_channel in message.channel.name.lower():
                if cmd.lower().startswith('pepe'):
                    await self.send_message(message.channel, self.meme_of_the_day('pepe'))

                elif cmd.lower().startswith('slav'):
                    await self.send_message(message.channel, self.meme_of_the_day('slav'))

                elif cmd.lower().startswith('doggo'):
                    await self.send_message(message.channel, self.meme_of_the_day('doggo'))









            if vote_channel in message.channel.name.lower():

                if cmd.lower().startswith('startvote'):

                    if admin or Mod or subMod:
                        if self.vote_status:
                            await self.send_message(message.channel, "A vote is currently taking place. :x:")
                        else:

                            if "-public " in cmd:
                                self.isPublic = True
                                self.vote_type = "Public"
                                cmd = cmd.replace("-public ", "")

                            if len(cmd.lower().replace('startvote ', '')) < 10:
                                await self.send_message(message.channel,message.author.mention+" The vote topic is too short. Please try something more detailed. :x:")
                            else:
                                self.vote_author = message.author.id
                                self.vote_status = True
                                self.raw_topic = cmd[10:]
                                self.yes_votes, self.no_votes, self.abstained = [],[],[]

                                if vote_wipe == True:
                                    try:
                                        await self.purge_from(message.channel, limit=100)
                                    except:
                                        print("Cleared chat but Exception 404 thrown.")

                                line_breaker = ""

                                for i in "Topic: "+self.raw_topic:
                                    line_breaker += "="

                                self.vote_topic = "```markdown\n"\
                                                  "Topic: "+cmd[10:]+ '\n'+line_breaker + \
                                                  "\n\n# Votes cannot be changed after submission." \
                                                  "\n# Type !votehelp in #bot ir #vote for a list of commands." \
                                                  "```"
                                await self.send_message(message.channel, "Attention: A new `"+self.vote_type+"` vote has been started by "+message.author.mention+".\n"+self.vote_topic)
                    else:
                        await self.send_message(message.channel, message.author.mention+" You must be an Admin or Moderator to start a vote. :x:")




                if cmd.lower().startswith('topic'):
                    if self.vote_status:
                        await self.send_message(message.channel, self.vote_topic)
                        await self.delete_message(message)
                    else:
                        await self.send_message(message.channel, message.author.mention+" There is currently no vote taking place. :x:")
                        await self.delete_message(message)


                elif cmd.lower().startswith('votehelp'):
                    cmd = self.print_commands('content/txt/vote.txt')
                    await self.send_message(message.channel, message.author.mention+" has requested vote the vote commands: "+cmd)
                    await self.delete_message(message)




                elif cmd.lower().startswith('vote '):

                    if admin or Mod or subMod or self.isPublic:

                        if self.vote_status:
                            vote = cmd.replace('vote ','')
                            if (message.author.id in self.yes_votes) or (message.author.id in self.no_votes):
                                await self.send_message(message.channel, message.author.mention+ " You have already submitted a vote. :x:")
                                await self.delete_message(message)
                            else:
                                if 'yes' in vote.lower():
                                    self.yes_votes.append(message.author.id)
                                    await self.send_message(message.channel, message.author.mention+" has their submitted a vote. :white_check_mark:")
                                    await self.delete_message(message)
                                elif 'no' in vote.lower():
                                    self.no_votes.append(message.author.id)
                                    await self.send_message(message.channel, message.author.mention+" has their submitted a vote. :white_check_mark:")
                                    await self.delete_message(message)
                        else:
                            await self.send_message(message.channel, "\n"+message.author.mention+" There is no vote currently taking place.")
                            await self.delete_message(message)
                    else:
                        await self.send_message(message.channel, "\n"+message.author.mention+" Sorry this vote is set to `Private `. You must be an Admin or Mod to be able to vote.")
                        await self.delete_message(message)





                elif cmd.lower().startswith('endvote'):

                    if self.vote_author == message.author.id or admin or Mod:

                        # Calculate abstained members:
                        vote_participants = []



                        for member in message.server.members:
                            if (member.status == discord.Status.online or member.status == discord.Status.idle) and member.id != self.user.id:
                                if self.isPublic == False:
                                    for role in member.roles:
                                        if "Admin" in role.name or "Mod" in role.name or "Loser" in role.name:
                                            vote_participants.append(member.id)
                                            break
                                else:
                                    vote_participants.append(member.id)



                        for id in vote_participants:
                            if id in self.yes_votes or id in self.no_votes:
                                continue
                            else:
                                self.abstained.append(id)


                        if self.vote_status:
                            res = "Results for "+self.raw_topic
                            breaker = ""
                            for i in res:
                                breaker += "'"

                            if len(res) % 2 == 0:
                                breaker += "'"

                            self.results = ("```python\n"+breaker+"\n"+res+"\n"+breaker+"\n\n- Yes: " + str(len(self.yes_votes)) + "\n- No: " + str(len(self.no_votes)) + "\n- Abstained: " + str(len(self.abstained)) + "\n\n"+breaker+"```")
                            await self.send_message(message.channel,"The vote has been ended by: "+message.author.mention)
                            await self.send_message(message.channel,self.results)
                            await self.delete_message(message)
                            self.vote_status = False
                            self.isPublic = False
                            self.vote_type = "Private"

                        else:
                            await self.send_message(message.channel, message.author.mention+" There is no vote currently taking place.")
                            await self.delete_message(message)
                    else:
                        await self.send_message(message.channel, message.author.mention+" You must be an Admin or the vote author to end the vote.")
                        await self.delete_message(message)



                elif cmd.lower().startswith('results'):
                    if self.results == "":
                        await self.send_message(message.channel, "The results from the previous vote have been wiped.")
                    else:
                        await self.send_message(message.channel, "Results from previous vote:\n"+self.results)









            if command_channel in message.channel.name.lower():



                # Music configuration (capacity, song length, queue limit, max requests.

                if message.author.id in admin_ids or admin or Mod:

                    if cmd.lower().startswith('music max-capacity '):
                        cap = cmd.lower().replace('music max-capacity ', '')
                        try:
                            cap = int(cap)
                            if cap < 1:
                                await self.send_message(message.channel,message.author.mention+" The Playlist must have a minimum capacity of 5. :x:")
                            elif cap > 100:
                                await self.send_message(message.channel,message.author.mention+" We can only allow a maximum Playlist capacity of 100 songs... for now. :x:")
                            else:
                                settings['PLAYER']['BotPlaylistCap'] = cap
                                with open("content/Settings.ini", "w") as settingsfile:
                                    settings.write(settingsfile)
                                await self.send_message(message.channel,"The maximum playlist capacity has been changed to: " + cap + " song(s).")
                        except:
                            await self.send_message(message.channel,"The maximum playlist capacity could not be changed.")


                    elif cmd.lower().startswith('music song-length '):
                        cap = cmd.lower().replace('music song-length ', '')
                        try:
                            cap = int(cap)

                            if cap < 4:
                                await self.send_message(message.channel,
                                                  message.author.mention + " The max song length limit can only be set to a `minimum of 4 minutes`. :x:")
                            elif cap > 120:
                                await self.send_message(message.channel,
                                                  message.author.mention + " We can only allow a maximum song length limit of 120 Minutes (2 hours). :x:")
                            else:
                                settings['PLAYER']['MaxSongLength'] = cap
                                with open("content/Settings.ini", "w") as settingsfile:
                                    settings.write(settingsfile)
                                await self.send_message(message.channel,"Maximum song length limit has been changed to: " + cap + " minutes.")
                        except:
                            await self.send_message(message.channel,"Maximum song length limit could not be changed.")



                    elif cmd.lower().startswith('music queue-limit '):
                        cap = cmd.lower().replace('music queue-limit ', '')
                        try:
                            cap = int(cap)
                            if cap < 1:
                                await self.send_message(message.channel,message.author.mention+" The YouTube Playlist Queue limit must be a minimum of 1 song. :x:")
                            elif cap > 50:
                                await self.send_message(message.channel,message.author.mention+" We can only allow a maximum YouTube Playlist Queue of 50 songs. :x:")
                            else:
                                settings['PLAYER']['YoutubePlaylistCap'] = cap
                                with open("content/Settings.ini", "w") as settingsfile:
                                    settings.write(settingsfile)
                                await self.send_message(message.channel,"Maximum YouTube queue limit has been changed to: " + str(cap) + " song(s).")
                        except:
                            await self.send_message(message.channel,"Maximum YouTube queue limit could not be changed.")



                    elif cmd.lower().startswith('music max-requests '):
                        cap = cmd.lower().replace('music max-requests ', '')
                        try:
                            cap = int(cap)
                            if cap < 1:
                                await self.send_message(message.channel,message.author.mention+" The max song requests per user must be a minimum of 1 songs. :x:")
                            elif cap > 15:
                                await self.send_message(message.channel,message.author.mention+" The max song requests per user must be a maximum of 15 songs. :x:")
                            else:
                                settings['PLAYER']['MaxUserSongRequests'] = str(cap)
                                with open("content/Settings.ini", "w") as settingsfile:
                                    settings.write(settingsfile)
                                await self.send_message(message.channel,"The maximum song request amount (per user) has been changed to: " + str(cap) + " song(s).")
                        except:
                            await self.send_message(message.channel,"The maximum song request amount could not be changed.")


                    elif cmd.lower()=='music settings':
                        breaker = ""
                        for i in (message.server.name+" Music Player Settings:"):
                            breaker += "="
                        contents = (message.server.name+" Music Player Settings:\n"+ \
                                    breaker+"\n"+\
                                   "\n[Max Playlist Song Capacity]: "+str(settings['PLAYER']['BotPlaylistCap'])+ \
                                   "\n[Max Song Length (before auto-skip)]: "+str(settings['PLAYER']['MaxSongLength'])+ \
                                   "\n[Max YouTube Playlist Queue Amount]: "+str(settings['PLAYER']['YoutubePlaylistCap'])+\
                                   "\n[Max User Song Requests]: "+str(settings['PLAYER']['MaxUserSongRequests'])+\
                                   "\n"
                                   "\nType !music for a list of music commands."+\
                                   "\n------------------------------------------")
                        msg = "```markdown\n"+contents+"```"
                        await self.send_message(message.channel,msg)












                if cmd.lower().startswith('invite'):
                    if message.author.id == str(settings['BOTSETTINGS']['owner-id']):
                        invite = 'https://discordapp.com/oauth2/authorize?&client_id='+str(settings['BOTSETTINGS']['bot-id'])+'&scope=bot&permissions=0'
                        await self.send_message(message.author, invite)
                    else:
                        await self.send_message(message.channel, 'Sorry, only the bot owner can do this.')


                elif cmd.lower().startswith('leave'):
                    if message.author.id in admin_ids or message.author.id == str(settings['BOTSETTINGS']['owner-id']):
                        await self.leave_server(message.server)
                    else:
                        await self.send_message(message.channel, 'Sorry, only Server Owners and the bot owner can do this.')





                elif cmd.lower().startswith('restart'):
                    if message.author.id in admin_ids or admin == True:
                        await self.change_status(discord.Game(name="RESTARTING"))
                        msg = await self.send_message(message.channel,
                                                      'Restarting ' + self.user.name + " in 5 seconds...")

                        seconds = 4
                        while seconds > -1:
                            await asyncio.sleep(1)
                            await self.edit_message(msg, 'Restarting ' + self.user.name + " in " + str(seconds) + " seconds...")
                            seconds = seconds - 1


                        await self.edit_message(msg, self.user.name + " is now going online.")

                        try:
                            python = sys.executable
                            os.execl(python, python, *sys.argv)
                        except:
                            await self.edit_message(msg, self.user.name + " failed to restart.")
                    else:
                        await self.send_message(message.channel, 'Sorry, only Bot Owners and Server Admins can do this.')



                elif cmd.lower().startswith('shutdown'):
                    if message.author.id in admin_ids:
                        await self.change_status(discord.Game(name="SHUTTING DOWN"))
                        msg = await self.send_message(message.channel,'Shutting down ' + self.user.name + " in 5 seconds...")
                        seconds = 4
                        while seconds > -1:
                            await asyncio.sleep(1)
                            await self.edit_message(msg, 'Shutting down ' + self.user.name + " in " + str(seconds) + " seconds...")
                            seconds = seconds - 1
                        await self.edit_message(msg, self.user.name + " is now offline.")
                        exit()
                    else:
                        await self.send_message(message.channel, 'Sorry, only Bot Owner can do this.')












                elif cmd.lower().startswith('git'):
                    if message.author.id == str(settings['BOTSETTINGS']['owner-id']):
                        if "-pull" in cmd.lower():
                            cwd = os.getcwd()
                            repo = git.Repo(os.getcwd())
                            head = repo.heads[0].name
                            x = str(cwd).split("/")[-1]

                            try:
                                git.cmd.Git(cwd).pull()
                                msg = await self.send_message(message.channel,
                                                              'Attempting Git Pull... :hourglass_flowing_sand: ')
                                await asyncio.sleep(2)
                                result = await self.edit_message(msg, x+" "+head+' Pull was successful. :pencil:')
                                print(x + " git pull completed.")
                                await asyncio.sleep(30)
                                await self.delete_message(result)
                            except:
                                msg = await self.send_message(message.channel,
                                                              'Attempting Git Pull... :hourglass_flowing_sand: ')
                                await asyncio.sleep(2)
                                result = await self.edit_message(msg,  x+" "+head+' Pull was un-successful. :x:')
                                await asyncio.sleep(30)
                                await self.delete_message(result)


                        if "-info" in cmd.lower():
                            msg = await self.send_message(message.channel, 'Gathering Github Repo Information... :hourglass_flowing_sand: ')
                            await asyncio.sleep(2)
                            repo = git.Repo(os.getcwd())
                            desc = repo
                            result = await self.edit_message(msg,'```erl\nGithub Repo Info:\nBla Bla bla\nDescription: '+desc+'```')
                            await asyncio.sleep(30)
                            await self.delete_message(result)
                    else:
                        await self.send_message(message.channel, 'Sorry, only the Bot Owner can do this.')









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
                                await self.send_message(message.channel,self.user.name + "'s current game has been changed to: `" +settings['BOTSETTINGS']['currentgame'] + "`")
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
                        if url.lower().startswith('default') or url.lower().startswith('reset') :
                            url = 'https://noot.tech/c/NootTechIcon.jpg'

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
                #        VOICE Commands
                # -------------------------------

                elif cmd.lower().startswith('connect'):
                    if (message.author.id in admin_ids or admin == True or Mod == True or subMod == True):
                        if message.author.voice_channel.name == music_channel:
                            try:
                                await self.send_message(message.channel, 'Connected to '+music_channel+'.')
                                await mp.get_voice_client(message.author.voice_channel, True)
                            except discord.errors.InvalidArgument:
                                await self.send_message(message.channel,'Error connecting to voice channel... :(')
                        else:
                            await self.send_message(message.channel, 'You have to be in the '+music_channel+' channel to be able to connect the bot.')
                    else:
                        await self.send_message(message.channel, 'Sorry, only Server Owners, Admins or Mods can connect the bot to a voice channel.')




                elif cmd.lower().startswith('disconnect'):
                    if message.author.id in admin_ids or admin == True or Mod == True:
                        await mp.disconnect_voice_client()
                        await self.change_status(discord.Game(name=self.currentgame))
                        await self.send_message(message.channel, 'Disconnected from '+music_channel+'.')
                    else:
                        await self.send_message(message.channel, 'Sorry, only Server Owners or Admins can disconnect the bot from a voice channel.')




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
                        await self.send_message(message.channel,"You need to be in the same channel as the bot to remove a song!")






                elif cmd.lower().startswith('volume '):

                    cmd = cmd.lower().replace('volume ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True or subMod == True:
                        await mp.change_volume(cmd, message.channel)
                    else:
                        await self.send_message(message.channel, "Please ask a moderator or admin to change the volume for you! :wink:")





                elif cmd.lower().startswith('currentsong') or cmd.lower().startswith('playing') or cmd.lower().startswith('song'):
                    await mp.current_song(message)



                elif cmd.lower().startswith('add '):
                    if message.author.voice_channel == mp.voice_client.channel:
                        L = []
                        link = cmd[4:]

                        if len(link) < 8:
                            await self.send_message(message.channel,"Your search needs to contain a minimum of 8 characters.")
                        else:
                            if 'http://' in link or 'https://' in link:
                                args = link
                            else:
                                query = urllib.parse.quote(link)
                                url = "https://www.youtube.com/results?search_query=" + query
                                soup = bs4.BeautifulSoup(urlopen(url).read(), "lxml")
                                for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                                    if len(video['href']) < 25 and "?v=" in video['href']:
                                        L.append('https://www.youtube.com' + video['href'])
                                args, link = L[0], L[0]


                            if "youtube" in link.lower():
                                phrase = etree.HTML(urlopen(link).read()).xpath("//span[@id='eow-title']/@title")
                                title = phrase[0]
                                phrase = phrase[0].lower().replace("[","").replace("]","").replace("(","").replace(")","").split(' ')

                            elif "soundcloud" in link.lower() and 'http:' in link.lower():
                                title = args.lower().replace("[","").replace("]","").replace("(","").replace(")","").replace("http://soundcloud.com/", "").replace("-", " ").split("/")
                                title = title[0]+" - "+title[1]
                                phrase = args.lower().replace("http://soundcloud.com/", "").replace("-", " ").split("/")

                            elif "soundcloud" in link.lower() and 'https:' in link.lower():
                                title = args.lower().replace("[","").replace("]","").replace("(","").replace(")","").replace("https://soundcloud.com/", "").replace("-", " ").split("/")
                                title = title[0] + " - " + title[1]
                                phrase = args.lower().replace("https://soundcloud.com/", "").replace("-", " ").split("/")

                            elif "bandcamp" in link.lower() and 'https:' in link.lower():
                                title = link.replace("-"," ").replace("bandcamp/track/","").replace("https://","").replace("."," - ")
                                phrase = title.split(" - ")

                            elif "bandcamp" in link.lower() and 'http:' in link.lower():
                                title = link.replace("-", " ").replace("bandcamp/track/", "").replace("http://","").replace("."," - ")
                                phrase = title.split(" - ")


                            rejections = []
                            Spam = False

                            for item in phrase:
                                if item in spamlist:
                                    Spam = True
                                    rejections.append(item)

                            rejects = ""
                            for item in rejections:
                                rejects += " `" + item + "` "

                            if Spam == True and ("bandcamp" not in link or "soundcloud" not in link):
                                await self.send_message(message.channel,"Sorry. `"+title+"` could not be added to the playlist due to the following words:" + rejects)
                            else:
                                voice = await mp.get_voice_client()
                                if 'youtube' in args:
                                    player = await mp.get_player(voice.channel)
                                    if (len(mp.playlist) == 0 and player is None) or (len(mp.playlist) == 0 and player.is_done()):
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

                                elif 'bandcamp' in args:
                                    player = await mp.get_player(voice.channel)
                                    if (len(mp.playlist) == 0 and player is None) or (len(mp.playlist) == 0 and player.is_done()):
                                        await mp.add_playlist(args, message, type='b')
                                        await mp.audio_player(new=True)
                                    else:
                                        await mp.add_playlist(args, message, type='b')
                                else:
                                    msg = '{0.author.mention} : Invalid Link.'
                                    await self.send_message(message.channel, msg.format(message))
                    else:
                        await self.send_message(message.channel, "You need to be in the same channel as the bot to add a song!")



















                elif cmd.lower().startswith('block '):
                    cmd = cmd.lower().replace('block ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True:
                        if "<@" in cmd and self.user.id not in cmd and (len(cmd) > 19 and len(cmd) < 23):
                            directory = 'content/servers/'+message.server.id+"/"
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            path = directory+str(message.server.id)+'_blacklist.txt'
                            file = open(path, 'a')
                            member_id = cmd.replace("<@", "").replace(">", "").replace("!", "")
                            member = discord.utils.get(message.server.members, id=member_id)
                            occur = False
                            with open(path) as f:
                                for line in f:
                                    if member_id in line:
                                        occur = True
                            if occur == True:
                                await self.send_message(message.channel, "The user " + cmd + " is already blacklisted.")
                            else:
                                unblockable = False
                                for role in member.roles:
                                    if "denBot" in role.name or "Loser" in role.name:
                                        unblockable = True
                                        break
                                    elif "Fag" in role.name or "Admin" in role.name:
                                        unblockable = True
                                        break
                                if member_id in admin_ids or unblockable:
                                    await self.send_message(message.channel,"You cannot blacklist a server owner, bot admin or server admin.")
                                else:
                                    server = member.server
                                    bot_role = discord.Role
                                    for role in server.roles:
                                        if 'bot-ban' in role.name:
                                            bot_role = role
                                            break
                                    file.write(cmd + " - " + member.name + '\n')
                                    file.close()
                                    try:
                                        await client.add_roles(member, bot_role)
                                        await self.send_message(message.channel,"The user " + cmd + " has been `added` to the " + message.server.name + " blacklist and has been given bot-ban role.")
                                        await self.send_message(member,"You been `blacklisted` from using me on " + message.server.name + ". :(")
                                    except:
                                        await self.send_message(message.author,"Please create a bot-ban role that does not have posting access to the #bot chat and also give NootTech bot privileges to give people this role.")
                                        await self.send_message(message.channel,"User has been added to blacklist but `NOT` given bot-ban role due to server configuration.")
                                        await self.send_message(member,"You been `blacklisted` from using me on " + message.server.name + ". :(")
                        else:
                            await self.send_message(message.channel,
                                                    "Please use the @ prefix when adding someone to the blacklist, e.g. @denBot")
                    else:
                        await self.send_message(message.channel,
                                                "Only Bot Admins and Server Owners can add users to the bot blacklist.")




                elif cmd.lower().startswith('blacklist'):
                    cmd = cmd.lower().replace('block ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True:
                        try:
                            directory = 'content/servers/' + message.server.id + "/"
                            if not os.path.exists(directory):
                                os.makedirs(directory)

                            path = directory+str(message.server.id)+'_blacklist.txt'
                            blacklist = open(path)
                            strng = ""
                            for line in blacklist:
                                strng += line
                            await self.send_message(message.channel,
                                                    "```python\n " + message.server.name + " Blacklist:\n" + strng + "```")
                        except:
                            await self.send_message(message.channel,
                                                    "There was an error loading the blacklist - perhaps the list is empty.")

                    else:
                        await self.send_message(message.channel,
                                                "Only Bot Admins and Server Owners can view the server blacklist.")






                elif cmd.lower().startswith('unblock '):
                    cmd = cmd.lower().replace('unblock ', '')
                    if message.author.id in admin_ids or admin == True or Mod == True:
                        if "<@" in cmd and self.user.id not in cmd and (len(cmd) > 19 and len(cmd) < 23):
                            directory = 'content/servers/' + message.server.id + "/"
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            path = directory + str(message.server.id) + '_blacklist.txt'
                            occur = False
                            output = []
                            with open(path) as f:
                                for line in f:
                                    if cmd in line:
                                        occur = True
                                    else:
                                        output.append(line)
                            f.close()
                            member_id = cmd.replace("<@", "").replace(">", "").replace("!","")
                            member = discord.utils.get(message.server.members, id=member_id)
                            if occur == True:
                                server = member.server
                                bot_role = discord.Role
                                for role in server.roles:
                                    if 'bot-ban' in role.name:
                                        bot_role = role
                                        break
                                writer = open(path, 'w')
                                writer.writelines(output)
                                writer.close()
                                try:
                                    await client.remove_roles(member, bot_role)
                                    await self.send_message(message.channel,
                                                            "The user " + cmd + " has been `removed` from the " + message.server.name + " blacklist and bot-ban role.")
                                    await self.send_message(member,
                                                            "You been `removed` from the " + message.server.name + " blacklist and no longer have the bot-ban role.")
                                except:
                                    await self.send_message(message.channel,
                                                            "The user " + cmd + " has been `removed` from the " + message.server.name + " blacklist but `bot-ban could not be removed`.")
                                    await self.send_message(member,
                                                            "You been `removed` from the " + message.server.name + " blacklist but the `bot-ban role could not be removed`.")
                            else:
                                await self.send_message(message.channel,
                                                        member.name + " is not in the blacklist.")
                        else:
                            await self.send_message(message.channel,
                                                    "Please use the @ prefix when adding someone to the blacklist, e.g. @denBot")
                    else:
                        await self.send_message(message.channel,
                                                "Only Bot Admins and Server Owners can remove users to the bot blacklist.")



















































                # -------------------------------
                #      Normal Bot Commands
                # -------------------------------

                elif cmd.lower().startswith('wordcloud'):
                    wc_msg = await self.send_message(message.channel, 'Generating the wordcloud for "' + message.server.name+'"... :writing_hand:')
                    directory = '../servers/'+message.server.id +"/"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    wcpath = directory+str(message.server.id)+'_wordcloud.txt'
                    word.get_wordcloud(wcpath)
                    file.close()


                    try:

                        wc_img = await self.send_file(message.channel, 'result.png')
                        wc_msg = await self.edit_message(wc_msg,
                                                         '"' + message.server.name + '" Wordcloud on: `' + time.strftime(
                                                             "%c") + '`')
                    except:
                        await self.edit_message(wc_msg, "I can't upload images to " + message.server.name + ":frowning:")

                    os.remove('result.png')





                elif cmd.lower().startswith('uptime'):
                    uptime = (dt.utcnow() - startTime)
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
                        self.days += 1
                        int_hours = int(hours) - 24
                        hours = str(int_hours)
                    up = ('I have been online for: ' + str(
                        self.days) + " Days, " + hours + " Hours, " + minutes + " Minutes and " + seconds + " Seconds. :thinking:")
                    await self.send_message(message.channel, up.format(message))


                elif cmd.lower().startswith('playlist'):
                    if not private:
                        await mp.get_queue(message)
                    else:
                        msg = '{0.author.mention} : This command can not be done in a PM'
                        await self.send_message(self, message.channel, msg.format(message))






                elif cmd.lower().startswith('bosh'):
                    victim = cmd.replace("bosh ", "")
                    if self.user.id in victim:
                        await self.send_message(message.channel, message.author.mention+' get boshd! fukin rekt scrub')
                    elif settings['BOTSETTINGS']['owner-id'] in victim:
                        await self.send_message(message.channel, message.author.mention + " get boshd! u cunto")
                    elif "<@" in victim:
                        await self.send_message(message.channel, victim + ' just got boshd')

                elif cmd.lower().startswith('ping'):
                    await self.send_message(message.channel, 'Pong!')
                elif cmd.lower().startswith('pong'):
                    await self.send_message(message.channel, 'Ping!')

                elif cmd.lower().startswith('ding'):
                    await self.send_message(message.channel, 'Dong!')
                elif cmd.lower().startswith('dong'):
                    await self.send_message(message.channel, 'Ding!')

                elif cmd.lower().startswith('bing'):
                    await self.send_message(message.channel, 'Bong!')
                elif cmd.lower().startswith('bong'):
                    await self.send_message(message.channel, 'Bing!')

                elif cmd.lower().startswith('ting'):
                    await self.send_message(message.channel, 'tong!')
                elif cmd.lower().startswith('tong'):
                    await self.send_message(message.channel, 'ting!')

                elif cmd.lower().startswith('wing'):
                    await self.send_message(message.channel, 'wong!')
                elif cmd.lower().startswith('wong'):
                    await self.send_message(message.channel, 'wing!')

                elif cmd.lower().startswith('test'):
                    await self.send_message(message.channel, 'the git pull works!')

                elif cmd.lower().startswith('lenny'):
                    await self.send_message(message.channel, '( ͡° ͜ʖ ͡°)')

                elif cmd.lower().startswith('imdb'):
                    cmd = cmd.lower()
                    film = str(await imdb.imdb(cmd))
                    title = cmd.replace('imdb ','')
                    await self.send_message(message.channel, 'Sent IMDB Results for "' + title + '" :film_frames: ')
                    await self.send_message(message.author, film)


                elif cmd.lower().startswith('calc ') or cmd.lower().startswith('wa ') or cmd.lower().startswith('eval ') or cmd.lower().startswith('wolfram '):
                    load_msg = await self.send_message(message.channel, "Gathering results for: `"+cmd+"`...")
                    if "calc " in cmd:
                        cmd = cmd.replace("calc ","")
                    elif "wa " in cmd:
                        cmd = cmd.replace("wa ", "")
                    elif "eval " in cmd:
                        cmd = cmd.replace("eval ", "")
                    elif "wolfram " in cmd:
                        cmd = cmd.replace("wolfram ", "")
                    try:
                        res = self.wolfram_client.query(cmd)
                        result = "Wolfram-Alpha Query Result for '`"+cmd+"`'\n```erl\n"+str(next(res.results).text)+"```"
                    except:
                        result = "Couldnt return result from Wolfram-Alpha API. :x:"
                    await self.edit_message(load_msg, "Sent Wolfram-Alpha Query Results via PM :bar_chart:")
                    await self.send_message(message.author, result)



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

                elif cmd.lower().startswith('steamhelp'):
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

                elif cmd.lower().startswith('info'):

                    msg = "```markdown\n" \
                          "NootBot - Private Release (WIP)\n" \
                          "===============================\n\n" \
                          "[Author: ][denBot (Dan)]\n" \
                          "[Joined: ][Jan 12, 2015]\n" \
                          "[Watched:][1 time(s)]\n"\
                          "[Starred:][0 time(s)]\n" \
                          "[Latest: ][First Commit - 10 day(s) ago]\n" \
                          "[Github: ][https://github.com/denBot/NootTechBot]\n\n" \
                          "Visit us at: https://noot.tech/\n" \
                          "-------------------------------" \
                          "```"
                    await self.send_message(message.channel, msg)

                elif cmd.lower().startswith('google '):
                    cmd = cmd[6:]
                    loading = await self.send_message(message.channel, "Searching Google Results... :mag_right: ")
                    NotSafe = False
                    phrase = cmd.split(' ')
                    cmd = cmd.replace(' ','+')
                    req = Request("https://www.google.com/search?q=" + cmd)
                    req.add_header('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
                    response = urlopen(req)
                    soup = bs4.BeautifulSoup(response.read(), "html.parser")
                    title = []
                    desc = []
                    for i in soup.find_all("h3", class_="r"):
                        title.append(i.text)

                    for i in soup.find_all("div", class_="s"):
                        desc.append(i.text)

                    # Removes 'Cached' and 'Similar' hypertext from google results.
                    description = desc[0].replace('Similar', '\n').replace('Cached', '\n')
                    desc_srch = description.lower().split(' ')

                    for item in desc_srch:
                        if item in NSFW:
                            NotSafe = True

                    for item in phrase:
                        if item in NSFW:
                            NotSafe = True

                    if NotSafe == True:
                        await self.edit_message(loading,"Sorry, this search (or its result) was detected as NSFW. We can't link you that... Naughty! :smirk:")
                    else:
                        await asyncio.sleep(1)
                        await self.edit_message(loading, (message.author.mention + ' `'+title[0]+'`\n'+description))

                elif cmd.lower().startswith('translatehelp'):
                    cmd = self.print_commands('content/txt/translate.txt')
                    await self.send_message(message.channel, "Sent Translate commands via PM.")
                    await self.send_message(message.author, cmd)

                elif cmd.lower().startswith('votehelp'):
                    cmd = self.print_commands('content/txt/vote.txt')
                    await self.send_message(message.channel, "Sent Voting commands via PM.")
                    await self.send_message(message.author, cmd)

                elif cmd.lower().startswith('translate '):
                    await self.send_message(message.channel, translator.translate(cmd.lower()))

                elif cmd.lower().startswith('youtube '):
                    loading = await self.send_message(message.channel, "Searching YouTube Results... :mag_right: ")
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
                    await asyncio.sleep(1)
                    if NotSafe == True:
                        await self.edit_message(loading, 'Sorry, the words '+ rejects +' are considered NSFW. Naughty! :smirk:')
                    else:
                        for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                            if len(video['href']) < 25:
                                L.append('https://www.youtube.com' + video['href'])
                        await self.edit_message(loading, message.author.mention + ' `Result for "'+youtube_link+'"` \n'+L[0])


                elif cmd.lower()=='help':
                    help = self.print_commands('content/txt/help.txt')
                    await self.send_message(message.channel, "Sent help commands via PM.")
                    await self.send_message(message.author, help)

                elif cmd.lower()=='music':
                    help = self.print_commands('content/txt/music.txt')
                    await self.send_message(message.channel, "Sent music commands via PM.")
                    await self.send_message(message.author, help)

                elif cmd.lower()=='admin':
                    if message.author.id in admin_ids and (message.author.id == str(settings['BOTSETTINGS']['owner-id']) or admin or Mod or subMod):
                        admin = self.print_commands('content/txt/admin.txt')
                        await self.send_message(message.channel, "Sent Admin commands via PM.")
                        await self.send_message(message.author, admin)
                    else:
                        await self.send_message(message.channel, 'Sorry, only an Admin/Mod can do this.')


                elif cmd.lower()=='coinflip':
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

            elif cmd.lower()=='stream' and (admin or Mod or subMod):
                try:
                    await self.send_message(message.channel, "Come visit MamaMax's Live Stream!")
                    await self.send_message(message.channel, "https://www.youtube.com/c/MamaMaxxy/live")
                except:
                    print('Couldnt post stream link in user channel.')












# Loading Opus Libraries and Initiating bot.
try:
    load_opus_lib()
except:
    print("Error loading Opus Libraries")


try:
    client = NootBot()
    client.run()
except:
    print("Error running bot client.")