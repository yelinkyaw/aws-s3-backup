#!/usr/bin/env python
import tarfile
import datetime
import tempfile
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

# AWS Constants
aws_access_key = 'AWS Access Key'
aws_secret_key = 'AWS Secret Key'
bucket_name = 'Bucket Name'
bucket_location = 'backup'

# Current Datetime 
now = datetime.datetime.now()

# Temp Archvie
temp_directory = tempfile.gettempdir()

# Get Config File Path
config_directory = os.path.dirname(os.path.dirname(__file__)
config_file = os.path.join(config_directory, 'backup.conf')

# Get List to Archive
lines = [line.strip() for line in open(config_file)]

# Starting Backup
print 'Starting Backup'
for line in lines:
	if os.path.isfile(line) or os.path.isdir(line):
		# Archive
		source_full_path = line
		source_directory_name = os.path.basename(source_full_path)
		print 'Start Archiving ' + source_full_path
		archive_file_name = source_directory_name + '-repos-backup-' + now.strftime('%d-%m-%Y') + '.tar.gz'
		archive_full_path = os.path.join(temp_directory, archive_file_name)
		print 'Archiving finish'
		# Create Archive
		tar = tarfile.open( archive_full_path , 'w:gz')
		tar.add(source_full_path, arcname=source_directory_name)
		tar.close()
		# Accessing S3
		con = S3Connection(aws_access_key, aws_secret_key)
		bucket = con.get_bucket(bucket_name)
		object = Key(bucket)
		object.key = os.path.join(bucket_location, archive_file_name)
		print 'Uploading ' + archive_file_name + ' to ' + bucket_name + '/' + bucket_location
		object.set_contents_from_filename(archive_full_path)
		print 'Uploading finish'
		# Clear Temp File
		os.remove(archive_full_path)
	else:
		# Invalid Path
		print 'Invalid archive path'
print 'Finish Backup'
