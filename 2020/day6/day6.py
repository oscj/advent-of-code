def main():
    f = open('day6.txt', 'r')
    input = f.read()

    # get forms by group in 2 d array
    groups = [i.replace("\n" , " ").split(" ") for i in input.split("\n\n")]
    yes_counts = []
    for g in groups:
        yes_counts.append(get_yes_count_p1(g))
    
    print("(Part 1) Sum of yes counts: {}".format(sum(yes_counts)))

    yes_counts = []
    for g in groups:
        yes_counts.append(get_yes_count_p2(g))
    
    print("(Part 2) Sum of yes counts: {}".format(sum(yes_counts)))


def get_yes_count_p1(group):
    answered = {}
    for form in group:
        for q in form:
            if q not in answered:
                answered[q] = q
    return len(answered)

def get_yes_count_p2(group):
    answered = {}
    for form in group:
        for  q in form:
            if q not in answered:
                answered[q] = 1
            else:
                answered[q] += 1
    total = 0
    for key in answered:
        if  answered.get(key) == len(group):
            total += 1
    
    return total


if __name__ == '__main__':
    main()