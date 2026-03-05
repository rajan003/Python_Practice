##Empty Lis
## my_list = []  >> When you want to store items Dynamically >> Appemd values later 
## jobs = []

  ## jobs.append("JOB-1")
  ## jobs.append("JOB-2")
  ## print(jobs)

##Empty Tuple → ()
  ## my_tuple = ()  >> You cannot change it after creation.
  ## No use

## Empty Set
  ## my_set = set() >> NOT {} (that creates a dictionary!)
  ## signals = ["REQ", "ACK", "REQ"]
  ## unique_signals = set()

## Empty Dictionary
  ## my_dict = {}

  ##counts = {}
  ## counts["REQ"] = 1
  ## counts["ACK"] = 2
  ## >> {'REQ': 1, 'ACK': 2}

########% Mock Sample Problem #######
## ypu are given logs = ["ERROR", "INFO", "WARNING", "ERROR", "INFO", "ERROR"]
## Write a code to print 
  ## ERROR: 3
  ## INFO: 2
  ## WARNING: 1

logs = ["ERROR", "INFO", "WARNING", "ERROR", "INFO", "ERROR"]

log_f = {}
for log in logs
    if log in log_f
        log_f[log]+=1 
    else
        log_f[log]=1

## Given jobs = [4, 8, 12, 3, 7]
  ## limit = 15
  ## Fill the machine sequentially (in order).
  ## Add jobs until limit is exceeded.
  ## Stop when next job cannot fit.
jobs = [4,8,12,3,7]
limit = 15
machine = []

remaining = []
used = 0
for job in jobs 
   if used + job < limit
      machine.append("job")
   else remaining.append("job")


## Find Duplicate Signals
## signals = ["REQ", "ACK", "DATA", "REQ", "ACK", "VALID"]
## Print only the signals that appear more than once.

signal = ["REQ", "ACK", "DATA", "REQ", "ACK", "VALID"]
signal_list = []

for sig in signal: 
   if sig in signal_list:
     print(sig)
   else signal_list.append(sig)











