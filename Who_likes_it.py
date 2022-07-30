#https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python/all/clever

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

#functions to learn from this

#first, use >>>>dictionary<<<< to store value.
    #when working with a big amount of data,
        #this will help we access the value we want easily (hashmap)

#second, the code is >>>line up<<<< so its easy to read
    #to be specific, the part where he put
        # values of the dictionary line up perfectly
        #is a pressure to read

#third, the way he access the >>>index<<< using >>>min<<<
    #this way of using it is so specific
    #to be able to pull off this, experiences is needed

#forth, use >>>format<<< and use >>>*args<<<<
    #this help me understand *args too, without any tiredness


#todo: read this again, i think this is near real situation

def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)


#this one is clearer
#just not an one-line code

