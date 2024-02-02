tree = {
    1:[2,9,10],
    2: [3,4],
    3:[],
    4:[5,6,7],
    5:[8],
    6:[],
    7:[],
    8:[],
    9:[],
    10:[]
}
def depth_first_search(tree,start):
    queue=[start]
    visited=[]

    while queue:
        print("Before ",queue)
        node = queue.pop(0)
        visited.append(node)
        # print("Visited: \n",visited)
        for child in tree[node]:
            # print(child)
            if child not in visited and child not in queue:
                # print(child)
                queue.append(child)
        print("After ",queue)
    
    return visited

print(depth_first_search(tree,1))