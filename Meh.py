def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" kuid ", ", kuid ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" aga ", ", aga ")
    lause = lause.replace(" siis ", ", siis ")
    lause = lause.replace(" vaid ", ", vaid ")
    return lause
    

fail = open("vigane.txt", encoding = "UTF-8")
f = open("parandatud.txt", "w", encoding = "UTF-8")

for lause in fail:
    korras = paranda_komavead(lause)
    f.write(str(korras))

fail.close()
f.close()