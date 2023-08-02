def encryption(message,shift_number):
    alphapet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    code =''
    for i in message:
        position = 0
        for j in alphapet:
            if i != j:
                position +=1
            else:
                break
        new_position = position +shift_number%26
        if new_position < 26:
            for h in alphapet:
                if i not in alphapet:
                    code+=i
                    break
                if h == alphapet[new_position]:
                    code+=alphapet[new_position]
                    break
        else:
            Range  = new_position - 26
            for h in alphapet:
                if i not in alphapet:
                    code+=i
                    break
                if h == alphapet[Range]:
                    code+=alphapet[Range]
                    break

    print("here' the encoded result: " + code)





