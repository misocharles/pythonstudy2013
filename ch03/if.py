
data = open('sketch.txt')

print(data.readline(), end='')
print(data.readline(), end='')

# 파일의 제일 앞으로 돌아가기
data.seek(0)

for each_line  in data:
    
    if each_line.find(":") != -1 :
        (role, line_spoken) = each_line.split(":", 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

data.close()
