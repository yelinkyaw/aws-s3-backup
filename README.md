AWS S3 Backup
===================
Simple python script to backup the list of local files to S3.
It can be executed from crontab for automated snapshot.

Requirements
===================
1. Python 2.7 and later
2. Boto 2.9 and later

Configurations
===================
1. Update aws_access_key and aws_secret_key
2. Update bucket_name to store backup file
3. Update bucket_location
4. Update backup.conf