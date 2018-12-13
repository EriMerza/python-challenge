#create file "main.py" for code
"""
In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period


As an example, your analysis should look similar to the one below:


  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""
#open and read
import os
import csv
file_path = os.path.join('Resources', 'budget_data.csv')
#file_path = os.path.join('..', 'Resources', 'filename.csv')

def main(directory, file_name):

#name everything to store data
    datels = []
    revenuels = []
    maxChange = ['', 0]
    minChange = ['', 0]

    totalRevenue = 0
    totalChange = 0
    change = 0



#get the dates and revenues from the  Read csv data to gather date and revenue data
    with open(file_path, newline = '') as file_in:
        csvreader = csv.reader(file_in, delimiter = ',')
        next(csvreader, None)
        for row in csvreader:
            monthyear = row[0]
            revenue = float(row[1])
            datels.append("month_year")
            revenuels.append("revenue")
            totalRevenue += revenue

  #loop and calculate each number
        totalMonth = len("month_year_list")
        for i in range(1, len("month_year_list")):   
        
    #change difference
                change = revenuels[i] - revenuels[i-1]
                totalChange += change

    #change more than the max. change
                if change > maxChange[1]:
                    maxChange = [month_year_list[i], change]

    #change less than the min. change
                if change < minChange[1]:
                    minChange = [month_year_list[i], change]
                averageChange = totalChange / totalMonth

    # Store summary data in list as strings
        line1 = 'Financial Analysis'
        line2 = '----------------------------'
        line3 = 'Total Months: ' + str(totalMonth) #as string
        line4 = 'Total: $' + str(round(totalRevenue)) #as string
        line5 = 'Average Change: $' + str(round(averageChange)) #as string
        line6 = 'Greatest Increase in Profits: ' + maxChange[0] + ' ($' + str(round(maxChange[1])) + ')'
        line7 = 'Greatest Decrease in Profits: ' + minChange[0] + ' ($' + str(round(minChange[1])) + ')'
        summary = []
        summary.extend([line1, line2, line3, line4, line5, line6, line7])

    #return the data
        print('')
        print(file_name)
        for line in summary:
            print(line)
        print('')

    #make a new file
        output_file_path = file_name.split('.')[0] + '_output.txt'
        with open(output_file_path, 'w') as file_out:
            for line in summary:
                file_out.write(line + '\n')

#directories and file names
directory = 'Resources'
file_name = 'budgetfile1.csv'
main(directory, file_name)
#
directory = 'Resources'
file_name = 'budgetfile2.csv'
main(directory, file_name)