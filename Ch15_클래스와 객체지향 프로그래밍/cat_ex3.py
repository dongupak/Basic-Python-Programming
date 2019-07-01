class Cat:
    # 생성자 혹은 초기화 메소드라 한다
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 고양이 클래스의 정보를 출력하는 메소드
    def info(self):
        print('고양이 이름은',self.name, '색깔은 ', self.color)

cat1 = Cat("네로", "검정색")  # cat1 인스턴스 생성
cat2 = Cat("미미", "갈색")  # cat2 인스턴스 생성

cat1.info()
cat2.info()

