import csv

def helper(word,female_first_names,male_first_names,special_names,file):
    listOfWords = word.split(' AND ')
    #print(listOfWords)
    first = listOfWords[0].strip()
    second = listOfWords[1].strip()
    first_part = first.split(' ')
    second_part = second.split(' ')
    if len(first_part) == 1 and len(second_part) == 2:
        first_part.append(second_part[-1])
    elif len(first_part) == 1 and len(second_part) == 3:
        if second_part[0] in special_names:
            first_part.append(second_part[-1])
        elif (second_part[0] in male_first_names and second_part[1] in male_first_names) or (second_part[0] in female_first_names and second_part[1] in female_first_names):
            first_part.append(second_part[-1])
        else:
            first_part.append(second_part[-2])
            first_part.append(second_part[-1])
    elif len(first_part) == 1 and len(second_part) > 3:
        first_part.append(second_part[-2])
        first_part.append(second_part[-1])


    elif (len(first_part) == 2 and len(second_part) == 2):
        if first_part[0] in male_first_names and first_part[1] not in male_first_names:
            pass
        elif first_part[0] in female_first_names and first_part[1] not in female_first_names:
            pass
        elif (second_part[0] in male_first_names and second_part[1] in male_first_names) or (second_part[0] in female_first_names and second_part[1] in female_first_names):
            first_part.append(second_part[-1]) # previously was pass
        else:
            first_part.append(second_part[-1])
    elif (len(first_part)==2 and len(second_part)==3):
        if second_part[0] in special_names:
            first_part.append(second_part[-1])
        elif (second_part[0] in male_first_names and second_part[1] in male_first_names) or (second_part[0] in female_first_names and second_part[1] in female_first_names):
            first_part.append(second_part[-1])
        else:
            first_part.append(second_part[-2])
            first_part.append(second_part[-1])


    elif (len(first_part) == 2 and len(second_part) > 3):
        #first_part.append(second_part[-2])
        if second_part[0] in special_names:
            first_part.append(second_part[-1])
        else:
            first_part.append(second_part[-2])
            first_part.append(second_part[-1])


    file.write(" ".join(first_part))
    file.write("\n")


with open('dist.female.first.txt','r') as f:
    female_first_names = []
    lines = f.readlines()
    for line in lines:
        female_first_names.append(line.split()[0])
    # print(female_first_names)

with open('dist.male.first.txt','r') as f1:
    male_first_names = []
    lines = f1.readlines()
    for line in lines:
        male_first_names.append(line.split()[0])

with open('dev-test.csv') as csv_file:
    special_names = ['PROFESSOR','DOCTOR','REVEREND','MAJOR','COLONEL']
    file = open('output.txt', 'w+')
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        helper(row[0],female_first_names,male_first_names,special_names,file)




