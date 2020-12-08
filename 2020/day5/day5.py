import math


def main():
    f = open('day5.txt', 'r')
    seats = [l.replace("\n", "") for l in f]

    seat_ids = []

    # Part 1
    for seat in seats:
        row = get_row(seat)
        col = get_col(seat)
        seat_ids.append(get_seat_id(row, col))

    seat_ids.sort()
    print("Greatest Seat ID: {}".format(seat_ids[len(seat_ids) - 1]))

    # Part 2
    # find two seat IDs that difference is 2 AND that the ID inbetween them does NOT exist
    print ("Missing ID: {}".format(find_missing_id(seat_ids)))

def find_missing_id(seat_ids):
    cached = {}

    for id in seat_ids:
        # Look for Ids that have a difference of -2 and that id in between does not exist
        if -2 + id in cached and not id + 1 in seat_ids:
            return id + 1
        else:
            cached[id] = id


def get_row(boarding_pass):
    low, high = 0, 127

    for c in boarding_pass[0:6]:
        if c == 'F':
            high = low + int((high - low) / 2)
        elif c == 'B':
            low = low + math.ceil((high - low) / 2)

    row = high
    if boarding_pass[6] == 'F':
        row = low
    return row


def get_col(boarding_pass):
    low, high = 0, 7

    for c in boarding_pass[7::]:
        if c == 'R':
            low = low + math.ceil((high - low) / 2)
        elif c == 'L':
            high = low + int ((high - low ) / 2)

   
    if boarding_pass[-1] == 'L':
        return low

    return high

def get_seat_id(row, col):
    return ((row * 8) + col)

if __name__ == '__main__':
    main()
