import threading

smb = [0, 1]
i = smb[0]-1

def work ():
    global i
    i += 1
    a = threading.Timer(0.25, work)
    a.start ()
    print "stackoverflow", i
    if i == 5:
        print 'canceling at', i
        a.cancel()
        print 'stopped'

work ()