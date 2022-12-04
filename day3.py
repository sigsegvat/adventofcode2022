def find_char(string):
    length = len(string)
    if length == 0:
        raise Exception()

    half_length = length // 2

    first_half = string[:half_length]
    second_half = string[half_length:]

    common_chars = set(first_half) & set(second_half)

    if not common_chars:
        raise Exception()

    return common_chars.pop()


def map_char_to_priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return 0


with open('day3.txt', 'r') as file1:
    lines = file1.readlines()

sum1=0
for line in lines:
    char = find_char(line.strip())
    prio = map_char_to_priority(char)
    sum1+=prio

print("solution 1",sum1)




groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

priorities = []
for group in groups:
    common_chars = set(group[0].strip()) & set(group[1].strip()) & set(group[2].strip())
    if not common_chars :
        raise Exception()
    else:
        priority = map_char_to_priority(common_chars.pop())

    priorities.append(priority)

print("solution 2",sum(priorities))