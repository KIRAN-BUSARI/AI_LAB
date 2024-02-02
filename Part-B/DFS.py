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
    stack=[start]
    visited=[]

    while stack:
        print("Before ",stack)
        node=stack.pop()
        visited.append(node)
        print("Visited: \n",visited)
        for child in reversed(tree[node]):
            # print(child)
            if child not in visited and child not in stack:
                stack.append(child)
        print("After ",stack)
    
    return visited

print(depth_first_search(tree,1))