list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]

if list1 is list1:
    print("list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1, list2의 데이터 값은 동일하며")
    if list1 is list2:
        print("list1과 list2는 같은 인스턴스입니다")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다")

