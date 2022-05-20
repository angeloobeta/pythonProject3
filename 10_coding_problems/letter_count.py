def letter_count(s: str):
    s = s.split();
    dictionary = {}
    for i in s:
        temp = {}
        for j in range(len(i)):
            if i[j] not in temp:
                temp[i[j]] = 1
            else:
                temp[i[j]] += 1
        dictionary[i] = temp
    dictn = sorted(dictionary, key=lambda x: dictionary[x][x])
    print(dictn)
    return dictionary


print(letter_count("My name is ifeanyichukwu malachy what's yours?"))
# print(letter_count("Hello apple pie"))
