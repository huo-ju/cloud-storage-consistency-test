cloud-storage-consistency-test
==============================

a cmd script for test the file consistency on the cloud. It could be use for s3fs or other fuse based tool test.

Usage: cst.py cmd [path] [num] [size(k)]

1. create 50 files, size 10k test file in the /mnt/s3/test01 dir.(this dir has been mount to s3)
python cst.py create /mnt/s3/test01 50 10

create 50 file(s), time:6.90075492859(seconds)

2. create 50 files, size 10k test file in the test01 dir.(local disk)
python cst.py create test01 50 10

create 50 file(s), time:0.0640368461609(seconds)

3. compare the local dir and s3fs mount point
python cst.py compare test01 /mnt/s3/test01 10

compare 10 file(s), equal: 100.0% time:0.520743846893(seconds)

4. update local files to 15k
python cst.py create test01 50 15 

create 50 file(s), time:0.0967829227448(seconds)

5. update s3fs files to 15k
python cst.py create /mnt/s3/test01 50 15

create 50 file(s), time:7.60858488083(seconds)

6. compare files on test server B, all files update failure
python cst.py compare test01 /mnt/s3/test01 10

compare 10 file(s), equal: 0.0% time:0.741319894791(seconds)

