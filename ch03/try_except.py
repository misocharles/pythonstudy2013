data = open('sketch.txt')

for each_line  in data:

    try:
        (role, line_spoken) = each_line.split(":", 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        print("###crash")
        pass
    
    #pass : 빈 문장(null, empty)으로 아무런 처리를 하지않는다.
data.close()
