#슬라이싱 : 시작값이상 끝값미만
a = list(range(20))
print(a)
print(a[0:5]) #앞에 0생략 가능 =[:5]
print(a[10:15]) #11번째~15번째 구할때

#음수인덱싱 : 뒤에서부터 가리킴, 가장 뒤 원소(-1)
print(a[-1])
#음수슬라이싱
print(a[-3:]) #맨뒤 인덱스 생략 가능, 끝까지 의미
print(a[-3:-1])