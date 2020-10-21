import subprocess
import urllib
urllib.urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt", filename="/home/ec2-user/sample.txt")
subprocess.call(["aws", "s3", "mb", "s3://aws-lab-unique-bucket-name","--region","us-east-2"])
subprocess.call(["aws", "s3", "cp", "/home/ec2-user/sample.txt","s3://aws-lab-unique-bucket-name/sample.txt"])
