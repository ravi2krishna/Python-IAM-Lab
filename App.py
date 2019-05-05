import subprocess
import urllib
urllib.urlretrieve("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4", filename="/home/ec2-user/video.mp4")
subprocess.call(["aws", "s3", "mb", "s3://aws-lab-videos-your-name","--region","us-east-2"])
subprocess.call(["aws", "s3", "cp", "video.mp4","s3://aws-lab-videos-your-name/video.mp4"])
