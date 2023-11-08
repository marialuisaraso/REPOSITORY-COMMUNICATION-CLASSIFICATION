from sentistrength import PySentiStr

senti = PySentiStr()
senti.setSentiStrengthPath('C:\Users\Teste\Downloads\TCC-APLICACAO\SentiStrength\SentStrength_Data\SentStrength_Data_Sept2011\SentiStrength2.3Free.exe') 
senti.setSentiStrengthLanguageFolderPath('C:\Users\Teste\Downloads\TCC-APLICACAO\SentiStrength\SentStrength_Data')
str_arr = ['What a lovely day', 'What a bad day']
result = senti.getSentiment(str_arr, score='scale')
print(result)