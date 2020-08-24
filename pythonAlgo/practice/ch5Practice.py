# chapter5 연습문제

# 5-1
# 두 인자의 평균
def myaverage(a, b):
    a, b = float(a), float(b)
    return (a+b)/2


# 5-2
# 리스트를 인자로 받은 후 최대값과 최소값을 반환
# 내장함수 사용하지 않고 구현
def get_max_min(data_list):
    """
    return maxValue(최대값), minValue(최소값)
    """
    maxValue = data_list[0]
    minValue = data_list[0]
    for num in data_list:

        if maxValue < num:
            maxValue = num
        if minValue > num:
            minValue = num
    return maxValue, minValue

# 5-3
# 절대 경로를 입력받은 후 해당 경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환


def get_txt_list(path):
    import os
    result = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('txt'):
            result.append(file)

    return result

# 5-4
# 체체중과 키를 인자로 하여 BMI에 따라 체형 분류 반환


def printBMI(weight, height):
    """
    weight은 kg 단위, height은 m 단위
    """
    bmi = float(weight/(height ** 2))
    if bmi < 18.5:
        return "마른체형"
    elif 18.5 <= bmi and bmi > 25.0:
        return "표준"
    elif 25.0 <= bmi and bmi > 30.0:
        return "비만"
    else:
        return "고도비만"

# 5-5
# 키와 몸무게를 입력받아 체형 정보를 계속해서 출력해주는 프로그램 작성, 무한루프 구조


def BMIProgram():
    while True:
        weight = float(input("몸무게를 kg단위로 입력하여 주세요 : "))
        height = float(input("키를 m단위로 입력하여 주세요 : "))
        print(printBMI(weight, height))

# 5-6
# 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성


def get_triangle_area(width, height):
    return width * height / 2

# 5-7
# 함수의 인자로 시작과 끝을 나타내는 숫자를 받아 시작부터 끝까지의 정수값의 합을 반환하는 함수 작성(시작값과 끝값을 포함)


def add_start_to_end(start, end):
    targetList = list(range(start, end+1))
    result = 0
    for num in targetList:
        result += num
    return result

# 5-8
# 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스틀ㄹ 반환하는 함수


def firstThreeString(data_list):
    result = []
    for string in data_list:
        string = string[0:3]
        result.append(string)

    return result
