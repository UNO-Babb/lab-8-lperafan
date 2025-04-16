#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data [1]
    idNum = data[3]
    year = data[5]

    major = ' '.join(data[6:])

    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major, year)
    output = last + ", " + first + ", " + student_id + ", " + major_year + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]
  return id

def makeMajorYear(major, year):
    if len(major) >= 3:
      major_abbr = major[:3].upper()
    else:
      major_abbr = major.upper()

    if year.lower() == "freshman":
      year_abbr = "FR"
    elif year.lower() == "sophomore":
      year_abbr = "SO"
    elif year.lower() == "junior":
      year_abbr = "JR"
    elif year.lower() == "senior":
      year_abbr = "SR"
    else:
      year_abbr = "NA"

    return major_abbr + "-" + year_abbr


if __name__ == '__main__':
  main()
