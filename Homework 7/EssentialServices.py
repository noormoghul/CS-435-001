# python 2

import sys 
from collections import defaultdict 
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 

    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
        if smallest != idx: 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
            self.swapMinHeapNode(smallest, idx) 
            self.minHeapify(smallest) 

    def extractMin(self): 
        if self.isEmpty() == True: 
            return
        root = self.array[0] 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.minHeapify(0) 
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
        i = self.pos[v] 
        self.array[i][1] = dist 
        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)/2 ) 
            i = (i - 1) / 2; 
  
    def isInMinHeap(self, v): 
        if self.pos[v] < self.size: 
            return True
        return False
  

class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    def addEdge(self, src, dest, weight): 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    def dijkstra(self, src): 
        V = self.V  
        dist = []  
        minHeap = Heap() 
        for v in range(V): 
            dist.append(sys.maxint) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
        minHeap.size = V; 
        while minHeap.isEmpty() == False: 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
            for pCrawl in self.graph[u]: 
                v = pCrawl[0] 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxint and pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
                        minHeap.decreaseKey(v, dist[v])   
        return dist
  

num_citizens = int(input())
all_citizens_dest = {}
citizens = []
for i in range(num_citizens):
    temp = raw_input()
    all_citizens_dest[temp] = i
    citizens.append(temp)
num_dest = int(input())   
total_citizens_dest = num_dest + num_citizens
services = []
ct = 0
services = sorted(services)
for i in range(len(all_citizens_dest), len(all_citizens_dest) + num_dest):
    temp = raw_input()
    services.append(temp)
    all_citizens_dest[services[ct]] = i
    ct += 1
graph = Graph(total_citizens_dest)   
for i in range(int(input())):
    temp = raw_input()
    parsed = temp.split(', ')
    graph.addEdge(all_citizens_dest.get(parsed[0]), all_citizens_dest.get(parsed[1]), int(parsed[2]))
final_ans = []
for i in range(num_citizens):
    results = graph.dijkstra(i)
    preped_result = []
    for j in range(num_citizens, len(all_citizens_dest)):
        preped_result.append(results[j])
    preped_result.append(citizens[i])
    final_ans.append(preped_result)
sorted_final_ans = sorted(final_ans,  key=lambda x: x[-1])
for item in services:
    print item,
print ''

for i in range(len(sorted_final_ans)):
    for j in range(len(sorted_final_ans[0])):
        print str(sorted_final_ans[i][j]),
    print ""
    
