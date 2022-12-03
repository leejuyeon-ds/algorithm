from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반환""" # 이를 함수 어노테이션이라 함
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    
    # step 1: 배열의 원소 수 입력받기
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num인 리스트 생성
    
    # step 2: 배열의 값 입력받기
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
        
    # step 3: 최댓값 구하기 및 반환하기
    print(f'최댓값은 {max_of(x)}입니다.')