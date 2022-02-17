import os
import colorama
import threading

# 3x+1

class Index:
    def __init__(self):
        self.current_index = 1

    def update_index(self, new_index):
        self.current_index = new_index

    def get_current_index(self):
        return self.current_index

index = Index()

class Title:
    def __init__(self):
        self.longest_tree = 0
        self.title = f'"3x+1 Checker | Made by Lunafy#0923 | Current Index: {index.get_current_index()} | Longest Tree [Max 100k]: {self.longest_tree}"'

    def update_longest_tree(self, new_value):
        self.longest_tree = new_value

    def get_longest_tree(self):
        return self.longest_tree

    def update_title(self):
        self.title = f'"3x+1 Checker | Made by Lunafy#0923 | Current Index: {index.get_current_index()} | Longest Tree [Max 100k]: {self.longest_tree}"'
        os.system(f"title {self.title}")

title = Title()

class MessageType:
    class SUCCESS:
        fore = colorama.Fore.GREEN
    class ERROR: 
        fore = colorama.Fore.RED

def log_state(self, content: str, type: MessageType):
    self.pending_logs.append(type.fore + content + colorama.Fore.RESET)


def runner():
    while True:
        starting_number = index.get_current_index()
        index.update_index(starting_number + 1)
        current_number = starting_number

        numbers = []

        for i in range(100000):
            if current_number % 2 == 0:
                try:
                    current_number /= 2
                except:
                    break
            else:
                current_number = (3*current_number) + 1
            
            if current_number in [4, 2, 1]:
                break

            numbers.append(current_number)
        
        if len(numbers) > title.get_longest_tree():
            title.update_longest_tree(len(numbers))

        if current_number not in [4, 2, 1]:
            with threading.Lock(): log_state(f"[SUCCESS] Attempted number: {starting_number}", MessageType.SUCCESS)
            with open("out.txt", "w+") as out:
                out.write(f"VALID NUMBER: {current_number}")
                out.close()

def window_title():
    last_index = index.get_current_index()
    while True:
        if index.get_current_index() != last_index:
            title.update_title()
            last_index = index.get_current_index()

thread_count = 10000

active_threads = []

title_updater = threading.Thread(target=window_title)
title_updater.start()

active_threads.append(title_updater)

for i in range(thread_count):
    thread = threading.Thread(target=runner)
    thread.start()
    active_threads.append(thread)

