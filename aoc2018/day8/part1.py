import sys

tree = [int(x) for x in sys.stdin.read().split(' ')]


def parse_tree(tree, i):
    child_results = 0
    k = i + 2
    for j in range(tree[i]):
        k, this_result = parse_tree(tree, k)
        child_results += this_result
    child_results += sum(tree[k:k + tree[i+1]])
    k += tree[i+1]
    return (k, child_results)

print parse_tree(tree, 0)
