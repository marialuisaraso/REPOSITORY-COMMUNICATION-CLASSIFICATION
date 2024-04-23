import re

def extract_and_sum_last_number_1(line):
    pattern1 = r"[-+]?\d*\.\d+|\d+"
    numeros1 = re.findall(pattern1, line)
    
    if numeros1:
        last_number_1 = 0
        last_number_1 = float(numeros1[-1])
        with open('Tools/Index/MIRRORcompounds.txt', 'a') as file2:
            file2.write(str(last_number_1) + "\n")
        return last_number_1
    else:
        return 0.0  
    
def extract_and_sum_last_number_2(line):
    # Expressão regular para encontrar os números
    pattern2 = r"[-+]?\d*\.\d+|\d+"
    numeros2 = re.findall(pattern2, line)
    
    if numeros2:
        last_number_2 = 0
        last_number_2 = float(numeros2[-1])
        with open('Tools/Index/MIRRORcompounds.txt', 'a') as file2:
            file2.write(str(last_number_2) + "\n")
        return last_number_2
    else:
        return 0.0  
    
def extract_and_sum_last_number_3(line):
    pattern3 = r"[-+]?\d*\.\d+|\d+"
    numeros3 = re.findall(pattern3, line)
    
    if numeros3:
        last_number_3 = 0
        last_number_3 = float(numeros3[-1])
        with open('Tools/Index/MIRRORcompounds.txt', 'a') as file2:
            file2.write(str(last_number_3) + "\n")
        return last_number_3
    else:
        return 0.0  

def process_input_1(filename):
    with open(filename, 'r') as file:
        index_score1 = 0
        for line in file:
            last_number_1 = extract_and_sum_last_number_1(line)
            index_score1 += last_number_1
        return index_score1
    
def process_input_2(filename):
    with open(filename, 'r') as file:
        index_score2 = 0
        for line in file:
            last_number_2 = extract_and_sum_last_number_2(line)
            index_score2 += last_number_2
        return index_score2
    
def process_input_3(filename):
    with open(filename, 'r') as file:
        index_score3 = 0
        for line in file:
            last_number_3 = extract_and_sum_last_number_3(line)
            index_score3 += last_number_3
        return index_score3

input_file_1 = "MIRRORissuesVaderOutput.txt"
input_file_2 = "MIRRORcommitsVaderOutput.txt"
input_file_3 = "MIRRORprsVaderOutput.txt"


final_index_score1 = process_input_1(input_file_1)
final_index_score1 = final_index_score1 / 11272
print("\n ISSUES INDEX:", final_index_score1, "\n")
final_index_score2 = process_input_2(input_file_2)
final_index_score2 = final_index_score2 / 7532
print("COMMITS INDEX:", final_index_score2, "\n")
final_index_score3 = process_input_3(input_file_3)
final_index_score3 = final_index_score3 / 5014
print("PRS INDEX:", final_index_score3, "\n")

final_index_score_general = (final_index_score3) + (final_index_score2*3) + (final_index_score1*2) # WEIGHTS: 2 FOR ISSUES, 3 FOR COMMITS, 1 FOR PULL REQUESTS
print("GLOBAL INDEX:", final_index_score_general/6, "\n") # SCORE DIVIDED BY 6 (SUM OF WEIGHTS)- WEIGHTED AVERAGE
