import subprocess
subprocess.call(["aws", "s3", "mb", "s3://aws-lab-videos-your-name","--region","us-east-2"])
subprocess.call(["aws", "s3", "cp", "video.mp4","s3://aws-lab-videos-your-name/video.mp4"])
