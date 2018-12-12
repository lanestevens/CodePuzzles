import sys

tree = [int(x) for x in sys.stdin.read().split(' ')]


def parse_tree(tree, i):
    child_map = {}
    k = i + 2
    for j in range(tree[i]):
        k, this_result = parse_tree(tree, k)
        child_map[j + 1] = this_result
    
    child_results = 0
    if child_map:
        for j in tree[k:k + tree[i + 1]]:
            child_results += child_map.get(j, 0)
        k += tree[i + 1]
        return (k, child_results)
    child_results += sum(tree[k:k + tree[i+1]])
    k += tree[i + 1]
    return (k, child_results)

print parse_tree(tree, 0)
