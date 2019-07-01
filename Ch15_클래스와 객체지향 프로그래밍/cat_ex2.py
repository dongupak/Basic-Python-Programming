class Cat:
    def info(self):  # info() 메소드
        self.name = "나비"  # 인스턴스 변수 name 생성
        self.color = "검정색"  # 인스턴스 변수 color
        print('고양이 이름은', self.name, '색깔은', self.color)

cat = Cat()  # 인스턴스 생성
cat.info()  # 인스턴스의 메소드 실행

