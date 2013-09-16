#pomocna funkcija za kontrolirani ispis u vise redova
def ispis(objekt,br):
    objekt=str(objekt)
    d=len(objekt)
    red=d // br
    ostatak=d%br
    za_ispis=""
    for k in xrange(red):
        za_ispis=za_ispis+objekt[k*br:(k+1)*br]+"\ \n"
    if ostatak==0:
        za_ispis = za_ispis[:-3]
    else:
        za_ispis= za_ispis+objekt[red*br:]
    print za_ispis
