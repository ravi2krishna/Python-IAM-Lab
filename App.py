import subprocess
import urllib
urllib.urlretrieve("https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4", filename="/home/ec2-user/video.mp4")
subprocess.call(["aws", "s3", "mb", "s3://aws-lab-videos-your-name","--region","us-east-2"])
subprocess.call(["aws", "s3", "cp", "/home/ec2-user/video.mp4","s3://aws-lab-videos-your-name/video.mp4"])
