class Puppy:

    name = "" # 멤버 변수(필드) : class 안에서 사용 가능한 변수
    goal = ""

    def __init__(self, name, goal): # 생성자: 객체화 시 호출되는 함수
        # 받아온 name 과 goal 은 이 생성자를 벗어날 수 없다. (생성자의 쓰임이 다하면 함께 없어진다.)
        # 그래서 클래스(객체) 멤버 에다가 넣어줘야, 객체가 살아있는 동안 사용이 간으하다.
        # 그런데 name = name 형태로는 어떤 것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀석은 self 를 이용하여 표시해 준다.
        self.name = name
        self.goal = goal

puppy = Puppy("멍멍이", "집지키기")