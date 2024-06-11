#Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, 
# ta cũng được một số nguyên tố.
# Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
import math
def rivot(N):
    reverse = 0
    while(N != 0):
        r = N  % 10
        N //= 10
        reverse = reverse * 10 + r
    return reverse
def checkNto(N):
    if N < 2:
        return False
    for i in range(2, int(math.sqrt(N)) + 1, 1):
        if N % i == 0:
            return False
    return True  
if __name__ == '__main__':
    N = int(input('Nhập số nguyên N : '))
    for i in range(10, N, 1):
        if checkNto(i) == True and checkNto(rivot(i)) == True and i != rivot(i):
            print(i)
            
        
        
    
    