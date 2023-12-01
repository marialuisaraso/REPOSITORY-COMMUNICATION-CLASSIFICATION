from sentistrength import PySentiStr

senti = PySentiStr()
senti.setSentiStrengthPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentStrength_Data') 
senti.setSentiStrengthLanguageFolderPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentStrength_Data')
str_arr = ['What a lovely day', 'What a bad day']
result = senti.getSentiment(str_arr, score='scale')
print(result)