import sys
import time
from tqdm import tqdm
import threading
class audum():
    count = 0
    def __init__(self,a, b, c,d,e,f,g,h):

        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h




    def kalu(self):
        n1 = input('fav 3 digit num:')
        j = f'{n1}'
        n2 = input('contact number +91:')
        k = f'{n2}'
        n3 = input('birth date:')
        l = f'{n3}'
        n4 = input('birth month:')
        m = f'{n4}'
        n5 = input('birth year:')
        n = f'{n5}'
        n6 = input('Bike Number:')
        o = f'{n6}'
        n7 = input('car Number:')
        p = f'{n7}'
        n8 = input('shoes Number:')
        q = f'{n8}'
        mylist = [a, b, c,d,e,f,g,h,j,k,l,m,n,o,p,q]

        count = 0
        for z in mylist:
          for i in mylist:
             print(z + i)
             file.write("\n" + z + i)
             print(z +'@'+ i)
             file.write("\n" + z + '@' + i)
             count = count +1
        count1 = 0
        for i in mylist:
             print(i + "@123")
             file.write("\n" + i + '@123')
             print(i)
             file.write("\n" + i)
             count1 = count1 +1



        print(f'Total passwords{count1 + count}')


    def passw(self):
        mylist1 = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        mylist2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
        num = int(input("enter the length of your pass:"))
        count2 =0
        for ii in mylist2:
            if (num == 1):
                print(ii)
                file.write("\n" + ii)
                count2 = count2 +1
            for jj in mylist1:
                if (num == 2):
                    print(ii + jj)
                    file.write("\n" + ii + jj)
                    count2 = count2 + 1

                for kk in mylist1:
                    if (num == 3):
                        print(ii + jj + kk)
                        file.write("\n" + ii + jj + kk)
                        count2 = count2 + 1

                    for ll in mylist1:
                        if (num == 4):
                            print(ii + jj + kk + ll)
                            file.write("\n" + ii + jj + kk + ll)
                            count2 = count2 + 1

                        for mm in mylist1:
                            if (num == 5):
                                print(ii + jj + kk + ll + mm)
                                file.write("\n" + ii + jj + kk + ll + mm)
                                count2 = count2 + 1
        print(f'Total password:{count2}')
        for ii in mylist2:
            for jj in mylist1:
                for kk in mylist1:
                    for ll in mylist1:
                        for mm in mylist1:
                            for nn in mylist1:
                                if (num == 6):
                                    print(ii + jj + kk + ll + mm + nn)
                                    file.write("\n" + ii + jj + kk + ll + mm + nn)
                                    count2 = count2 + 1
                                for oo in mylist1:
                                    if (num == 7):
                                        print(ii + jj + kk + ll + mm + nn + oo)
                                        file.write("\n" + ii + jj + kk + ll + mm + nn + oo)
                                        count2 = count2 + 1
                                    for pp in mylist1:
                                        if (num == 8):
                                            print(ii + jj + kk + ll + mm + nn + oo)
                                            file.write("\n" + ii + jj + kk + ll + mm + nn + oo)
                                            count2 = count2 + 1
                                        for qq in mylist1:
                                            if (num == 9):
                                                print(ii + jj + kk + ll + mm + nn + oo + pp + qq)
                                                file.write("\n" + ii + jj + kk + ll + mm + nn + oo + pp + qq)
                                                count2 = count2 + 1
                                            for rr in mylist1:
                                                if (num == 10):
                                                    print(ii + jj + kk + ll + mm + nn + oo + pp + qq + rr)
                                                    file.write("\n" + ii + jj + kk + ll + mm + nn + oo + pp + qq+ rr)
                                                    count2 = count2 + 1
        print(f'Total password:{count2}')
def check(num):
    if sys.version_info.major < 3:
        print("Must be using Python 3")
        sys.exit()

    for iii in tqdm(range(0, 100), desc="loop1:", unit="CHECKING PYTHON.. "):
        time.sleep(0.01)
    print("\n")

if __name__ == "__main__":
    print('                     A TOOL BY Zsploit                              ')
    print('                                                               ')
    print('       /\                                            /\          ')
    time.sleep(0.1)
    print('      /  \                                          /  \         ')
    time.sleep(0.1)
    print('     /    \                                        /    \        ')
    time.sleep(0.1)
    print('    /      \                                      /      \       ')
    time.sleep(0.1)
    print('   /        \                                    /        \     ')
    time.sleep(0.1)
    print(' [=-------------------------------------------------------=]     ')
    time.sleep(0.1)
    print('  |                                                       |     ')
    time.sleep(0.1)
    print('  |      ----------                         |*  *         |     ')
    time.sleep(0.1)
    print('  |              /                          |     *       |    ')
    time.sleep(0.1)
    print('  |             /                           |      *      |    ')
    time.sleep(0.1)
    print('  |            /                            |     *       |    ')
    time.sleep(0.1)
    print('  |           /           @          @      | * *         |    ')
    time.sleep(0.1)
    print('  |          /          @   @      @   @    |             |    ')
    time.sleep(0.1)
    print('  |         /          @     @   @       @  |             |    ')
    time.sleep(0.1)
    print('  |        /            @   @      @   @    |             |    ')
    time.sleep(0.1)
    print('  |       ---------       @          @      |             |    ')
    time.sleep(0.1)
    print(' [=--------------------------------------------------------=]    ')
    print("===================================================================")
    print('     /\      |---------  =============   ========  \          /                                ')
    print('    /  \     |                 |             |      \        /      ')
    print('   /    \    |                 |             |       \      /     ')
    print('  /______\   |                 |             |        \    /       ')
    print(' /        \  |                 |             |         \  /         ')
    print('/          \ |---------        |         ========       \/          ')
    print("=====================================================================")
    print('                                                         -@Zsploit')
    print('                                                         -V 1.0')
    print("Warning!!! ONLY FOR EDUCATIONAL PURPOSE.")
    print("will try our best for letting you get your desireS passwordS!")

    t1 = threading.Thread(target=check, args=(10,))

    t1.start()
    t1.join(10)
    print(u'Python3 OK \N{check mark}')
    print('Enter the basic details of target')
    a = input("First Name:")
    b = input("last Name:")
    c = input("Fathers Name:")
    d = input("Sisters Name:")
    e = input("brother Name:")
    f = input("fav Actor:")
    g = input('fav Actress:')
    h = input('fav Sports:')

    file = open('password.txt', 'w')
    k = audum(a, b, c,d,e,f,g,h)
    k.kalu()
    k.passw()

