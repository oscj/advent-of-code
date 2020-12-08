def main():
    f = open('day4.txt', 'r')
    all_passports = [l.replace("\n", " ") for l in f.read().split("\n\n")]  
    
    # Part 1
    valid_passports = validate_passports(all_passports)
    print("(Part 1) Number of Valid Passports: {}".format(len(valid_passports)))
    
    # Part 2
    valid_passports = validate_passports_p2(all_passports)
    for p in valid_passports:
        print(p)
        print()
    print("(Part 2) Number of Valid Passports: {}".format(len(valid_passports)))

############################################# Part 1
def validate_passports(passport_list):
    '''
        Fields:
        - byr
        - iyr
        - eyr
        - hgt
        - hcl
        - ecl
        - pid
        - cid (optional)
    '''
    valid_passports = []

    for passport in passport_list:
        present_fields = [ entry[0] for entry in (data.split(":") for data in passport.split(" "))]
        if(validate_fields(present_fields)):
            valid_passports.append(passport)

    return valid_passports

def validate_fields(fields):
    return ('byr' in fields and 'iyr' in fields and 'eyr' in fields and 'hgt' in fields and 'hcl' in fields and 'ecl' in fields and 'pid' in fields)


############################################# Part 2
def validate_passports_p2(passport_list):
    valid_passports = []

    for passport in passport_list:
         # check if required fields exist and act accordingly
         present_fields = [ entry[0] for entry in (data.split(":") for data in passport.split(" "))]
         if not validate_fields(present_fields):
             continue
         else:
            # validate data if all fields present
            present_fields_and_values = [ [entry[0], entry[1]] for entry in (data.split(":") for data in passport.split(" "))]
            field_value_dict = {}
            for pairs in present_fields_and_values:
                field_value_dict[pairs[0]] = pairs[1]
            print(field_value_dict)
            is_valid = validate_field_data(field_value_dict)
            if(is_valid):
                valid_passports.append(passport)

    return valid_passports

def validate_field_data(field_value_dict):
    '''
    - byr (Birth Year) - four digits; at least 1920 and at most 2002.
    - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    - hgt (Height) - a number followed by either cm or in:
    - If cm, the number must be at least 150 and at most 193.
    - If in, the number must be at least 59 and at most 76.
    - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    - pid (Passport ID) - a nine-digit number, including leading zeroes.
    - cid (Country ID) - ignored, missing or not.
    '''

    try:
        byr = int(field_value_dict['byr']) >= 1920 and int(field_value_dict['byr']) <= 2002
        iyr = int(field_value_dict['iyr']) >= 2010 and int(field_value_dict['iyr']) <= 2020
        eyr = int(field_value_dict['eyr']) >= 2020 and int(field_value_dict['eyr']) <= 2030

        height_val = int(field_value_dict['hgt'][0:-2])
        height_unit = field_value_dict['hgt'][-2:-1]
        hgt = False
        if height_unit == 'c':
            hgt = height_val >= 150 and height_val <= 193
        elif height_unit == 'i':
            hgt = height_val >= 59 and height_val <= 76
        
        hcl = True
        hair = field_value_dict['hcl']
        if(hair[0] == '#' and len(hair[1::]) == 6):
           for c in hair[1::]:
               if not (c.isdigit() or c in 'abcdef'):
                   return False

        ecl = field_value_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        pid = True
        passport_id = field_value_dict['pid']
        if(len(passport_id) == 9):
            for c in passport_id:
                if not c.isdigit():
                    return False
        else:
            return False 

        return byr and iyr and eyr and hgt and hcl and ecl and pid
    except Exception as e:
        return False
            

if __name__ == '__main__':
    main()
