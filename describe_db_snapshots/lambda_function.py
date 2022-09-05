import boto3
from botocore.client import ClientError

rds = boto3.client('rds')

def describe_snapshots(instanceid):
	snapshots = rds.describe_db_snapshots(
			DBInstanceIdentifier=instanceid, SnapshotType='manual')['DBSnapshots']
	snapshots = sorted(
			snapshots, key=lambda x: x['SnapshotCreateTime'], reverse=True)

	return snapshots

def lambda_handler(event, context):
	instance = [RDSのインスタンス名]
	describe_snapshots(instance)
