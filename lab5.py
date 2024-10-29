
import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:data.Time, time2:data.Time) ->data.Time:
    time3 = data.Time(time1.hour + time2.hour, time1.minute + time2.minute, time1.second + time2.second)
    while time3.second >59:
        time3.second -= 60
        time3.minute += 1
    return time3

# Part 4
def is_descending(lista:list)->bool:
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            return False
    return True

# Part 5
def largest_between(lista, idx1, idx2):
    if idx1 < idx2:
        largest = lista[idx1]
        for i in range(idx1+1,idx2+1):
            if lista[i] > largest:
                largest = lista[i]
        return largest
    elif idx1> idx2:
        largest = lista[idx2]
        for i in range(idx2 + 1, idx1):
            if lista[i] > largest:
                largest = lista[i]
        return largest
    else:
        return lista[idx1]



# Part 6
def furthest_from_origin(lista:list):
    if len(lista) == 0:
        return None
    else:
        furthest = lista[0]
        furthest_distance = (lista[0].x**2 + lista[0].y**2)**0.5
        for i in range(1,len(lista)):
            new_distance = (lista[i].x**2 + lista[i].y)**0.5
            if furthest_distance < new_distance:
                furthest = i
                furthest_distance = new_distance
        return furthest