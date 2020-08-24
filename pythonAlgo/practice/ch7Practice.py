# chapter7 연습문제

# 7-1
# 1부터 10까지의 숫자를 각 라인 단위로 파일에 출력하는 프로그램 작성

f = open("number.txt", "wt")
for i in range(1, 11):
    f.write(str(i))
    f.write("\n")
f.close()

# 7-2
# 사용자에게 경로를 입력받은 후 해당 경로에 있는 디렉터리와 파일 목록을 flist.txt라는 파일로 출력하는 함수를 작성하세요


def printFile(path):
    import os
    filelist = os.listdir(path)
    f = open("flist.txt", "wt")
    for file in filelist:
        f.write(file)
        f.write("\n")
    f.close()


printFile("/mnt/c/systemTrading/pythonAlgo")
