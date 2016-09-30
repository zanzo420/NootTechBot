# NootTechBot


# Installation:

1. Requires Python 3.5+

2. CD into a memorable directory on your computer (such as desktop or documents), Run : "pip install --upgrade" and then "pip install git+https://github.com/denBot/denBot-debian" in your command prompt (without quotations).

2. Once installed, CD into the denBot folder which you have cloned (which can be found in the area you cloned the githup repo at) and run the following : "pip install requirements.txt".

3. After all requirements have been installed, be sure to install ffmpeg (and/or libav-tools if you are on linux)

4. open up Settings.ini located in the content folder and add in all of the API keys you will require:
- Steam API Key (for steam functionality)
- Imgur API Key and Secret
- Merriam Webster Dictionary API
- Discord Bot Token (REQUIRED)
- Bot @<ID> (Used by cleverbot)
- Your prefered command prefix (! default)
- Other bot settings.

# Installing on debian/linux servers:
To install libav-tools: run "sudo apt-get install libav-tools" in your command prompt.
To install ffmpeg, install libav-tools first and then "sudo apt-get install ffmpeg"

Depending on your OS (such as Debian), ffmpeg may not install.


If you are unable to get this bot working with ffmpeg, open up players.py and search for:
          kwargs = {'options': '-af "volume=0.3"', 'use_avconv': False}

Set 'use_avconv': True and save the file. This will use libav-tools instead of ffmpeg for your music bot.

