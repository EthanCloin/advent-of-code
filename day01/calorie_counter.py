
def heaviest_elf():
    with open('/Users/ethancloin/Developer/advent-of-code/day01/input.txt', 'r') as f:
        elf_calories = cur_max = 0
        for line in f.readlines():
            if line == '\n':
                # we know it's a new elf
                # stop summing and check against maximum
                cur_max = max(cur_max, elf_calories)
                elf_calories = 0
            else:
                item_calories = int(line.split('\n')[0])
                elf_calories += item_calories
    return cur_max

def top_three_heaviest_elves():
    # third <= second <= first
    first = second = third = 0

    with open('/Users/ethancloin/Developer/advent-of-code/day01/input.txt', 'r') as f:
        elf_calories = 0
        for line in f.readlines():
            if line == '\n':
                # smaller than third largest
                if elf_calories <= third:
                    pass

                # smaller than second largest
                elif elf_calories <= second:
                    # replace third and proper reset
                    third = elf_calories

                # smaller than largest
                elif elf_calories <= first:
                    third = second
                    second = elf_calories

                # new largest
                else: 
                    third = second
                    second = first
                    first = elf_calories
                elf_calories = 0
            else:
                elf_calories += int(line.split('\n')[0])
        print(f"1st: {first} -- 2nd: {second} -- 3rd: {third}")
        return first + second + third

print(top_three_heaviest_elves())


