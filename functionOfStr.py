# 문자열 관련 함수들
a = "hobby"
print(a.count('b')) #문자열 중 b의 갯수
print(a.find('b')) #문자열 중 b의 위치
print(a.find('k')) # 없는 경우

#indexOf와 기능이 유사한 함수이다........ㅎㅎㅎ 자주쓰겠네

#말하자 마자 인덱스 알려주는 함수가 나오네.....

b = "Life is too short"
print(b.index('t'))
#print(b.index('k')) 없으면 딱 오류 발생해버림

# 이번엔 글자 마다 특정 문자 포함시키기
c = "abcde"
print(','.join(c))

#이렇게 배열에도 포함시킬 수 이씀
print(','.join(['a','b','c','d']))

# 이건 어디에나 많이 쓰일텐데 파이썬이 좋아보이는 점은 함수명이 짧다는 것....... ㅎㅎㅎ편해버림!!!! 인간과 친숙한 언어러구만
d ="orange"
print(d.upper())
e = "APPLE"
print(e.lower())

#이것도 진짜 많이 쓰일 것 같은데 공백 지우는 함수들!!!!!!!!!!!!!!!!!!!!!!!!!!

f = '      apple         '
print(f.lstrip())
print(f.rstrip())
print(f.strip())

#이건 뭐 똑같지 뭐 텍스트 대체하는 함수
g = "My life is beautiful"
print(g.replace('life', 'glasses'))

# 이것도 되게 많이 쓰이는 함수임.......!!!!!!!!!!!!!!근데 똑같애버림 ㅎㅎㅎㅎ
h = "Life is so cool"
i = "baby:it's:cold:outside"
print(h.split())
print(i.split(":"))