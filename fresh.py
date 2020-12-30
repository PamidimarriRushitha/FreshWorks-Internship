import code as x
import threading 
from threading import*
import time
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
