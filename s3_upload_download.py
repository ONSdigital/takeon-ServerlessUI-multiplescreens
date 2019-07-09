import boto3


def download():
    # download files from s3
    s3 = boto3.resource('s3')
    s3.Bucket('multiple-screens').download_file('templates/index.html', 'tmp/myindex.html')
    s3.Bucket('multiple-screens').download_file('templates/name.html', 'tmp/myname.html')


def upload():
    # upload files to s3
    file = "templates/index.html"
    file2 = "templates/name.html"
    bucket_name = "multiple-screens"
    s3 = boto3.client("s3")
    s3.upload_file(file, bucket_name, file)
    s3.upload_file(file2, bucket_name, file2)


