## read a CSV file from S3 and print the data in dataframe
'''
import pandas as pd
import boto3
import os
import sys
from io import StringIO

s3_client = boto3.client('s3')
s3_obj = s3_client.get_object(Bucket='vamsi-test-bucket-cli2', Key= 'tags.csv')
body = s3_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))
print(df)
'''
# read a CSV file from S3 and sort the rows based on field

import pandas as pd
import boto3
import os
import sys
from io import StringIO

s3_client=boto3.client('s3')
s3_obj=s3_client.get_object(Bucket='vamsi-test-bucket-cli2', Key='tags.csv')
body=s3_obj['Body']
csv_string=body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))

sorted_csv=df.sort_values(by=[movieId])
print(sorted_csv)

