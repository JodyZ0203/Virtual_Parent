import json
import time
import matplotlib.pyplot as plt
from timeit import default_timer as timer

preMadeInformation = '''
{ 
    "users": [
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 12,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 6,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 25,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 22,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 24,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 19,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 23,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll223213",
         "name": "Lance Lewis",
         "age": 25,
         "password": "progdfamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 18,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 16,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 15,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 20,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 24,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 13,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 13,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll223213",
         "name": "Lance Lewis",
         "age": 35,
         "password": "progdfamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 47,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 6,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 11,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 10,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 21,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 19,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 20,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      }
   ]
}
'''
data = json.loads(preMadeInformation)
with open('basicInformation.json', 'w') as file:
    json.dump(data, file, indent=3)
with open('basicInformation.json') as file:
    data = json.load(file)
    print(data)

infoSort = data['users']
print(len(infoSort))


def bubbleSort(unsortedList):
    length = len(unsortedList)
    while length > 0:
        length -= 1
        i = 0
        while i < length:
            if infoSort[i]['age'] > infoSort[i+1]['age']:
                infoSort[i], infoSort[i+1] = infoSort[i+1], infoSort[i]
                #print(str(i) + " swapped with " + str(i + 1))
            #correctEntry += 1
            i += 1
'''
start_time = time.time()
bubbleSort(infoSort)
print("--- %s seconds ---" % (time.time() - start_time))
print(infoSort)
'''

def selectionSort(unsortedList):
    length = len(unsortedList)
    counter = 0
    j = 0   #min
    i = 0   #current
    while counter < length:
        for i in range(j+1, length):
            if infoSort[i]['age'] < infoSort[j]['age']:
                #print("current item is " + str(i))
                #print("current minimum is " + str(j))
                #print("first item in the unsorted list is " + str(counter))
                j = i  # It will change
        infoSort[counter], infoSort[j] = infoSort[j], infoSort[counter]
        i += 1

        #counter += 1
        counter = counter + 1
        j = counter
'''
start_time = time.time()
selectionSort(infoSort)
print("--- %s seconds ---" % (time.time() - start_time))
'''
'''
for i in range(len(infoSort) - 1, -1, -1):
    if infoSort[i] == 25:
        infoSort.pop(i)
with open('basicInformation.json', 'w+') as f:
    json.dump(data, f, indent=3)
    file.close()
'''
'''
def delUser(number):
    i = 0
    count = 0
    with open('algofile.json') as f:
        data1 = json.load(f)
    infoSort1 = data['users']
    while count < number:
        for i in range(number):
            print(i)
            del infoSort1[i]
        i += 1
        count += 1
        with open('basicInformation.json', 'w+') as f:
            json.dump(data1, f, indent=3)
            file.close()

delUser(10)
'''

def linearSearch(list, key):
    length = len(list)
    i = 0
    while i < length:
        if key == list[i]['age']:
            number = i
            print(str(key) + " is in index: " + str(i))
            return number
        i += 1


def binerySearch(sortedList, key):
    maxi = len(sortedList)
    mini = 0
    comparison = 0
    while mini < maxi:
        if (maxi + mini) % 2 == 0:
            i = int((maxi + mini) / 2)
            comparison += 1
            if infoSort[i]['age'] < key:
                mini = i
            elif infoSort[i]['age'] > key:
                maxi = i
            else:
                print(str(key) + " is in index: " + str(i))
                print("it takes " + str(comparison) + " comparisons")
                return i
                mini = maxi
        else:
            i = int((maxi + mini - 1) / 2)
            comparison += 1
            if infoSort[i]['age'] < key:
                mini = i
            elif infoSort[i]['age'] > key:
                maxi = i
            else:
                print(str(key) + " is in index: " + str(i))
                print("it takes " + str(comparison) + " comparisons")
                return i
                mini = maxi

infoSort.sort(key=lambda age: age['age'])
start = timer()
#infoSort.sort(key=lambda age: age['age'])
#selectionSort(infoSort)
#bubbleSort(infoSort)
#linearSearch(infoSort, 90)
binerySearch(infoSort, 1)
end = timer()
print(end - start)

t = time.process_time()
#infoSort.sort(key=lambda age: age['age'])
#selectionSort(infoSort)
#bubbleSort(infoSort)
#linearSearch(infoSort, 90)
binerySearch(infoSort, 19)
elapsed_time = time.process_time() - t
print(elapsed_time)


x1 = [3500, 4500, 5500, 6500]
y1 = [0.000848, 0.000977, 0.001556, 0.00158]
plt.plot(x1, y1, label="Binary Search plus sort")
x2 = [3500, 4500, 5500, 6500]
y2 = [0.0000299, 0.0000231, 0.0000227, 0.0000226]
plt.plot(x2, y2, label="Binary Search")
x3 = [3500, 4500, 5500, 6500]
y3 = [0.000556, 0.000701, 0.00115, 0.000979]
plt.plot(x3, y3, label="Linear Search")

