python=523
java=353
c=225
len_line=47
one_char='.'
one_line=len_line*one_char+'\n'

print('python:')
print((int)(python/len_line)*one_line, end='')
print((python%len_line)*one_char+'\n')
print('java:')
print((int)(java/len_line)*one_line, end='')
print((java%len_line)*one_char+'\n')
print('c:')
print((int)(c/len_line)*one_line, end='')
print((c%len_line)*one_char+'\n')
