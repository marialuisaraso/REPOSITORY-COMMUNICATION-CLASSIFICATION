from sentistrength import PySentiStr

senti = PySentiStr()
senti.setSentiStrengthPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentiStrength_Data') 
senti.setSentiStrengthLanguageFolderPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentStrength_Data')
result = senti.getSentiment('hi')
print(result)

