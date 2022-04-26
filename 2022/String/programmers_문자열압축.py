string = input()



def solution(s):

    n = 1
    answer = len(s)

    while n <= len(s)//2:
        result = []
        cnt = 1
        for i in range(0, len(s), n):
            tmp = s[i:i + n]
            if i == 0:
                result.append(tmp)
            else:
                last = result[-1]
                if len(last) > n:
                    cnt = int(last[:len(last)-n])
                    last = last[len(last)-n:]

                if last == tmp:
                    cnt += 1
                    result[-1] = str(cnt) + last

                else:
                    cnt = 1
                    result.append(tmp)
        print(result)
        total = 0
        for word in result:
            total += len(word)

        if answer > total:
            answer = total

        n += 1

    return answer

print(solution(string))