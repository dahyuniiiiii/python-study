a = list(range(10))
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#맨뒤에 추가
a.append(10)
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.append(20)
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
print(a[0]) #0, 리스트첫값
#인덱스값삭제
del a[0] #0삭제, 리스트첫값삭제
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
print(a[2]) #3
del a[2] #3삭제, 리스트세번째값삭제
print(a) #[1, 2, 4, 5, 6, 7, 8, 9, 10, 20]
