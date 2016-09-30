import discord, youtube_dl, asyncio, configparser

settings = configparser.ConfigParser()
settings.read('Settings.ini')


 # ---------------------------------------------------------------------------
 # This was written by Maware for the ImoOnna Bot
 # https://github.com/PotatoHunters/ImoOnnaBot/
 # It has been modified by Maware for the use of denBot
 # ---------------------------------------------------------------------------

class Player(discord.Client):



    # Create variables when created
    def __init__(self, client, server):
        super().__init__()
        self.voice_client = None
        self.player = None
        self.playlist = []
        self.max_playlist_length = int(settings['PLAYER']['YoutubePlaylistCap'])
        self.player_length = int(settings['PLAYER']['MaxSongLength'])*60
        self.max_song_requests = int(settings['PLAYER']['MaxUserSongRequests'])-1
        self.playlist_cap = int(settings['PLAYER']['BotPlaylistCap'])
        self.client = client
        self.server = server
        self.volume = float(settings['PLAYER']['defaultvol'])

        try:
            self.useav = settings['PLAYER']['useavonv']
        except:
            self.useav = False


        # Skip and text channel to post np
        self.skip = False
        for channel in server.channels:
            if str(settings['BOTSETTINGS']['DefaultChannel']) == channel.name.lower():
                self.text_channel = channel
                break
            else:
                self.text_channel = server.default_channel

        self.get_music_channel()
        self.skip = False
        self.skips_needed = 0
        self.votes = []





    def get_music_channel(self):
        for channel in self.server.channels:
            if channel.type == discord.ChannelType.text:
                #checks if there are text channels with name 'bot' or 'music' or that contains 'bot' or 'music'
                if str(settings['BOTSETTINGS']['DefaultChannel']) == channel.name.lower():
                    self.text_channel = channel
                    break






    async def get_voice_client(self, channel=None, reset=False):

        '''
        Function to make the client to join users voice channel
        Or return the current voice client for the server
        Arguments
        ---------------
        channel: discord.Channel
        reset: bool
        return: discord.VoiceClient or None (if no voice client for that server)
        '''

        # Check if we do not want to join a voice channel
        if reset == False:
            # Check if the bot is connected and return the voice client if it is else return None
            if self.client.is_voice_connected(self.server):
                return self.voice_client
            else:
                return None

        # Disconnect from current voice channel for server if in one
        if self.client.is_voice_connected(self.server):
            await self.voice_client.disconnect()

        # Join users voice channel and set voice client
        voice_client = await self.client.join_voice_channel(channel)
        self.voice_client = voice_client
        return voice_client






    async def disconnect_voice_client(self):
        '''
        Function to disconnect bot from the voice channel it is in and wipe everything clean to bot with the music player
        :return: None
        '''

        #Clear playlist
        self.playlist = []

        # Disconnect Bot from voice channel
        print('Disconnect from voice')
        await self.voice_client.disconnect()

        # Clear everything to nothing
        self.voice_client = None
        self.player = None

    def stop(self):
        self.player.stop()
        self.playlist = []









    async def add_playlist(self, url, message, type='y'):

        if len(self.playlist) > self.playlist_cap:
            await self.client.send_message(message.channel, ":notes: The playlist is at capacity ("+self.playlist_cap+" songs). Please try again later.")
        else:
            if type=='y':
                startpos = 1
                endpos = 2
                if '&index=' in url:
                    isPlaylist = True
                    temp = url.split('&')
                    for i in range(0, (len(temp))):
                        if 'index=' in temp[i]:
                            sstart = temp[i].replace('index=', '')
                            startpos = int(sstart)
                            endpos = startpos + self.max_playlist_length - 1
                            break
                ytdl = youtube_dl.YoutubeDL({'playliststart': startpos, 'playlistend': endpos})
                try:
                    result = ytdl.extract_info(url, download=False)
                    cont = True
                except youtube_dl.utils.DownloadError as e:
                    cont = False
                    if 'Incomplete YouTube ID' in str(e):
                        msg = '{0.author.name} : Not a valid Youtube video'
                        self.client.send_message(message.channel, msg.format(message))


                if cont:
                    user_occurance = 0

                    # Checks if the message author is an admin
                    admin = False
                    for role in message.author.roles:
                        if settings['BOTSETTINGS']['botadmin'] in role.name or "Loser" in role.name or "Admin" in role.name:
                            admin = True

                    if 'entries' in result:
                        queued = 0
                        for i in range(0, len(result['entries'])):
                            # Get video url, title and set requester
                            url = result['entries'][i]['webpage_url']
                            title = result['entries'][i]['title']
                            video_already_present = False
                            user = message.author.mention
                            name = message.author.name
                            id = message.author.id

                            for item in self.playlist:
                                if item['user'] == user:
                                    user_occurance += 1
                                if item['title'] == title:
                                    video_already_present = True

                            if user_occurance > self.max_song_requests and (admin == False):
                                await self.client.send_message(message.channel,
                                                               ":notes: You currently have "+str(self.max_song_requests+1)+" songs in the playlist. Please try again later.")
                            elif video_already_present:
                                await self.client.send_message(message.channel,
                                                               ":notes: A song with the title `"+title+"` is already in this playlist.")
                            else:


                                if '`' in title:
                                    title = title.replace('`', '\'')

                                self.playlist.append({'url': url, 'title': title, 'user': user, 'name': name, 'id': id})
                                print(title + ' Added to queue')
                                queued = queued + 1



                        # Tell user the amount of playlist songs queued
                        msg = 'Queued: `' + str(queued) + ' song(s)`'
                        await self.client.send_message(message.channel, msg.format(message))

                    # Else it is a single video
                    else:
                        user_occurance = 0
                        video_already_present = False
                        url = result['webpage_url']
                        title = result['title']
                        user = message.author.mention
                        name = message.author.name
                        id = message.author.id


                        for item in self.playlist:
                            if item['user'] == user:
                                user_occurance += 1
                            if item['title'] == title:
                                video_already_present = True

                        if user_occurance > self.max_song_requests and (admin == False):
                            await self.client.send_message(message.channel,":notes: You currently have " + str(self.max_song_requests + 1) + " songs in the playlist. Please try again later.")
                        elif video_already_present:
                            await self.client.send_message(message.channel,":notes: A song with the title `" + title + "` is already in this playlist.")
                        else:
                            if '`' in title:
                                title = title.replace('`', '\'')
                            # Add info to playlist
                            self.playlist.append({'url': url, 'title': title, 'user': user, 'name': name, 'id':id})
                            print(title + ' Added to queue')

                            # Tell user the song has been queued
                            msg = 'Added to queue: `' + title + '`'
                            await self.client.send_message(message.channel, msg.format(message))

            # Soundcloud Section
            elif type == 's':
                # Set youtube_dl to use max_playlist_length to set the end of a set
                ytdl = youtube_dl.YoutubeDL({'playlistend': self.max_playlist_length})

                # Get SC song info
                cont = True
                try:
                    result = ytdl.extract_info(url, download=False)
                    cont = True
                # Invalid Link
                except youtube_dl.utils.DownloadError as e:
                    cont = False
                    if 'Unable to download JSON metadata' in str(e):
                        print('Invalid Soundcloud link')
                        msg = '{0.author.mention} : Not a valid Soundcloud song'
                        await self.client.send_message(message.channel, msg.format(message))

                if cont:
                    # If SC set
                    if 'entries' in result:
                        for i in range(0, len(result['entries'])):
                            # Get song url, title and set requester
                            url = result['entries'][i]['webpage_url']
                            title = result['entries'][i]['title']
                            user = message.author.mention
                            name = message.author.name
                            id = message.author.id
                            # Make sure the video title cannot break code box in message
                            if '`' in title:
                                title = title.replace('`', '\'')
                            # Add info to playlist
                            self.playlist.append({'url': url, 'title': title, 'user': user, 'name': name, 'id': id})
                            print(title + ' Added to queue')

                        # Tell the user how many songs have been queued
                        msg = 'Queued: `' + str(len(result['entries'])) + ' songs`'
                        await self.clientlient.send_message(message.channel, msg.format(message))
                        # Else it is a single song
                    else:
                        # Get song url, title and set requester
                        url = result['webpage_url']
                        title = result['title']
                        user = message.author.mention
                        name = message.author.name
                        id = message.author.id
                        # Make sure the video title cannot break code box in message
                        if '`' in title:
                            title = title.replace('`', '\'')
                        # Add info to playlist
                        self.playlist.append({'url': url, 'title': title, 'user': user, 'name': name, 'id': id})
                        print(title + ' Added to queue')

                        # Tell the user the song has been queued
                        msg = 'Queued: `' + title + '`'
                        await self.client.send_message(message.channel, msg.format(message))
                        # Soundcloud Section

            elif type == 'b':
                ytdl = youtube_dl.YoutubeDL({'playlistend': self.max_playlist_length})
                try:
                    result = ytdl.extract_info(url, download=False)
                    cont = True
                except youtube_dl.utils.DownloadError as e:
                    cont = False
                    if 'Unable to download JSON metadata' in str(e):
                        print('Invalid Bandcamp link')
                        msg = '{0.author.mention} : Not a valid Bandcamp song'
                        await self.client.send_message(message.channel, msg.format(message))
                if cont == True:
                    url = result['webpage_url']
                    title = result['title']
                    user = message.author.mention
                    name = message.author.name
                    id = message.author.id
                    if '`' in title:
                        title = title.replace('`', '\'')
                    self.playlist.append({'url': url, 'title': title, 'user': user, 'name': name, 'id': id})
                    print(title + ' Added to queue')
                    msg = 'Queued: `' + title + '`'
                    await self.client.send_message(message.channel, msg.format(message))



    async def get_player(self, channel, new=False, url=''):

        # Youtube-dl function for downloading content.

        # If there is no player for server (Has to be new)
        if self.player is None:
            if new:
                # Set options for ffmpeg
                kwargs = {'options': '-af "volume='+str(self.volume)+'"', 'use_avconv': self.useav}
                # Get voice client
                voice = await self.get_voice_client(channel)
                # Create player
                player = await voice.create_ytdl_player(url, **kwargs)
                self.player = player
                return player
        else:
            # If making a new player
            if new:
                # Set options for ffmpeg
                kwargs = {'options': '-af "volume='+str(self.volume)+'"', 'use_avconv': self.useav}
                # Get voice client
                voice = await self.get_voice_client(channel)
                # Create player
                player = await voice.create_ytdl_player(url, **kwargs)
                self.player = player
                return player
            # Return the current player
            else:
                return self.player











    async def audio_player(self, new=False):

        loop = True
        while loop:

            # If playlist empty, stop player
            if len(self.playlist) == 0:
                player = await self.get_player(self.client.voice_client_in(self.server).channel)
                if player != None:
                    player.stop()
                loop = False
                break

            else:
                # Stop the player if the player is not new
                if new == False:
                    player = await self.get_player(self.client.voice_client_in(self.server).channel)
                    player.stop()

                text_channel = self.text_channel

                Cont = False
                try:
                    # Load audio
                    player = await self.get_player(self.client.voice_client_in(self.server).channel, new=True,url=self.playlist[0]['url'])
                    Cont = True
                except youtube_dl.utils.ExtractorError:
                    # Display error message is blocked
                    discord.Client.console_print('Audio blocked in Country')
                    temp_msg = "Audio blocked in Bot's Country Sorry :c"
                    await self.client.send_message(text_channel, temp_msg)
                    Cont = False
                except youtube_dl.utils.DownloadError:
                    # Display error message is blocked
                    discord.Client.console_print('Audio blocked in Country')
                    temp_msg = "Audio blocked in Bot's Country Sorry :c"
                    temp = False
                    await self.client.send_message(text_channel, temp_msg)
                    Cont = False

                if Cont:

                    if "bandcamp.com" not in self.playlist[0]['url']:
                        mins = int(player.duration / 60)
                        secs = player.duration % 60

                    title = self.playlist[0]['title']
                    currently_playing = title
                    await self.client.change_status(discord.Game(name=currently_playing))

                    if "bandcamp.com" in self.playlist[0]['url']:
                        temp_msg = 'Now Playing: `' + title + ' [Bandcamp]` \nRequested by ' + self.playlist[0]['user']

                    elif secs < 10:
                        temp_msg = 'Now Playing: `' + title + ' (' + str(mins) + ':0' + str(
                            secs) + 's)` \nRequested by ' + self.playlist[0]['user']
                    else:
                        temp_msg = 'Now Playing: `' + title + ' (' + str(mins) + ':' + str(
                            secs) + 's)` \nRequested by ' + self.playlist[0]['user']






                    # Send the current playing title + duration and who requested it and start audio



                    msg = 'Playing: ' + title + ' [' + player.url + ']'
                    print(msg)
                    player.start()

                    try:
                        sent_message = await self.client.send_message(text_channel, temp_msg)
                    except:
                        print("Error 403 or 404.")
                    # Skip (if active/current voters that have voted to skip)
                    self.skip = False
                    self.skips_needed = 0
                    self.votes = []


                    while self.player.is_playing() and not self.skip:
                        await asyncio.sleep(1)


                # Clear playlist of that song
                if self.playlist:
                    del self.playlist[0]
                loop = True
                new = False
                try:
                    await self.client.delete_message(sent_message)
                except:
                    continue
                await self.client.change_status(discord.Game(name=settings['BOTSETTINGS']['currentgame']))





    async def skip_audio(self):
        print('Audio Skipped')
        self.skip = True
        await asyncio.sleep(1)
        self.skip = False





    async def remove_song(self,message,song_int,admin=False):
        song_int = int(song_int)
        if len(self.playlist)==0:
            await discord.Client.send_message(self.client, message.channel, "Playlist is empty, there are no songs to remove.")
        elif song_int==0:
            await discord.Client.send_message(self.client, message.channel, "Cannot remove the currently playng song. Try skipping it instead.")
        else:
            if admin == True or message.author.id == self.playlist[song_int]['id']:
                try:
                    await discord.Client.send_message(self.client, message.channel, ("`"+self.playlist[song_int]['title'] + "` has been removed from the playlist by " + message.author.mention))
                    del self.playlist[song_int]
                except:
                    await discord.Client.send_message(self.client,message.channel,("`"+self.playlist[song_int]['title']+"` could not be removed from the playlist."))
            else:
                await discord.Client.send_message(self.client, message.channel,"Only an admin or the submitter can remove a song from the playlist.")






    async def get_queue(self, message):


        if len(self.playlist) < 2:
            msg = "`There's nothing in the playlist right now :( Feel free to add something!`"
        else:
            if len(self.playlist) > 26:
                prange = 26
            else:
                prange = len(self.playlist)
            title = 'Songs in the '+message.server.name+' Playlist:'
            breaker = ""
            for letter in title:
                breaker+="-"
            msg = '```markdown\n'+title+'\n'+breaker+'\n\n# Currently Playing: '+self.playlist[0]['title']+': Requested by '+self.playlist[0]['name']+"\n\n"

            for i in range(1, prange):
                msg = msg + "[ "+str(i) + '. ' + self.playlist[i]['title'].replace("[","(").replace("]",")") + ': ][ Requested by ' + self.playlist[i]['name'] + ' ]\n'
            msg = msg + '```'

        await discord.Client.send_message(self.client, message.author, msg.format(message))








    # Set player volume
    async def change_volume(self, percentage, message_channel):
        if str(percentage) == "over 9,000" or str(percentage) == "over 9000":
            self.volume = 250 / 100
            if self.player is not None:
                self.player.volume = self.volume
            await self.client.send_message(message_channel,':notes: HOLY SHIT, Over 9,000!')

        elif int(percentage) < 15 or int(percentage) > 150:
            # Send user error message for invalid percentage
            await self.client.send_message(message_channel,':anger: Volume is done by percentage between 15%  and 150%, Please pick a vaild percentage')
        else:
            # Change percentage to a valid number for ffmpeg or avconv
            self.volume = int(percentage) / 100
            # Make sure there is a player to change the volume for
            if self.player is not None:
                self.player.volume = self.volume
            # Send volume has been changed message
            await self.client.send_message(message_channel,':notes: Volume has been changed to: **{0}%**'.format(percentage))












    # Check if user is admin a force skips or vote to skip if not admin
    async def do_skip(self, message, admin=False):
        args = ""
        if len(message.content) > 5:
            if message.content[5] == " ":
                args = message.content[6:]
            else:
                args = message.content[5:]

        # If user has the manage server permisson
        if admin and args == "-f":
            # If there is a player and it is playing
            if self.player != None and self.player.is_playing():
                # Skip
                self.skip = True
                await asyncio.sleep(1)
                self.skip = False
                await self.client.send_message(message.channel,
                                               ':notes: Song has been forced skipped by **{0}**'.format(
                                                   message.author.display_name))
                # Reset skip
                self.skips_needed = 0
                self.votes = []
            else:
                # Send message saying there is nothing to skip
                await self.client.send_message(message.channel,
                                               '{0} - There is nothing playing to be skipped'.format(
                                                   message.author.mention))
        else:
            # If there is a player and it is playing
            if self.player != None and self.player.is_playing():
                # Vote Skip
                # If already voted
                if message.author.id in self.votes:
                    await self.client.send_message(message.channel, ':x: You have already voted to skip')
                else:
                    # First vote skip
                    if not self.votes:
                        numofmembers = len(self.voice_client.channel.voice_members)
                        self.skips_needed = int(numofmembers * 0.6)

                    # Add users to voted list
                    self.votes.append(message.author.id)

                    # Check if max has been reached
                    if len(self.votes) == self.skips_needed:
                        await self.client.send_message(message.channel,
                                                       '**{0}** has voted to skip.\nThe vote skip has passed.'.format(
                                                           message.author.display_name))
                        # Skip
                        self.skip = True
                        await asyncio.sleep(1)
                        self.skip = False
                        await self.client.send_message(message.channel, ':notes: Song has been skipped')
                        # Reset skip
                        self.skips_needed = 0
                        self.votes = []
                    else:
                        # Say remaning votes left
                        votes_needed_left = self.skips_needed - len(self.votes)
                        await self.client.send_message(message.channel,
                                                       '**{0}** has voted to skip.\n**{1}** more votes needed to skip.'.format(
                                                           message.author.display_name, votes_needed_left))
            else:
                # Send message saying there is nothing to skip
                await self.client.send_message(message.channel,
                                               '{0} - There is nothing playing to be skipped'.format(
                                                   message.author.mention))


    async def current_song(self,message):
        if len(self.playlist)==0:
            await discord.Client.send_message(self.client, message.channel, "There is currently no song playing.")
        else:
            current_song = self.playlist[0]['title']
            requested_by = self.playlist[0]['name']

            if "bandcamp" in str(self.playlist[0]['url']):
                await discord.Client.send_message(self.client, message.channel,message.author.mention+"\nCurrently playing: `"+current_song+" [Bandcamp]`\nURL: `"+self.playlist[0]['url']+"`\nRequested by: `" + requested_by+"`")
            else:
                mins = int(self.player.duration / 60)
                secs = self.player.duration % 60
                await discord.Client.send_message(self.client, message.channel,message.author.mention+"\nCurrently playing: `"+current_song+" ("+str(mins)+":"+str(secs)+")`\nURL: `"+self.playlist[0]['url']+"`\nRequested by: `" + requested_by+"`")

