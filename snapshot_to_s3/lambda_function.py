import json
import boto3
import time
from botocore.client import ClientError
from datetime import datetime, timedelta, tzinfo

rds = boto3.client('rds')
s3 = boto3.resource('s3')
client = boto3.client('kms')

def export_snapshot(prefix, instanceid):
	snapshots = rds.describe_db_snapshots(
	DBInstanceIdentifier=instanceid, SnapshotType='manual')['DBSnapshots']
	snapshots = sorted(
	snapshots, key=lambda x: x['SnapshotCreateTime'], reverse=True)
	snapshot = snapshots[0]
	newsnapshotid = "-".join([prefix,datetime.now().strftime("%Y-%m-%d-%H-%M")])

	response = rds.start_export_task(
	ExportTaskIdentifier=newsnapshotid,
	SourceArn=snapshot['DBSnapshotArn'],
	S3BucketName=[S3のバケット名],
	IamRoleArn=[IAMロール]
	KmsKeyId=[KMSkey],
	S3Prefix=[S3に付けたいプレフィックス名],
	)
	return(response)


def lambda_handler(event, context):
	snapshot_prefix = [スナップショットのprefix名]
	instance = [RDSのインスタンス名]
	export_snapshot(snapshot_prefix, instance)
