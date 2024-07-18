Web VPython 3.2
from vpython import *
import random

def S(arg):
    global speed
    speed = arg.value

def pause_resume():
    global paused
    paused = not paused

def f(x):
    wtext(text="\n\n")
    wtext(text="Select a method")
    wtext(text="    ")
    menu(bind=m, choices=["Select option", "Bubble", "Insertion", "Selection", "Quick", "Merge"])
    wtext(text="\n\n\n\n")
    def m(x):
        if x.index == 1:
            bubble()
        elif x.index == 2:
            insertion()
        elif x.index == 3:
            selection()
        elif x.index == 4:
            quick_sort(0, len(l2) - 1)
        elif x.index == 5:
            merge_sort(0, len(l2) - 1)

canvas(width=1000, height=600, background=color.black)
button(bind=f, text="RUN", color=color.black, background=color.white)
button(bind=pause_resume, text="Pause/Resume", color=color.black, background=color.white)

l = [int(random.randint(1, 50)) for _ in range(1, 100)]
l2 = [box(length=0.8, width=1, height=l[i], pos=vector(i - 50, l[i] / 2, 0)) for i in range(len(l))]

speed = 10
paused = False
slider(bind=S, min=10, max=300)

def bubble():
    wtext(text="Project by:\n")
    wtext(text="    G Nishant           21071A66A9\n")
    
    for i in range(len(l2)):
        for j in range(len(l2) - i - 1):
            # Compare the adjacent elements
            if l2[j].height > l2[j + 1].height:
                # Swap the elements
                l2[j].color=color.red
                l2[j+1].color=color.red
                sleep(1/speed)
                l2[j].height, l2[j+1].height = l2[j + 1].height, l2[j].height
                l2[j].color=color.white
                l2[j+1].color=color.white
        l2[len(l2)-1-i].color=color.blue


def selection():
    wtext(text="Project by:\n")
    wtext(text="    G Nishant\n")
    for i in range(len(l2) - 1):
        min_index = i
        for j in range(i + 1, len(l2)):
            while paused:
                rate(10)
            if l2[j].height < l2[min_index].height:
                min_index = j
        if min_index != i:
            l2[i].color, l2[min_index].color = color.red, color.red
            sleep(1 / speed)
            l2[i].height, l2[min_index].height = l2[min_index].height, l2[i].height
            l2[i].color, l2[min_index].color = color.white, color.white
        l2[i].color = color.blue

def insertion():
    wtext(text="Project by:\n")
    wtext(text="    G Nishant\n")
    l2[0].color = color.blue
    for i in range(1, len(l2)):
        j = i
        l2[i].color = color.blue
        while j > 0 and l2[j].height < l2[j - 1].height:
            while paused:
                rate(10)
            l2[j].color = color.red
            sleep(1 / speed)
            l2[j].height, l2[j - 1].height = l2[j - 1].height, l2[j].height
            l2[j].color = color.blue
            j -= 1
        l2[i].color = color.green

def quick_sort(low, high):
    if low < high:
        pi = partition(low, high)
        quick_sort(low, pi - 1)
        quick_sort(pi + 1, high)

def partition(low, high):
    pivot = l2[high].height
    i = low - 1
    for j in range(low, high):
        while paused:
            rate(10)
        if l2[j].height <= pivot:
            i += 1
            l2[i].color, l2[j].color = color.red, color.red
            sleep(1 / speed)
            l2[i].height, l2[j].height = l2[j].height, l2[i].height
            l2[i].pos.y, l2[j].pos.y = l2[j].pos.y, l2[i].pos.y
            l2[i].color, l2[j].color = color.white, color.white
    l2[i + 1].color, l2[high].color = color.red, color.red
    sleep(1 / speed)
    l2[i + 1].height, l2[high].height = l2[high].height, l2[i + 1].height
    l2[i + 1].pos.y, l2[high].pos.y = l2[high].pos.y, l2[i + 1].pos.y
    l2[i + 1].color, l2[high].color = color.white, color.white
    return i + 1

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    left = l2[low:mid + 1]
    right = l2[mid + 1:high + 1]
    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        while paused:
            rate(10)
        if left[i].height <= right[j].height:
            l2[k].height = left[i].height
            l2[k].pos.y = left[i].height / 2
            i += 1
        else:
            l2[k].height = right[j].height
            l2[k].pos.y = right[j].height / 2
            j += 1
        k += 1
    while i < len(left):
        l2[k].height = left[i].height
        l2[k].pos.y = left[i].height / 2
        i += 1
        k += 1
    while j < len(right):
        l2[k].height = right[j].height
        l2[k].pos.y = right[j].height / 2
        j += 1
        k += 1
