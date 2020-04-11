#@author: Mr T

import os

class SHen(object):
    def __init__(self,filename):
        if os.path.exists(filename):
            print('[+] Found file:{}'.format(filename))
        else:
            print('[-] Not Found file:{}'.format(filename))
            exit()

        self.file=filename
        self.shengc()

    def shengc(self):
        dk=open(self.file,'r',encoding='utf-8')
        for r in dk.readlines():
            data="".join(r.split('\n'))
            jg1=".".join(data.split(' '))
            jg2=".a.".join(data.split(' '))
            jg3=data.split(' ')
            print(jg1)
            print(jg2)
            print(jg3[0][0]+jg3[1])
            print(jg3[0][0]+'a'+jg3[1])
            print(jg3[0][0] +jg3[0][1]+ jg3[1])
            print(jg3[0][0] + jg3[0][1]+'a'+ jg3[1])

if __name__ == '__main__':
    obj=SHen('lista.txt')
