# function to print menu
def menu():

    print('|----------------------------------------------------------|')
    print('| 1. Shortest path between 2 cities                        |')
    print('| 2. Shortest path between 2 cities through x and y cities |')
    print('| 3. Common connection between 3 cities                    |')
    print('| 4. Exit                                                  |')
    print('|----------------------------------------------------------|')

# function to read file and store the city in graph
def read_file():

    # opening flight.txt as read onyl
    file = open('mini_flight.txt', 'r')

    # declaring empty string
    key = ''

    # looping through the file
    for x in file:
        # storing line as a string
        line_string = x
        # getting length of the string and -1
        len_string = len(line_string) - 1

        # cutting the string so only name of the city and country ramin
        city = line_string[7:len_string]

        # if city doesn't exit in city_list, then adding it
        if city not in city_list:
            city_list.append(city)

        # if From is in a string then make city a new key in the graph
        if 'From' in line_string:
            key = city
            flight_graph[key] = []
        # until another From is not reached adding cities to list and associating it with previous key
        if not 'From' in line_string:
            lst = flight_graph[key]
            lst.append(city)
            flight_graph[key] = lst

# function to find the shortest path between two nodes
def find_shortest_path(graph, start_node, target_node, path = []):

    # if starting city doesn't exit in city_list then exit
    if start_node not in city_list:
        return None

    # if target city doesn't exit in city_list then exit
    if target_node not in city_list:
        return None

    # adding current node to the path
    path = path + [start_node]

    # if current_node is target node then return list
    if start_node == target_node:
        return path

    # if current node is not graph then return list
    if start_node not in graph:
        return None

    # declaring empty list
    shortest = None

    # looping through the key associated list
    for node in graph[start_node]:
        if node not in path:
            # recursively calling itself
            newpath = find_shortest_path(graph, node, target_node, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    # return the shortest path
    return shortest

# function to find a path between two nodes
def find_path(graph, start_node, target_node, path = []):

    # adding current node to the path
    path = path + [start_node]

    # if current_node is target node then return list
    if start_node == target_node:
        return path

    # if current node is not graph then return list
    if start_node not in graph:
        return None

    # looping the key values in a list associated
    for node in graph[start_node]:
        if node not in path:
            # recursively calling itself
            newpath = find_path(graph, node, target_node, path)
            if newpath:
                return newpath

    # if no path has been found then return as none
    return None

# function to print path
def print_path(path):

    # looping the list
    for x in path:
        # if the last element has been reached don't print '->' else print it
        if x == path[-1]:
            print(x)
        else:
            print(x, '->', end=' ')

# function for finding common connection between three places
def option3():

    # getting input from the user
    name1 = input('Enter name of the city 1: ')
    name2 = input('Enter name of the city 2: ')
    name3 = input('Enter name of the city 3: ')

    # copying city_list into update_list
    update_list = city_list

    # removing user input name cities from the update_list so we don't loop over
    update_list.remove(name1)
    update_list.remove(name2)
    update_list.remove(name3)

    # looping over updated list
    for x in update_list:
        # finding path to c from user input
        lst1 = find_path(flight_graph, name1, x)
        lst2 = find_path(flight_graph, name2, x)
        lst3 = find_path(flight_graph, name3, x)

        # getting len of the paths
        len1 = len(lst1) - 2
        len2 = len(lst2) - 2
        len3 = len(lst3) - 2

        # if len of the all the path is greater then 0 then stop the loop and print
        if len(lst1) != 0 and len(lst2) != 0 and len(lst3) != 0:
            print('You should three meet at city:', lst1[-1])
            print('Route for first person:', end=' ')
            print_path(lst1)
            print('Route for second person:', end=' ')
            print_path(lst2)
            print('Route for third person:', end=' ')
            print_path(lst3)
            print('Total connection', len1 + len2 + len3)
            break

if __name__ == '__main__':

    # graph as adjacency list data structure to store data
    flight_graph = {

    }
    # creating an empty list that will be able to store all the city present in graph
    city_list = []

    # calling read_file function to
    read_file()

    # initializing user input so it will loop once
    user_input = '1'

    while user_input != 4:

        # calling menu function
        menu()

        # taking in user input
        user_input = int(input('Enter: '))

        # if user input is 1 then find shortest path between two cities
        if user_input == 1:
            name1 = input('Enter name of starting city:  ')
            name2 = input('Enter name of target city:    ')
            list1 = find_shortest_path(flight_graph, name1, name2)
            print_path(list1)
            print('Total connection:', len(list1) - 2)
            print()

        # if user input is 1 then find shortest path between two cities through x and y
        if user_input == 2:
            name1 = input('Enter name of starting city:   ')
            name2 = input('Enter name of connection city: ')
            name3 = input('Enter name of connection city: ')
            name4 = input('Enter name of target city:     ')

            lst = find_shortest_path(flight_graph, name1, name2)
            lst2 = find_shortest_path(flight_graph, name2, name3)
            if len(lst2) != 0:
                lst2.pop(0)
            lst += lst2
            lst2 = find_shortest_path(flight_graph, name3, name4)
            if len(lst2) != 0:
                lst2.pop(0)
            lst += lst2
            print_path(lst)
            print('Total connection:', len(lst) - 4)

        # if user input is 3 then call option3 function
        if user_input == 3:
            option3()