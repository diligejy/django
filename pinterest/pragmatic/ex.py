def test_one(numbers):
    answer = []
    len_list = len(numbers)
    for i in range(len_list):
        for j in range(i+1, len_list):
            values = numbers[i] + numbers[j]
            if not values in answer:
                answer.append(values)
                answer.sort()
    return answer

def test_code():
    assert test_one([2,1,3,4,1]) == [2,3,4,5,6,7]
    assert test_one([5,0,2,7]) == [2,5,7,9,12]