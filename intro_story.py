import textwrap

story = '''
Olet yksityinen etsivä viettämässä lomaa parhaiden kaveriesi kanssa. Olette vuokranneet yksityisen lentokoneen, joka matkustaa ympäri Eurooppaa. Loman lopussa matkareitin viimeisessä maassa löydätte ruumiin piilotettuna lentokoneen ruumasta. Puet etsivähattusi takaisin päälle napataksesi ystäväsi murhaajan. Kansainvälinen poliisi ilmoittaa, että sinulla on rajallinen budjetti (500 €) ja matkustamiseen kuluu 50 €. Sinun täytyy saada oikeutta ystävällesi saamalla vastuullinen kaltereiden taakse. Sinun täytyy kerätä vihjeitä rikoksesta ja niiden perusteella tehdä syytöksiä murhaajasta, murha- aseesta sekä maasta, missä murha tapahtui. 

'''

wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
intro_list = wrapper.wrap(text=story)


def getStory():
    return intro_list

