from linked_list import Linked_List

def split(l_list):

    if l_list == None or l_list.head == None:
        l_left = l_list
        l_right = None
        return l_left, l_right

    else:
        midpoint = l_list.size() // 2
        mid_node = l_list.node_at_index(midpoint - 1)

        left_half = l_list
        right_half = Linked_List()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):

    merged_list = Linked_List()
    merged_list.add(0)

    current = merged_list.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:

        if left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node

        elif right_head == None:
            current.next_node = left_head
            left_head = left_head.next_node

        else: 
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node


    merged_list.head = merged_list.head.next_node
    return merged_list

def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


L = Linked_List()
L.add(534)
L.add(6)
L.add(534)
L.add(756)
L.add(3546)
L.add(72)

print("UNSORTED: ", L)
print("SORTED: ", merge_sort(L))









