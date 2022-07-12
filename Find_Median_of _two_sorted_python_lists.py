import numpy as np
import random
def generate_random_lists():
    len1 = [random.randrange(2, 100, 1) for i in range(1)][0]
    len2 = [random.randrange(2, 30, 1) for i in range(1)][0]
    list1 = [random.randrange(1, 50, 1) for i in range(len1)]
    list2 = [random.randrange(1, 100, 1) for i in range(len2)]
    list1 = np.sort(list1)
    list2 = np.sort(list2)
    return list1, list2

class Solution(object):
    def findMedianSortedArrays(self, list1, list2):
        total_length = len(list1)+len(list2)
        median_pos = int(total_length/2)
        flag = 0; median = ""
        update = 0
        if total_length == 2:
            median = sum(np.concatenate((list1,list2)))/2
        if total_length == 1:
            median = np.concatenate((list1,list2))[0]
        if total_length == 0:
            median = "nan"
            print("The input lists have problem")
            print("list1 :", list1, "list2 :", list2)
        # cases when both the lists are of same size
        if len(list1) > 1 and len(list1) == len(list2):
            if update == 0 and list1[0] <= list2[0]:
                list2 = np.insert(list2,0,list1[0])
                list1 = list1[1:]
                update = 1
            if update == 0 and list1[0] > list2[0]:
                list1 = np.insert(list1,0,list2[0])
                list2 = list2[1:]
                update = 1
        if total_length > 2 and len(list1) <= median_pos:
            list3 = list1
            list1 = list2
            list2 = list3
            list3 = []
        if total_length > 2 and len(list1) == 0:
            list1 = [list2[0]]
            list2 = list2[1:]
        if total_length > 2 and len(list2) == 0:
            list2 = [list1[0]]
            list1 = list1[1:]
            
        if total_length > 2 and len(list1) > median_pos:
            start_pos = 0
            while flag == 0:
                if start_pos < len(list2) and list1[median_pos] > list2[start_pos]:
                    median_pos = median_pos-1
                    start_pos = start_pos+1
                else: 
                    flag = 1
                if flag == 1 and total_length%2 == 0 and list1[median_pos] >= list2[start_pos-1] and list1[median_pos-1] <= list2[start_pos-1]:
                    if start_pos > 0:
                        median = (list1[median_pos]+list2[start_pos-1])/2
                    if start_pos <= 0:
                        median = (list1[median_pos]+list1[median_pos-1])/2
                if flag == 1 and total_length%2 == 0 and list1[median_pos-1] > list2[start_pos-1]:
                    median = (list1[median_pos]+list1[median_pos-1])/2
                if flag == 1 and total_length%2 == 0 and list1[median_pos] < list2[start_pos-1] and start_pos <= len(list2):
                    if start_pos > 1:
                        median = (max(list2[start_pos-2],list1[median_pos])+list2[start_pos-1])/2
                    else:
                        median = (list1[median_pos+start_pos-1]+min(list1[median_pos+start_pos],list2[start_pos-1]))/2
                if flag == 1 and total_length%2 != 0 and median_pos ==  start_pos:
                    median = max(list1[median_pos],list2[median_pos-1])
                if flag == 1 and total_length%2 != 0 and median_pos !=  start_pos:
                    if start_pos == 0 and list1[median_pos] <= list2[start_pos]:
                        median = list1[median_pos]
                    if start_pos == 0 and list1[median_pos] > list2[start_pos]:
                        median = list2[start_pos-1]
                    if start_pos != 0 and list1[median_pos+1] <= list2[start_pos-1]:
                        median = max(list1[median_pos],list2[start_pos-1])
                    if start_pos != 0 and list1[median_pos+1] > list2[start_pos-1]:
                        median = max(list1[median_pos],list2[start_pos-1])
                    else: median = list1[median_pos]
        
        else:pass
        return median
   
solution = Solution()
counter = 0; iterations = 10000
print("Problem Statement: Find Median of two sorted python lists \n")
print("calculating median for randomly generated %s pairs of python lists" %iterations)
print("...................")
for i in range(iterations):
    list1, list2 = generate_random_lists()
    try:
        solution_median = solution.findMedianSortedArrays(list1, list2)
        numpy_median = np.median(np.sort(np.concatenate((list1,list2))))
    except:
        print("There is an error!")
        print("data input :", list1,list2)
    if numpy_median == solution_median or str(numpy_median) == solution_median:
        counter = counter + 1
    if counter == iterations:
        print("Ta Da!!! The solution is producing the correct median which is equal to numpy median for %s randomly generated different size lists." % str(iterations))
    if type(numpy_median) != np.float64:
        numpy_median = str(numpy_median)
    if numpy_median != solution_median:
        print("Solution is wrong for following cases, look at following:")
        print("data input :")
        print(list1)
        print(list2)
        print("solution median:", solution_median)
        print("numpy median :",numpy_median)
        print(len(list1), len(list2))
        print(".....")
