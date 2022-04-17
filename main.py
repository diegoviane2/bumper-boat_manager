##########################################
# Written by Diego Viane                 #
# Github: https://github.com/diegoviane2 #
##########################################
from machine import Pin
import _thread
from time import sleep
import heapq
import random

#Pinout definitions
rl1 = Pin(2, Pin.OUT)
rl2 = Pin(4, Pin.OUT)
rl3 = Pin(17, Pin.OUT)
rl4 = Pin(16, Pin.OUT)


player_pins = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1], [0,1,0,0], [0,1,0,1], [0,1,1,0] , [0,1,1,1], [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

qe = []
heapq.heapify(qe)

def read_pins(pins): 
    return rl1.value(pins[3]),rl2.value(pins[2]),rl3.value(pins[1]),rl4.value(pins[0])

def queue_insert(bt_pressed, queue):
    heapq.heappush(queue,bt_pressed)
    
def queue_delete(queue):
    return heapq.heappop(queue)
    
def input_reader():
    while True:
        data = input('Bote: ')
        queue_insert(data,qe)
    
_thread.start_new_thread(input_reader,())

while True:
       
    while len(qe) > 0:
        read_pins(player_pins[int(queue_delete(qe))])
        sleep(3)
        read_pins(player_pins[0])
        sleep(0.5)