def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" kuid ", ", kuid ")
    lause = lause.replace(" et ", ", et ")
    print(lause)
    
paranda_komavead("Mul on igav sest päev on hall.")
paranda_komavead("Võimalik kuid ma ei tea...")
paranda_komavead("Pean ettevalmistuma et seda teha.")
paranda_komavead("Tuli välja et see ei olegi tõsi.")