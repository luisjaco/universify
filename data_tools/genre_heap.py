# We will store the individual genres in a max heap where each node holds 
# a dictionary for each genre. This dictionary will hold values as follows:
# {
#   "genre" : genre name
#   "score" : 'score' of genre
#   "freshman_score" : score of freshmen only
#   "sophomore_score" : score of sophomores only
#   "junior_score" : score of juniors only
#   "senior_score" : score of seniors only
#   "graduate_score" : score of graduates only
#   "unknown_score" : score of those who do not choose to identify
# }
# with the heap looking like: [{genre data}, {genre data}].
# This file holds functions to upkeep the genre heap, add to a genre heap, and retrieve the top genres.

def parent(pos): 
    return pos//2

def left_child(pos): 
    return pos*2

def right_child(pos): 
    return (pos*2)+1

def isLeaf(heap, pos):
    if pos >= (len(heap)//2) and pos <= len(heap):
        return True
    return False

# Swaps the two genres.
def swap(heap, genre_list, pos1, pos2):
    # Adjusts the genre_list to keep track of the positions of swapped genres
    genre_list[heap[pos1]['genre']] = pos2
    genre_list[heap[pos2]['genre']] = pos1
    # Swaps genres in the heap
    heap[pos1], heap[pos2] = heap[pos2], heap[pos1]
    
# Maintains the heap starting from the first position.
def maxHeapify(heap, genre_list, pos=1): 
        # Created by GeeksForGeeks. Modified by Luis to fit the program.
        # If the node is a non-leaf node and score smaller
        # than any of its child
        if not isLeaf(heap, pos):
            if (heap[pos]['score'] < heap[left_child(pos)]['score'] or
                heap[pos]['score'] < heap[right_child(pos)]['score']):
  
                # Swap with the left child and heapify
                # the left child
                if (heap[left_child(pos)]['score'] > heap[right_child(pos)]['score']):
                    swap(heap, genre_list, pos, left_child(pos))
                    maxHeapify(heap, genre_list, left_child(pos))
  
                # Swap with the right child and heapify
                # the right child
                else:
                    swap(heap, genre_list, pos, right_child(pos))
                    maxHeapify(heap, genre_list, right_child(pos))

# Adds a new genre to the heap and adjusts it to the right position.
def add_genre(heap, genre_list, element):
        # Adds the new element to the end of the list.
        heap.append(element)
        current = len(heap)-1
        genre_list[element['genre']] = current
        # Loops while current genre has a higher score than its parent, and swaps genres.
        while (parent(current) > 0 and heap[current]['score'] > heap[parent(current)]['score']):
            
            heap = swap(heap, genre_list, current, parent(current))
            current = parent(current)
            # Checks edge cases, current is index 0 or parent is 0.
            if current == 0 or parent(current) == 0:
                break

# Changes value to existing genre in the heap, then maintains the heap.
def update_heap(heap, genre_list, element):
    pos = genre_list[element['genre']]
    # Adds new data to existing genre data.
    heap[pos]['score'] += element['score']
    heap[pos]['freshman_score'] += element['freshman_score']
    heap[pos]['sophomore_score'] += element['sophomore_score']
    heap[pos]['junior_score'] += element['junior_score']
    heap[pos]['senior_score'] += element['senior_score']
    heap[pos]['graduate_score'] += element['graduate_score']
    heap[pos]['unknown_score'] += element['unknown_score']
    # Heapifies-up to keep the heap.
    maxHeapify(heap, genre_list)

def genre_present(genre_list, genre_name):
    # Looks for genre in the current genre_list. If not found, returns -1.
    return genre_list.get(genre_name) is not None

# Prints current heap items and the genre positions.
def print_items(heap, genre_list):
    for i in heap:
        if i:
            for k, v in i.items():
                print(k + ": " + str(v))
            print()
    print(genre_list)

# Function to use in other files, takes school dict, then grabs the heap and genre_list.
def edit_heap(school_dictionary, element):
    genre_list = school_dictionary['genre_positions']
    heap = school_dictionary['genre_heap']

    if genre_present(genre_list, element['genre']):
        update_heap(heap, genre_list, element)
    else:
        add_genre(heap, genre_list, element)

def get_top_three(heap):
    # If heap does not have three genres in it, it should be empty
    if len(heap) == 1:
        return [None, None, None]
    elif len(heap) == 2:
        return [ heap[1], None, None ]
    elif len(heap) == 3:
        return [ heap[1], heap[2], None ]
    else:
        if heap[2]['score'] > heap[3]['score']:
            return [ heap[1], heap[2], heap[3] ]
        else:
            return [ heap[1], heap[3], heap[2] ]
