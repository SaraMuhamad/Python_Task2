import argparse
import os
from subprocess import PIPE, Popen
from os.path import isfile, join
from os import listdir
import json 
import pandas as pd 
from pandas.io.json import json_normalize
from urllib.parse import urlparse
from datetime import datetime
import time
from pathlib import Path

import sys

def main():
    print(sys.argv[0])
    print(sys.argv[1])


if __name__ == '__main__':
    main()

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("Path",help="Enter the path that contains the files")
parser.add_argument("-u", "--unix", action="store_true", dest="unix", default=False,
                    help="UNIX format of timestamp")
#parse args         
args = parser.parse_args()
#change dir to the one given by user as args 
os.chdir(args.Path)           
# check duplicate                   
files = [item for item in listdir('.') if isfile(join('.', item))]
checksums = {}
duplicates = []
for filename in files:
    with Popen(["md5sum", filename], stdout=PIPE) as proc:
        checksum = proc.stdout.read().split()[0]
        if checksum in checksums:
            duplicates.append(filename)
        checksums[checksum] = filename
#remove duplicated files        
for filename in duplicates:
	os.remove(filename)
print(f"Found Duplicates: {duplicates}")
files=[item for item in listdir('.') if isfile(join('.', item))]

#transformation
p = Path('Result')
p.mkdir(exist_ok = True)

for file_name in files:
	if 'done' not in file_name:
		records = [json.loads(line) for line in open(file_name) if '_heartbeat_' not in json.loads(line)]
		df = json_normalize(records)


		df['web_browser'] = df['a'].str.split('(').str[0]
		df['operating_sys'] = df['a'].str.split('(').str[1].str.split(')').str[1]

		df['from_url'] =df.apply(lambda row: urlparse(row['r']).netloc if 'http' in row['r'] else row['r'] , axis = 1)
		df['to_url'] = df.apply(lambda row: urlparse(row['u']).netloc  if 'http' in row['u'] else row['u'] , axis = 1)

		df2 = df['ll'].apply(pd.Series)
		df2.columns = ['longitude','latitude']

		if args.unix:
    			df['time_in'] = df['t']
    			df['time_out'] = df['hc']
		else:
			df['time_in'] = pd.to_datetime(df['t'],unit='s')
			df['time_out'] = pd.to_datetime(df['hc'],unit='ms')
		
    
		df['time_zone'] = df['tz']
		df['city'] = df['cy']

		df=df[['web_browser','operating_sys','from_url','to_url','city',
		'time_zone','time_in','time_out']]
		df3=pd.concat([df[:], df2[:]], axis=1)
		df3=df3.dropna()
	
		# computing number of rows
		rows = len(df3.axes[0])
  

		df3.to_csv(args.Path+'/Result/'+file_name.split('.j')[0]+'.csv', index=False)
	
		print("Number of Rows in file "+file_name.split('.j')[0]+'.csv'+' =' , rows)
		print("File Path is : ",args.Path+'/Result')
	
		os.rename(file_name, 'done_'+file_name)
	

else:		
	print("there is no other files to be processed all files were successfuly done")
print("execution time = " ,time.time() - start_time, "seconds")
