#import os

#현재 디렉토리 확인
#print(os.getcwd())

# 디렉토리 이동명
#os.chdir("../ch03")

# 파일열기 -> 열어서 data라는 파일 객체에 대입
data = open('sketch.txt')

#readline() -> 한라인 읽기
print(data.readline(), end='')
print(data.readline(), end='')

# 현재 위치 알리기
#print(data.tell())

# 파일의 제일 앞으로 돌아가기
data.seek(0)

for each_line  in data:
#     print(each_line, end='')
    # ':'을 기준으로 자르기
#     (role, line_spoken) = each_line.split(":")
#     print(role, end='')
#     print(' said: ', end='')
#     print(line_spoken, end='')
    #too many values to unpack (expected 2) -> : 이 두 개이상 있는 경우
     (role, line_spoken) = each_line.split(":", 1)
     print(role, end='')
     print(' said: ', end='')
     print(line_spoken, end='')
#    need more than 1 value to unpack -> : 이 없는 경우
    
# 파일 닫기
data.close()
