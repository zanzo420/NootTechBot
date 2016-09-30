from urllib.request import urlopen
import bs4
import configparser

settings = configparser.ConfigParser()
settings.read('Settings.ini')
key = settings['MERRIAM-WEBSTER-DICT']['APIToken'] # Sets steam API key

MWKey = '65dd7533-0e1e-44ea-8c40-e21d300f2c50'
# Type of dictionary (depends on API)

def get_xml_definition(word):
    MWKey = '65dd7533-0e1e-44ea-8c40-e21d300f2c50'
    ref = 'collegiate'
    uri = "http://www.dictionaryapi.com/api/v1/references/"+ref+"/xml/"+word+"?key="+MWKey
    file = urlopen(uri)
    data = file.read()
    file.close()
    all_years = []
    xml_soup = bs4.BeautifulSoup(data,'xml')
    try:
        for item in xml_soup.find_all('entry'):

            for item2 in item.find_all('def'):

                new_list = []

                date = str(item2.find_all('date')).replace('<date>','').replace('</date>','').replace('[','(').replace(']',')')

                # If there is no date, don't return (), else return ordinary date of word definition.
                if date == '()':
                    header = (word[0].capitalize() + word[1:]+':')
                else:
                    header = (word[0].capitalize()+word[1:]+' *'+date+':'+"*")

                new_list.append(header)


                defintiions = str(item2.find_all('dt')).replace('<dt>', '').replace('[','').replace(']','').replace(':','')

                # Splits each definition into a list at the </dt> tag.
                defintiions = defintiions.split('</dt>, ')




                i = 0
                while i < len(defintiions):
                    # Removes / Replaces any un-needed <xml> code
                    defintiions[i] = (defintiions[i].replace('<it>','*').replace('</it>', '*').replace('**','').replace('<fw>', '**').replace('</fw>', '*').replace('**', '').replace('<vi>', '').replace('</vi>', '').replace('</dt>', '').replace('<sx>','').replace('</sx>','').replace('<un>','').replace('</un>','').replace('<aq>','').replace('</aq>',''))
                    individual_definition = (str(i+1)+": "+defintiions[i][0].capitalize()+defintiions[i][1:]+'.')
                    new_list.append(individual_definition)
                    i += 1
            all_years.append(new_list)

        #all_years has all the years
        string = ''
        #for item in all_years[-2]:
        #print(item)
        if len(all_years) > 2:
            for item in all_years[-2]:
                string = string + item + '\n'
            string = string + '\n'
            for item in all_years[-1]:
                string = string + item + '\n'
        else:
            for item in all_years[-1]:
                string = string + item + '\n'


        return 'The definition of "'+word+'" :mag_right:\n'+string
    except:
        return "Sorry, the Merriam-Websters API couldn't define that."