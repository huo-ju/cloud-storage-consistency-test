import time
import sys 
import os 
import hashlib

if __name__ == '__main__' :
    if len(sys.argv) < 2 :
        print 'Usage: ' + sys.argv[0] + ' cmd [path] [num] [size(k)]'
    else :
        cmd = sys.argv[1]
        path = "test"
        if len(sys.argv)>=3:
            path=sys.argv[2]
        if cmd=="create": 
            num = 500
            size = 1
            if len(sys.argv)>=4:
                num=sys.argv[3]
            if len(sys.argv)>=5:
                size=sys.argv[4]
            if not os.path.exists(path):
                os.makedirs(path)
            start = time.time()
            for idx in range(0,int(num)):
                f = open(path+"/test_"+str(idx)+".txt","w")
                for line in range(0,105*int(size)):
                    f.write(str(idx)+" "+str(line)+" line\n")  
                f.close()
            end = time.time()
            during = end - start
            print "create "+num+" file(s), time:"+str(during)+"(seconds)"
            exit(0)

        elif cmd=="compare":
            path1=""
            if len(sys.argv)>=4:
                path1=sys.argv[3]
            else:
                print "need two paths for compare."
                exit(1)
            num = 500
            if len(sys.argv)>=5:
                num=sys.argv[4]
            start = time.time()
            equal_num=0
            for idx in range(0,int(num)):
                f_path = open(path+"/test_"+str(idx)+".txt","r")
                data_path = f_path.read()

                try:
                    filename = path1+"/test_"+str(idx)+".txt"
                    f_path1 = open(filename,"r")
                    data_path1 = f_path1.read()
                    if hashlib.sha224(data_path).hexdigest() == hashlib.sha224(data_path1).hexdigest():
                        equal_num+=1
                except IOError as e:
                    print filename+":file not exist"
            end = time.time()
            during = end - start
            equal_rate=float(equal_num)/int(num)*100
            print "compare "+num+" file(s), equal: "+str(equal_rate)+"% time:"+str(during)+"(seconds)"
            exit(0)
