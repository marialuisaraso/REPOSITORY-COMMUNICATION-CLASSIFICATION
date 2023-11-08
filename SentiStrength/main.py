from sentistrength import PySentiStr

senti = PySentiStr()
senti.setSentiStrengthPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentiStrength2.3Free.exe') # Note: Provide absolute path instead of relative path
senti.setSentiStrengthLanguageFolderPath('/Users/marialuisatomichraso/Desktop/TCC-PROJETO/SentiStrength/SentStrength_Data') # Note: Provide absolute path instead of relative path
str_arr = ['What a lovely day', 'What a bad day']
result = senti.getSentiment(str_arr, score='scale')
print(result)