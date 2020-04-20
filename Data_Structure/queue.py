# coding:utf-8
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def new_task():
    task = random.randrange(1, 181)
    if task == 180:
        return True
    return False


def simulation(numsec, ppm):
    lab_printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []
    for current_sec in range(numsec):
        if new_task():
            task = Task(current_sec)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_sec))
            lab_printer.start_next(next_task)
        lab_printer.tick()

    avg_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (avg_wait, print_queue.size()))


for i in range(10):
    simulation(3600, 10)
