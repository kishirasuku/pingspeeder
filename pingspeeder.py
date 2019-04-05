import commands

def main():
    print "how many count with ping?"
    times = input()
    print "where?"
    place = raw_input()
    sums=[]
    for i in range(times):
        answer=commands.getoutput("(ping -c 1 google.com|grep time=)|awk '{print $8}'")
        sums.append(float(answer[5:]))
    average=float(sum(sums)/times)
    with open("pingspeed.txt","a") as f:
        f.write("%s : %f \n" %(place,average))

if __name__ == '__main__':
    main()
    