x4 = [3500, 4000, 4500, 5000, 6000, 7000, 10000]
y4 = [0.000806, 0.000985, 0.001079, 0.0011515, 0.00141, 0.00146, 0.0029475]
plt.plot(x4, y4, label="Sort Function")
plt.xlabel('number of items')
plt.ylabel('run time(s)')
plt.title('Comparison of Run time ')
plt.legend()
plt.show()
'''
x1 = [3500, 4000, 4500, 5000, 6000, 7000, 10000]
y1 = [0.000806, 0.000985, 0.001079, 0.0011515, 0.00141, 0.00146, 0.0029475]
plt.plot(x1, y1, label="Sort Function")
x2 = [3500, 4000, 4500, 5000, 6000, 7000, 10000]
y2 = [2.291, 3.067, 3.71, 4.72, 6.21, 9.05, 19.823]
plt.plot(x2, y2, label="Bubble Sort")
x3 = [3500, 4000, 4500, 5000, 6000, 7000, 10000]
y3 = [1.093, 1.5694, 1.835, 2.35, 2.9288, 4.01, 8.7338]
plt.plot(x3, y3, label="Selection Function")
plt.xlabel('number of items')
plt.ylabel('run time(s)')
plt.title('Comparison of Run time ')
plt.legend()
plt.show()

This code shows me a comparison between bubble sort, selection sort, and the built in sort function on their run time.
The results are what I expected. First of all, the built in function is much more faster than the algorithms 
I have created. As all three algorithms sort through list with more and more items, bubble sort algorithms always had 
most run time, and the built in function always had list amount of time to finish sorting. When only 10000 items were 
given, the bubble sort algorithm took an average of 19.8 seconds, and causing my laptop to freeze for a bit. This goes 
on to show this algorithm's inefficiency. Going back to the code itself, for the bubble sort algorithm there are two 
while loops, which means, every item will be loop through until it is sorted, which means it will take quadratic time, 
so using the notation it will be O(n^2). Same as bubble sort algorithm, for the unsorted items, it will have to loop 
through and compare with every unsorted items in the list, so it uses a for loop and a while loop, making its time 
complexity O(n^2). After comparing the data I collected with the built in function, it seems like this function is so 
fast that the graph looks like a slightly tilted line, so the time complexity for this function is O(log n), even though
this function is fast, but the time is not constant, but if we round the numbers, 0.002 still seems like nothing when 
other algorithms takes 20 seconds to do the same. When the input size (n) is small, the difference in time is 
insignificant, but as n grows and approaches infinity, the run time will take much longer, wasting more resources, time, 
and money.
VIDEO REFLECTION
-I have noticed that the sorting algorithms with thin bars usually have more comparisons between items, and the 
algorithms with thicker bars have less comparisons and seems like it has needs less access to arrays. Additionally, it 
seems like the ones with thicker bars sorts faster, maybe they have the same number of items that needs to be sorted, 
but the size of the bar deceived my judgement on their performance.
- Someone makes the video to visualize the sorting process. The sound different sorting algorithms make is mesmerizing. 
The main audience for this video is for those who know how each algorithms work, for those who don't they will have a
difficult time understanding the process.
-This video can be skewed to show something that is incorrect through the delay, items being shuffled, and the thickness
of the bars. Different sorting algorithms can preform differently based on how the items are sorted, and for some
algorithm, their best case and worst case time complexity is similar. More importantly, it is difficult to make this 
video fair for all sorting algorithms, because they have different standards and different speed. On the screen, the 
thickness of the bars can be deceiving as it tricks you into thinking it will be faster, because it seems like it only
has sort through less items. Moreover, the delay of the sorting process can also be a issue, as it changes how fast the 
algorithm sorts.

After doing 4 trials on linear search, binary search, and binary search with sort function's tun time. It seems like
Binary search is very fast and sufficient. It only takes it roughly 0.00002 seconds to find something I am looking 
for out of 3500 to 6500 items, which is very fast. On the other hand, the linear search is not so fast, as it have to
loop through the whole list, because I am testing for worst case scenario, so it is looking for the last item in the
list. Linear search takes the same amount of time as the built in sort function. Now by examining the code, we can 
determine their time complexity. For binary search, it takes Logarithmic time, so O(log n) is the notation to represent
it. Since, binary search only need a few comparisons, so it does not have to look at every single item in the list. Even
though I used a while loop for this algorithm, it does not go through the whole list every time, but rather narrow down
the input size until the number is found. Therefore, it has a fast run time. Moving on to the the algorithm that 
takes linear time, which is linear search, as it have to look at every single one of the item in the list, so no matter 
how big n is, it always have a linear time complexity as it is only dependent on the size of the input.
'''



