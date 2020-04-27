# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:30:18 2020

@author: Asia Kamolpanus
"""
import os.path
import sys

class Graph():
    # take a filename and create dictionary graph connection
    def __init__(self, filename):
        with open(filename) as f:
            data = f.readlines()
        data = [x.strip() for x in data]   #strip /n

        graph = {}
        for edge_connect in data:
            node = list(edge_connect.split())
            graph[node[0]] = node[1:]  #first index = node , other index = neighbors

        self.graph = graph

    def search(self, mode, start, goal):
        # create empty list  (queue, expand path)
        queue = []
        expand = []
        mode = mode.lower()  # lower case string

        # first expand (start node)
        queue.append([start])

        while queue:
            # create empty node string (node ที่จะ expand)  , # node_queue = candidate node (เอาไป sort เพื่อแก้เรื่อง tie)
            node = ''
            node_queue = []

            # bfs หา min length ของ path ที่อยู่ใน queue แล้ว append เข้า node_queue
            if mode == 'bfs':
                min_length = []
                for value in queue:
                    min_length.append(len(value))
                min_length = min(min_length)
                for q in queue:
                    if len(q) == min_length:
                        node_queue.append(q)
            # dfs: find max length ของ path ที่อยู่ใน queue แล้ว append เข้า node_queue
            if mode == 'dfs':
                max_length = []
                for value in queue:
                    max_length.append(len(value))
                max_length = max(max_length)
                for q in queue:
                    if len(q) == max_length:
                        node_queue.append(q)

            # sort node_queue by last index for alphabet tie breaking
            node_queue = sorted(node_queue, key=lambda x: x[-1])

            # remove path ใน queue ที่ = node queue index 0 เพราะจะเป็น path ที่ถูกเลือกทำ expand ต่อ
            queue.remove(node_queue[0])

            # get first path from node_queue
            path = node_queue.pop(0)

            # get last value(node) from the path for expand
            node = path[-1]

            # append expand node to expand path
            # ถ้า node ถูก expand ให้ append แบบใส่ () แล้ว continue ข้ามส่วนที่เหลือ ไปหา node ใหม่
            if node in expand:
                expand.append('('+node+')')
                continue
            else:
                expand.append(node)


            # path found  (node = goal): print best path and expand path then stop
            if node == goal:
                print('path =', path)
                print('expand =', expand)
                break


            # get all connected nodes -> create new path -> append new path to queue
            for connected_node in self.graph.get(node, []):


                # create new path  (chosen path for expand + connected_node)
                new_path = list(path)
                new_path.append(connected_node)

                # check duplicate value example [A, B, A]
                # path ที่ขนาดมากกว่าหรือเท่ากับ 3 มีโอกาสที่ตัวสุดท้ายกับตัวที่ 3 ก่อนสุดท้ายเท่ากัน เพราะมีความสัมพันธ์ไปกลับ จึงต้องเช็คว่าไม่เอา

                if len(new_path) >= 3:
                    if new_path[-1] != new_path[-3]:
                           queue.append(new_path)
                else:
                    queue.append(new_path)



if __name__ == '__main__':
    while True:
        filename = str(input('Please input file name (example in.txt) '))
        if os.path.isfile(filename) == False:
            print('incorrect path')
            continue
        break
    while True:    
        user_input = input('Please input mode(BFS/DFS) + start node + goal node (example BFS A M) ')
        if user_input == "end":
            sys.exit()
        mode, start, goal = user_input.split()
                    
        mode = mode.lower()
        start = start.upper()
        goal = goal.upper()
    
        graph = Graph(filename)
        graph.search(mode, start, goal)
        