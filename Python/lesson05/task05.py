
def GenerateBBSTArray(a):
    a.sort()
    result_tree: list = [None] * len(a)
    result = process_sub_tree_no_side_effect(a, result_tree, 0, 0, len(a) - 1)
    return result

def process_sub_tree_no_side_effect(arr: list, tree: list, root_ind: int, start: int, end: int) -> list:
    new_tree: list = tree.copy()
    if root_ind >= len(arr):
        return new_tree
    if start > end:
        return new_tree
    middle_index: int = int((start + end) / 2)
    new_tree[root_ind] = arr[middle_index]
    new_tree = process_sub_tree_no_side_effect(arr, new_tree, root_ind * 2 + 1, start, middle_index - 1)
    new_tree = process_sub_tree_no_side_effect(arr, new_tree, root_ind * 2 + 2, middle_index + 1, end)
    return new_tree




