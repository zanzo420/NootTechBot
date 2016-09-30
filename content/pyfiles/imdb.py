import asyncio, async, aiohttp
async def imdb(message):
        film = message.replace('imdb ','')
        film_request = film
        if ' ' in film_request:
            temp = film_request.split(' ')
            film_request = '+'.join(temp)

        imdb_url = 'http://www.omdbapi.com/?t=' + film_request + '&y=&plot=short&r=json'
        aioclient = aiohttp.ClientSession()
        async with aioclient.get(imdb_url) as resp:
                imdb_data = await resp.json()
        aioclient.close()
        msg = film

        if 'Error' in imdb_data:
                return msg + '\n\nSorry, there is no IMDB info available for this film :('

        else:
                return msg + '\n\nIMDB Rating:  ' + imdb_data['imdbRating'] + '\nGenre:  ' + imdb_data[
                        'Genre'] + '\nReleased on:  ' + imdb_data['Released'] + '\n' + 'Description:  ' + imdb_data['Plot'] + '\n'



