'''
hash table(dictionary)
와
replace
'''
input_str = input()


def solution(s):
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for key, value in num_dict.items():
        if key in s:
            s = s.replace(key, value)

    answer = int(s)
    return answer

print(solution(input_str))