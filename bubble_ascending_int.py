def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                temp=array[j]
                array[j] = array[j+1]
                array[j+1]=temp
                
    print(array)

def driver():
    A=[5,7,2,1,6,77,9]
    bubble_sort(A)         
    
driver()
                