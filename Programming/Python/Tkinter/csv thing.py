import csv
csv_file = open('emailstorage2.csv', mode='r')
csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
	print(row['Email'])

csv_file = open('emailstorage2.csv', mode='a')
csv_writer = csv.writer(csv_file, skipinitialspace=True)
csv_writer.writerow({'hatdog123@gmail.com','lmao123','TestFile'})
csv_writer.writerow({'hatdog123@gmail.com','lmao123','TestFile'})



csv_file = open('emailstorage2.csv', mode='r')
csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
for row in csv_reader:
	print(row['Email'])