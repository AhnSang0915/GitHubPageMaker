# chapter02-01
# 파이썬 완전 기초
# print 사용법


print('python Start!')
print('''python Start!''')
print("""python Start!""")

# seperator 옵션

print('p', 'y', 't', 'h','o','n', sep= '')
print('010','3763', '4202', sep = '-')
print('tmqjf4921', 'naver.com', sep = '@')

# end 옵션

print('Welcome to', end = ' ')
print('IT News', end = ' ')
print('Web Site')

#file 옵션

import sys

print('Learn Python', file = sys.stdout)
print()

#format 옵션(d(정수), s(문자열), f(소수))

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))


# %s
print('%10s' %('nice'))
print('{:>10}'.format('nice'))

print('%-10s' %('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #원하는 문자를 넣을 수 있다.
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy')) #공간은 10개가 있지만 왼쪽부터 5개만 출력

# %d

print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f 

print('%f' % (3.143434343434))
print('{:f}'. format(3.143434343434))

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
