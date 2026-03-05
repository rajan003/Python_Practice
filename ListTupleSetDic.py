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

##Solve this on python:

##JOB-2: 15 GB
##JOB-3: 20GB
##JOB-4: 5GB

##The LSF has 2 mchines , with machine limit as

##machine-1: 20GB
##machine-2: 15GB

##4 jobs need tobe fit in LSF, you have to fit maximum job in first than move to another

jobs = {
    "JOB-2": 15,
    "JOB-3": 20,
    "JOB-4": 5,
    # If you really have JOB-1 too, add it here like: "JOB-1": 10
}

machines = {
    "machine-1": 20,
    "machine-2": 15
}

def pack_jobs_max_count_first(jobs, machines):  ## Defining a function arguments machine and jobs
    # Sort jobs by size ascending to maximize count on a machine
    remaining_jobs = sorted(jobs.items(), key=lambda kv: kv[1])  # (job, size)  Sorting the jobs as per the second value of each item

    allocation = {m: [] for m in machines}  ### Assigning an empty list to the machine at start 
    leftover = []  ## Emoty list to the Leftover

    for m, limit in machines.items():  ## Accesing the Machine items iwth (m, limit)== name of machine, its limit
        used = 0  ## A Variblae names used
        still_remaining = []  ## Varibal ename still remaining

        for job, size in remaining_jobs:
            if used + size <= limit:
                allocation[m].append((job, size))
                used += size
            else:
                still_remaining.append((job, size))

        remaining_jobs = still_remaining

    leftover = remaining_jobs
    return allocation, leftover

allocation, leftover = pack_jobs_max_count_first(jobs, machines)

# Pretty print
for m, items in allocation.items():
    used = sum(size for _, size in items)
    limit = machines[m]
    print(f"{m} ({used}/{limit} GB): {items}")

if leftover:
    print("Unscheduled:", leftover)
else:
    print("All jobs scheduled.")







                 
   
  
