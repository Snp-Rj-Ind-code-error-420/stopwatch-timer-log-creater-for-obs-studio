'''Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>'''
import time
def w_f(day=0,hour=0,minute=0,second=0):
    info=open(r"./log/uptime.txt",'w')
    x=str(day)+':'+str(hour)+':'+str(minute)+':'+str(second)
    info.write(x)
    info.close()

def r_f(x):
    info=open(r"./log/uptime.txt",'r')
    info=info.readline()
    if len(info)<=12:
        info=info.split(':')
        if x==0:
            return info[x]
        elif x==1:
            return info[x]
        elif x==2:
            return info[x]
        elif x==3:
            return info[x]
        else:
            print("ERROR! why you reach this end line ")
def p_t():
    w_f()
    while 1:
        time.sleep(1)
        day=int(r_f(0))
        hour=int(r_f(1))
        minute=int(r_f(2))
        second=int(r_f(3))
        second+=1
        if second==60:
            minute+=1
            second=0
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif minute==60:
            hour+=1
            minute=0
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif hour==24:
            day+=1
            hour=0
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif day==366:
            w_f()
            print('''a year has been pass so.
a very happy new year and, now the program has reach its limits so it terminate''' )
            break
        else:
            
            w_f(day,hour,minute,second)

def s_t():

    while 1:
        time.sleep(1)
        day=int(r_f(0))
        hour=int(r_f(1))
        minute=int(r_f(2))
        second=int(r_f(3))
        
        if second==0 and minute>0:
            minute-=1
            second=60
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif minute==0 and hour>0:
            hour-=1
            minute=60
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif hour==0 and day>0:
            day-=1
            hour=24
            w_f(day,hour,minute,second)
            day=int(r_f(0))
            hour=int(r_f(1))
            minute=int(r_f(2))
            second=int(r_f(3))
        elif day==0 and second==0 and minute==0 and hour==0:
            w_f()
            print('''timer ends''' )
            break
        else:
            second-=1
            w_f(day,hour,minute,second)
print('-'*100)
print("0.stopwatch")
print("1.timer")
print('-'*100)
x=int(input('enter your choice:-'))
if x==0:
    p_t()
elif x==1:
    x=input("enter the timer limit(dd:hh:min:sec)")
    x=x.split(':')
   
    day=int(x[0])
    hour=int(x[1])
    minute=int(x[2])
    second=int(x[3])
    w_f(day,hour,minute,second)
    s_t()
