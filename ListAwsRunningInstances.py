import argparse
import boto.ec2
from pprint import pprint
from boto import ec2

access_key = ''
secret_key = ''

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    reservations = ec2_conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    for reservation in reservations:
         for instances in reservation.instances:
              if instances.state == "running":
                   print "%s \t \t %s" % (instances.tags['Name'], instances.private_ip_address) 

def main():
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    parser = argparse.ArgumentParser()
    parser.add_argument('access_key', help='Access Key');
    parser.add_argument('secret_key', help='Secret Key');
    args = parser.parse_args()
    global access_key
    global secret_key
    access_key = args.access_key
    secret_key = args.secret_key
    
    for region in regions: get_ec2_instances(region)

if  __name__ =='__main__':main()
