import steamapi
import aiohttp
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import configparser

# Open up settings.ini with a text-editor and enter in your Steam API key and preferred settings then save the file.
settings = configparser.ConfigParser()
settings.read('content/Settings.ini')
key = settings['STEAM']['APIKey'] # Sets steam API key


steamapi.core.APIConnection(api_key=(key))




async def finder(client, cmd, message):
    user = cmd.replace('steam ', '')


    if len(user) == 17 and user.isnumeric() == True:
        try:
            user_url = steamapi.user.SteamUser(userid=user)
        except (steamapi.errors.APIBadCall, IndexError):
            await client.send_message(message.channel, 'User Not Found - ID Incorrect.')
            return
    else:
        try:
            user_url = steamapi.user.SteamUser(userurl=user)
        except steamapi.errors.UserNotFoundError:
            await client.send_message(message.channel, 'User Not Found - Custom URL Incorrect.')
            return



    avatar_data = None
    aioclient = aiohttp.ClientSession()
    async with aioclient.get(user_url.avatar_full) as resp:
        avatar_data = await resp.read()
        with open("temp.png", "wb") as f:
            f.write(avatar_data)
            f.close()
    aioclient.close()

    await client.send_file(message.channel, 'temp.png')
    os.remove('temp.png')

    try:
        steam_level = user_url.level
    except AttributeError:
        await client.send_message(message.channel, ('Name: '+user_url.name+'\nStatus: This profile is private.\nSteam ID: '+str(user_url.steamid)+'\nSteam URL: '+  user_url.profile_url))
        return None


    msg = 'Name: {0}\nSteam Level: {1}\nLast Online: {2}\nSteam ID: {3}\nSteam URL: {4}'
    await client.send_message(message.channel, msg.format(user_url.name, user_url.level, user_url.last_logoff, user_url.steamid, user_url.profile_url))






async def join(client, cmd, message):
    user = cmd.replace('steam ', '')

    if len(user) == 17 and user.isnumeric() == True:
        try:
            user_url = steamapi.user.SteamUser(userid=user)
        except (steamapi.errors.APIBadCall, IndexError):
            await client.send_message(message.channel, 'User Not Found - ID Incorrect.')
            return
    else:
        try:
            user_url = steamapi.user.SteamUser(userurl=user)
        except steamapi.errors.UserNotFoundError:
            await client.send_message(message.channel, 'User Not Found - Custom URL Incorrect.')
            return



    try:
        steam_level = user_url.level
    except AttributeError:
        await client.send_message(message.channel, ('Sorry, "' + user + '" aka ' + user_url.name + 's Steam Profile is currently set to Private.'))
        return

    html = urlopen(str(user_url.profile_url)).read()

    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all('a', {'class': "btn_green_white_innerfade btn_small_thin"}):
        print(a['href'])

        if a['href'] == 'steam://':
            await client.send_message(message.channel, ( user_url.name +' is currently playing: '+str(user_url.currently_playing)+' but is not currently joinable'+'\nWatch: steam://broadcast/watch/'+str(user_url.id)))
            return
        else:
            await client.send_message(message.channel, ( user_url.name +' is currently playing: '+str(user_url.currently_playing)+'\n Join: '+a['href']+'\nWatch: steam://broadcast/watch/'+str(user_url.id)))
            return

    for outer in soup.find_all('div', {'class': "profile_in_game_header"}):
        for item in outer:
            if item == "Currently Online" or item == "Currently Offline":
                await client.send_message(message.channel, ( user_url.name + ' is not currently playing a game on Steam.'))
            else:
                for inner in soup.find_all('div', {'class': "profile_in_game_name"}):
                    print(inner)
                    for other_item in inner:
                        await client.send_message(message.channel, ( user_url.name + ' is currently playing a non-steam game: "'+str(other_item)+'".'+'\nWatch: steam://broadcast/watch/'+str(user_url.id)))
