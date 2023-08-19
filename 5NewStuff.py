
# @param: dictionary of probabilities
# @returns: entropy of one time step
def calcEntropy(probs: dict[str, float]) -> float:
    pass    # Nikhil

# @param: dictionary of probabilities
# @returns: relative entropy of one time step
def calcRelEntropy(probs1: dict[str, float], probs2: dict[str, float]) -> float:
    pass    # Nikhil

# @param: list of list of probabilities
#         Each item in outer list is one time step. 
#         Each item in inner list is prob of one node inside one time step
# @returns: list of entropies
#           Each item in list is entropy of one time step
def calcEntropies(probs: list[list[float]]) -> list[float]:
    pass  # Nikhil

# @param: list of list of probabilities
#         Each item in outer list is one time step.
#         Each item in inner list is prob of one node inside one time step
# @returns: list of relative entropies
#           Each item in list is relative entropy of one time step
def calcRelEntropies(probs1: list[list[float]], probs2: list[list[float]]) -> list[float]:
    pass  # Nikhil

# @param: filename of CSV file containing counts
#         CSV format is: each line is one time step
#                        each line has 16 numbers separated by commas, which are counts of each node  
# @returns: list of list of probabilities. 
#           Each item in outer list is one time step. 
#           Each item in inner list is prob of one node inside one time step
# divides the counts by 1024 to get probs
def parseCountsCSV(filename: str) -> list[list[float]]:
    pass    # Shivansh

# @param: list of entropies, where the index of the list is the time step
# line graphs the entropies with time on x-axis
def graphEntropies(entropies: list[float]) -> None:
    pass    # Shivansh

# @param: dictionary of counts
# writes the counts to a CSV file in a new line (append mode). Writes only the counts, not the keys
def writeCountsCSV(counts: dict[str, int]) -> None:
    pass    # Shivansh

# @param: time
# runs the quantum walk once
def runWalkOnce(time: int, backend) -> dict[str, int]:
    pass    # Sagnik

# runs the quantum walk for total time
# writes the counts to a CSV file in a new line (append mode). Writes only the counts, not the keys
def runWalk(startTime: int, endTime: int, backend) -> None:
    pass    # Sagnik

# run on simulator
# put the results into a csv file
# calculate entropy
# graph entropies with time on x-axis

# run on quantum computer
# put the results into a csv file
# calculate entropy
# graph entropies with time on x-axis

# calculate relative entropy - bw sim and quantum computer
# graph relative entropies with time on x-axis