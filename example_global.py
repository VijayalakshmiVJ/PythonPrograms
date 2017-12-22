


count = 0

def func():
    global count
    print(count)
    if count > 0:
        print('Count incremented')
    count = count + 1
    print(count)

func()
func()

    
