def gordon(a):
    a=a.upper()
    a=a.replace(' ', '!!!! ')
    a=a.replace('A', '@')
    vowels = ['E', 'I', 'O', 'U']
    for each in vowels:
        a=a.replace(each, '*')
    return print(a + '!!!!')

gordon('What feck damn cake')
gordon('are you stu pid')
gordon('i am a chef')
gordon('dont you talk tome')
gordon('how dare you feck')