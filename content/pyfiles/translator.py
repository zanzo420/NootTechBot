import goslate

iso_codes = {'albanian':'SQ', 'arabic':'AR', 'armenian':'HY', 'bulgarian':'BG', 'catalan':'CA', 'czech':'CD', 'chinese':'ZH', 'croatian':'HR',
             'danish':'DA', 'dutch':'NL', 'english':'EN', 'spanish':'ES', 'finnish':'FI', 'french':'FR', 'greek':'EL', 'georgian':'KA',
             'german':'DE', 'hebrew':'HE', 'hindi':'HI', 'hungarian':'HU','irish':'GA', 'indonesian':'ID', 'italian':'IT', 'icelandic':'IS',
             'japanese':'JA', 'korean':'KO', 'latvian':'LV', 'lithuanian':'LT', 'maltese':'MT', 'mongolian':'MN', 'norwegian':'NN', 'persian':'FA',
             'polish':'PL','portuguese':'PT','romanian':'RO','russian':'RU','slovak':'sk','slovenian':'SL', 'somali':'SO', 'serbian':'SR', 'swedish':'SV',
             'thai':'TH', 'turkish':'TR','ukrainian':'UK','vietnamese':'VI','welsh':'CY'}



def translate(message):
    gs = goslate.Goslate()
    message = message.replace('translate ', '').split(" ", 1)
    language = str(message[0])
    sentence = str(message[1])
    for k in iso_codes.keys():
        if k in language:
            language = language.replace(k, iso_codes[k]).lower()

    try:
        result = gs.translate(sentence,language)
    except:
        result = "Goslate server is returning Error 503 :("

    return result
