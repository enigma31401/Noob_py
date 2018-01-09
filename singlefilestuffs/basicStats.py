#code by: Laniakea (Not that it's worth mentioning)

def setSum(list = []):
    total = sum(list) #Didn't have to make this function since sum() is native, but this is just to show how to pass list through/to functions
    return total

#set up mean
def setMean(size, list = []):
    listTotal = sum(list)
    setavg = listTotal/size
    return setavg

#calculate the variance (if statement to get population or sample based answer)
def getVariance(mean, size, list = []):
    from numpy import sum
    print("Calculating Variance....")
    varChoice = input("Calculate for a population or sample(p/s): ")

#If you need help determining when to use equality comparison == versus surface-qualia comparison is , see http://www.dbader.org/blog/difference-between-is-and-equals-in-python
 
    if(varChoice == 'p'):
        print("Calculating var w/ respect for it as a population...")
        anotherlist = []

        x = 0
        numera = 0
        while(x < size):
            
            numera += (list[x]-mean)**2
            # test code print(numera)
            #test code print(list, "and x is ", x)
            # test code print("lol")
            x +=1
        usersVar = numera/size
        return usersVar
            
    elif(varChoice == 's'):
        print("Calculation var w/ respect for it as a sample...")

        x = 0
        numera = 0
        while(x < size):
            numera += (list[x]-mean)**2
            x +=1
        usersVar = numera/(size-1)
        return usersVar

    else: 
        print("Error, probably invalid input!")

def get_stndev(usersvariance):
   import math
   stndDev = math.sqrt(usersvariance)
   return stndDev



 
def get_userSet():
    
    userSet = [] #Declaring essentially, the list to hold the values inputted by the user

    print("Welcome to python stats calculator 1.0")
    setSize = int(input("Enter the size of the set: "))
    if(setSize <= 0):
        exit("Invalid input, exiting program") #exit() is a native function, it ends program abruptly, like break but for all non-loop stuff, insert text dialogue inside if you want a message with the exit

    for arbVar in range(setSize): #for-loop for getting set values
        userSet.insert(arbVar, float(input("Input value: "))) #How to input value into each index(establish element)
    #for testing only -> print(sum(userSet))
    
    



    #---------Solutions-------#
    setTotal = setSum(userSet)
    setAverage = setMean(setSize, userSet)
    setVariance = getVariance(setAverage, setSize, userSet)
    setStandardDev = get_stndev(setVariance)
    #---------Final Output----#
    print("Set summation: ", round(setTotal,2))
    print("Set average: ", round(setAverage,2))
    print("Set variance: ", round(setVariance,2))
    print("Set standard deviation: ", round(setStandardDev,2)) 




get_userSet()

