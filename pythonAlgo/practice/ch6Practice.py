# chapter6 연습문제

# 6-1
# 다음의 조건을 만족하는 Point라는 클래스를 작성하세요.

# Point 클래스는 생성자를 통해 (x, y) 좌표를 입력받는다.
# setx(x), sety(y) 메서드를 통해 x 좌표와 y 좌표를 따로 입력받을 수도 있다.
# get() 메서드를 호출하면 튜플로 구성된 (x, y) 좌표를 반환한다.
# move(dx, dy) 메서드는 현재 좌표를 dx, dy만큼 이동시킨다.
# 모든 메서드는 인스턴스 메서드다.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# 6-2
# Point클래스에 대한 인스턴스를 생성한 후 4개의 메서드를 사용하는 코드를 작성하세요
testPoint = Point(4, 2)
print(testPoint.get())

testPoint.setx(5)
testPoint.sety(2)
print(testPoint.get())

testPoint.move(1, 5)
print(testPoint.get())

# 6-3
# 아래의 Stock 클래스에 대해 2개의 인스턴스를 생성했을 때 클래스와 a와 b 인스턴스의 네임스페이스를 그려보세요.

#
