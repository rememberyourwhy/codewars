# https://www.codewars.com/kata/556c04c72ee1147ff20000c9/train/python
#check if enough group and players each day, check if "weird" player joined the list
#check if there are two group that share the same 2 players


#The first problem is easier to handle
#But the second one is much harder and will require a lot of time with big G, D number


#SECOND PROBLEM

def no_repeat(list1, list2):
    common = list(set(list1) & set(list2))
    if len(common) > 1:
        return False
    else:
        return True

#First problem

#This function will give us the list of players from the first day schedule.
#So we can take that and get number of players ("N")
def get_n(day_list):
    day_list_string = str()
    for element in day_list:
        day_list_string += element
    return set(day_list_string), len(day_list_string)
def get_number_of_group(day_list):
    return len(day_list)
def check_first_problem(day_list, list_of_player_starter, number_of_player_starter):
    return get_n(day_list)[0] == list_of_player_starter and get_n(day_list)[1] == number_of_player_starter
def check_second_problem(day_list, number_of_group_starter):
    return len(day_list) == number_of_group_starter

def group_comparision(big_list, group_to_check):
    for day_list in big_list:
        for group_list in day_list:
            if not no_repeat(group_list , group_to_check):
                if group_list != group_to_check:
                    return False
    return True
def check_day_list_element(big_list):
    for index in range(len(big_list)):
        for index2 in range(index + 1, len(big_list)):
            common_list = set(big_list[index]).intersection(big_list[index2])
            if common_list != set():
                return False
    return True
def check_third_problem(big_list):
    if not check_day_list_element(big_list):
        return False
    for day_list in big_list:
        for group_list in day_list:
            if not group_comparision(big_list, group_list):
                return False
    return True

def valid(big_list):
    #check_first_problem:
    list_of_player_starter, number_of_player_starter = get_n(big_list[0])[0], get_n(big_list[0])[1]
    number_of_group_starter = get_number_of_group(big_list[0])
    result12 = True
    for day_list in big_list:
        if not (check_first_problem(day_list, list_of_player_starter, number_of_player_starter) and check_second_problem(day_list, number_of_group_starter)):
            result12 = False
            break

    result3 = check_third_problem(big_list)
    return result12 and result3


s = [
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
print(valid(s))
    #Now we compare each day if they have enough number of players and each player

#Man, pls refactor this code, its suck
#Todo: check solution: https://www.codewars.com/kata/556c04c72ee1147ff20000c9/solutions/python