# ### **문제 설명**

# 자연수 수열이 주어질 때, 수열에서 같은 값이 연속해서 나오는 개수를 순서대로 나열하는 과정을 반복하려 합니다.

# 예를 들어 수열이 [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]일 때, 같은 값이 연속해서 나오는 개수를 순서대로 나열하면 [2, 2, 2, 1, 1, 3, 3]이 됩니다. 새로 구한 수열에서 다시 같은 값이 연속해서 나오는 개수를 순서대로 나열하면 [3, 2, 2]가 됩니다. 마찬가지 작업을 계속 반복하면 수열은 다음과 같이 변합니다.

# [3, 2, 2] → [1, 2] → [1, 1] → [2] → [1] → [1] → [1] ...

# 이와 같이 처음 주어진 수열에 같은 값이 연속해서 나오는 개수를 순서대로 나열하는 과정을 계속해서 수행하면 마지막에는 [1]이 무한히 반복됩니다.

# 초기 수열이 담긴 배열 arr가 매개변수로 주어질 때, 최초로 [1]이라는 수열이 나올때까지 과정을 몇 번 수행했는지 return 하도록 solution 함수를 완성해주세요.


def solution(arr):
    count = 1
    tmp = None
    while count < 10:
        answer = list()
        arr.append(0)
        num = 1

        for i in range(len(arr) - 1):
            if arr[i] != arr[i+1]:
                answer.append(num)
                num = 1
            else:
                num+= 1
        count += 1
        arr = answer
        if len(arr) == 1:
            break
    return count
        
# solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3])
solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2])