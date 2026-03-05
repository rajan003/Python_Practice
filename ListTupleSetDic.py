## 1️⃣ List -- Ordered Collection (changeable)
  ## fruits = ["apple", "banana" , "mango"]
  ## Properties: Ordered, Can Change, Applow Duplication
     ## fruits.append("orange") >>> Addition/Append
     ## fruits[0]= "Grapes" >>> Modify
     ## print(fruits[1]) >> Index access

## 2️⃣ Tuple -- Ordered but not changeable
  ## point =(10,20)
	## Ordered ✅
	## Cannot change (immutable) ❌
	## Allows duplicates ✅
    ## print(point[0]) >> Works
    ## point[0]= 40 >>> ERROR
 ## Usecase--- Config Settings

## 3️⃣SET --- Unordfered unique collection
  ## number = {1,2,3,3,4} >> {1,2,3,4} >>Duplication removed automatically
    ##	No order ❌
	  ## No duplicates ❌
	  ## Can add/remove items ✅
  ## numbers.add(5)
  ## numbers.remove(2)

 ## 4️⃣ DICTIONARY → “Key → Value pair”
  # Properties
	# Key → Value structure
	# Keys must be unique
	# Ordered (Python 3.7+)
  #  student = {
  #      "name": "Anurag",
  #      "age": 25,
  #      "branch": "ECE"
  #  }
  # print(student["name"]) >>> This will print "Anurag"
  # Modify: student["name"] = "Rajan"
  # Add : student["RollNumber"] = 24
  # Looping through Dictionary:  for key , value in student.items():  >>> here for look iterating element is key,value
  #                                 print(key, ":", value)




##job requirement
jobs = {
        "JOB-1": 10,
        "JOB-2": 15,
        "JOB-3": 20,
        "JOB-4": 5
}

##Machine capacities
machine = {
  "machine-1": 20,
  "machine-2": 15
}

 for i in len(jobs)
    for j in len(jobs)
        if j > i : comb2[i][j] = jobs[i]+jobs[j]

 for i in len(jobs)
    for j in len(jobs)
        if i != j : comb3[i][j] = jobs[i]+jobs[j]
     
##Creating List for machine 1 and machine 2 seperately
machine_1 = [] ##Empty List
machine_2 = [] ##Empty List

m1_used = 0
m2_used = 0
sort_jobs = sort(jobs.items()}

for i in (len(jobs)):
    if(i + m1_used < machine.machine-1()):
            machine_1.append(i)
            m1_used+=i
    elif 


#####Combination Functions
## for combo in combinations(jobs, 2)  >>> Gives you combination of jobe in pair of 2

for r in range(1, len(jobs) + 1):
    for combo in combinations(jobs, r):








                 
   
  
