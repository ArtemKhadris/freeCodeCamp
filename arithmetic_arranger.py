def arithmetic_arranger(tasks, c=False):
    # 4 empty strings for output
    s1, s2, s3, s4 = str(), str(), str(), str()

    #function solve less than 5 problems
    if len(tasks) >= 5:
        return 'Error: Too many problems.'
    
    for task in tasks:
        task = task.replace(' ','')

    # other errors checking:
    # use only = or -
    # use only digits
    # lenght of number less than 5 symbols
        p = 0
        p += task.count('+')
        p += task.count('-')
        if p > 1:
            return 'Error: Numbers must only contain digits.'

        # for addition
        if '+' in task:
            task = task.split('+')
            for i in range(len(task)):
                for j in range(len(task[i])):
                    if task[i][j].isalpha():
                        return 'Error: Numbers must only contain digits.'
            task.append('+')
            if len(task[0]) > 4 or len(task[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            task.append(int(task[0]) + int(task[1]))

        # for substruction
        elif '-' in task:         
            task = task.split('-')
            for i in range(len(task)):
                for j in range(len(task[i])):
                    if task[i][j].isalpha():
                        return 'Error: Numbers must only contain digits.'
            task.append('-')
            if len(task[0]) > 4 or len(task[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            task.append(int(task[0]) - int(task[1]))
        
        # error sign
        else:
            return 'Error: Operator must be "+" or "-".'

        # m - coef for spaces in last two strings (solution and -----)
        m=abs(len(str(task[3])) - max(len(task[0]), len(task[1])) - 2)
        # n - coef for spaces in highest string
        n=((max(len(task[0]), len(task[1]))) - len(task[0]) + 2)
        # l -coef for second string
        l=((max(len(task[0]), len(task[1]))) - len(task[1]) + 1)
        
        # preparing output 
        s1 += ' ' * n + task[0] + ' ' * 4
        s2 += task[2] + ' ' * l + task[1] + ' ' * 4
        s4 += ' ' * m + str(task[3]) + ' ' * 4
        s3 += '-' * len(' ' * m + str(task[3])) + ' ' * 4

    # output
    if c:
        output='\n'.join((s1.rstrip(), s2.rstrip(), s3.rstrip(), s4.rstrip()))
    else:
        output='\n'.join((s1.rstrip(), s2.rstrip(), s3.rstrip()))
    return output

# test
# print(arithmetic_arranger(["3 + 8", "1 - 3801", "9999 + 1", "523 - 49"], True))