sudo yum update -y
sudo yum install git -y

git clone https://github.com/data-engineering-jigsaw/prefect-deployments-code.git


* sudo yum install python3 -y
* curl -O https://bootstrap.pypa.io/get-pip.py
* python3 get-pip.py --user

pip3 install prefect
pip3 install requests

prefect auth login --key YOUR_API_KEY
