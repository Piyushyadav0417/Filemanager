word = "learning"
with open("practice.txt", 'r') as f:
    
    
    
    
    
    
    
    
    
    
    
    
    # 3
    all_line = f.readlines()
    for line_number, i in enumerate(all_line, start=1):
        if word in i:
            print(line_number)
            break
    
    
    
    
    
    
    
    
    
    
    
    # 2
    # line1 = f.readline()
    # line2 = f.readline()
    # line3 = f.readline()
    # line4 = f.readline()
    # allline = [line1, line2, line3, line4]
    # for line_number, i in enumerate(allline, start=1):
    #     if word in i:
    #         print(line_number)
    
    
    
    
    
    # 1
    # line1 = f.readline()
    # line2 = f.readline()
    # line3 = f.readline()
    # line4 = f.readline()
    
    # if word in line1:
    #     print(1)
    # elif word in line2:
    #     print(2)
    # elif word in line3:
    #     print(3)
    # elif word in line2:
    #     print(4)
    # else:
    #     print("Not found")