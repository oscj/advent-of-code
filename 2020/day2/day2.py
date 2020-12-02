def main():
    f = open('day2.txt', "r")
    psswd_list = [x.replace("\n", "") for x in f]
    print(len(psswd_list))

    print("PART 1:")
    valid_passwds = get_valid_passwords_p1(psswd_list)
    print("Total Number of Valid Passwords : " + str(len(valid_passwds)))
    

    print("\n\nPART 2:")
    valid_passwds = get_valid_passwords_p2(psswd_list)
    print("Total Number of Valid Passwords : " + str(len(valid_passwds)))

# part 1
def get_valid_passwords_p1(psswd_list):
    valid_psswds = []

    for psswd in psswd_list:
        min = int(psswd.split(":")[0].split(" ")[0].split("-")[0])
        max = int(psswd.split(":")[0].split(" ")[0].split("-")[1])
        tartget_char = psswd.split(":")[0].split(" ")[1]
        attempted_psswd = psswd.split(":")[1].replace(" ", "")
        c_count = 0
        for c in attempted_psswd:
            if c == tartget_char:
                c_count += 1
        if c_count >= min and c_count <= max:
            valid_psswds.append(psswd)

    return valid_psswds

# part 2
def get_valid_passwords_p2(psswd_list):
    valid_psswds = []

    for psswd in psswd_list:
        first_index = int(psswd.split(":")[0].split(" ")[0].split("-")[0]) - 1
        last_index = int(psswd.split(":")[0].split(" ")[0].split("-")[1]) - 1
        
        tartget_char = psswd.split(":")[0].split(" ")[1]
        attempted_psswd = psswd.split(":")[1].replace(" ", "")
        
        first_c = attempted_psswd[first_index] 
        second_c =  attempted_psswd[last_index] 
        
        # ~(p ^ q) ^ (p v q)
        if (not (first_c == tartget_char and second_c == tartget_char)) and (first_c == tartget_char or second_c == tartget_char):
            valid_psswds.append(psswd)

    return valid_psswds

if __name__ == '__main__':
    main()