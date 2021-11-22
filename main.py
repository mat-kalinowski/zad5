import numpy

klasa1h = {
    'Hipolit Hipopotamowicz': {
        'jezyk polski': [3,3,4],
        'matematyka': [1,2,1,3,1],
        'plastyka': [1,1,1,1,1],
        'przyrka': [1,1,1,1,1]
    },
    'Julia Kramarz': {
        'plastyka': [1],
        'matematyka': [1,1,1,1,2],
        'polski': [1,2,1,1,3,1,1,1]
    },
    'Zuzia Kramarz': {
        'plastyka': [6],
        'matematyka': [5,6,5,6,5],
        'polski': [5,5,5,5,6]
    }
}

def zagrozenie(klasa):
    zagrozeni = {}
    for uczen, przedmioty in klasa.items():
        zagrozeni[uczen] = []
        for przedmiot, oceny in przedmioty.items():
            if numpy.mean(oceny) < 2.0:
                zagrozeni[uczen].append(przedmiot)

    return zagrozeni


def procent_zagrozonych(klasa):
    zagrozeni = zagrozenie(klasa)
    l_zagrozeni = 0
    for uczen, przedmioty in zagrozeni.items():
        # lista nie jest pusta - uczen nie jest zagrozony z przynajmniej jednego przedmiotu
        if przedmioty:
            l_zagrozeni += 1

    return 100 * float(l_zagrozeni)/float(len(zagrozeni))

def osly_dardanelskie(klasa):
    zagrozeni = zagrozenie(klasa)
    # tworzymy liste zawierajaca uczniow i liczbe przedmiotow z ktorej sa zagrozeni
    # np. zagrozeni_lb = [('Hipolit Hipopotamowicz', 2), ('Julia Kramarz', 3), ('Zuzia Kramarz', 0)]
    zagrozeni_lb = [(uczen, len(przedmioty)) for (uczen, przedmioty) in zagrozeni.items()]
    zagrozenia_max = max([zagrozenia_lb for (uczen, zagrozenia_lb) in zagrozeni_lb])
    
    return [uczen for (uczen, zagrozenia_lb) in zagrozeni_lb if zagrozenia_lb == zagrozenia_max]


if __name__ == "__main__":
    zagrozeni = zagrozenie(klasa1h)
    print(zagrozeni)
    procent = procent_zagrozonych(klasa1h)
    print(procent)
    osly = osly_dardanelskie(klasa1h)
    print(osly)
