def valid_ISBN10(isbn): 
    if len(isbn) != 10: return False
    if isbn[-1].isalpha() and isbn[-1] != "X": return False
    number = 0
    if isbn.isalnum():
        if isbn[:-1].isnumeric():
            for i in range(len(isbn)):  
                if i == 9 and isbn[i] == "X": num_to_pass = 10
                else : num_to_pass = int(isbn[i])
                number += num_to_pass *(i+1)
        else: number = 1


    return number%11 == 0
        

print(valid_ISBN10('XXXXXXXXXX'))

