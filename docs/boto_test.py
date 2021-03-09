import boto3
import logging

s3 = boto3.client('s3', endpoint_url='', aws_access_key_id='', aws_secret_access_key='')

BUCKET_NAME="demo_pred"

def create_bucket(bucket_name):
    try:
        res = s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
 
def delete_bucket(bucket_name):
    try:
        res = s3.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)



def make_object():
    try:
        # f = open("guru99.txt","w+")
        # for i in range(10):
        #     f.write("This is line %d\r\n" % (i+1))
        # f.close()
        f = open("guru99.txt","rb")
        s3.upload_fileobj(f, BUCKET_NAME, 'aaa/vvv.txt')
        f.close()
    except e:
        print('make_object error ' + e)

def download_object():
    # save to file
    # with open('output.txt', 'wb') as data:
    #     s3.download_fileobj(BUCKET_NAME, 'aaa/vvv.txt', data)
    response = s3.get_object(Bucket=BUCKET_NAME, Key='aaa/vvv.txt')
    data_str = response['Body'].read().decode('utf-8')
    print(data_str)

# create_bucket(BUCKET_NAME)
# delete_bucket(BUCKET_NAME)
# list_buckets()
# make_object()
# list_objects(BUCKET_NAME) # Emerson

download_object()

# s3.upload_file(PATH_TO_FILE, BUCKET_NAME, 'mykey')
# s3.upload_fileobj(FILE_OBJ, BUCKET_NAME, 'mykey')