import time
def countdown(t):
    while t:
        mins,sec = divmod(t, 60)
        timer= '{:02d}:{:02d}'.format(mins,sec)
        print(timer)
        time.sleep(1)
        t=t-1
    print("finished")
t =input("Enter the time in seconds:")
countdown(int(t))

OUTPUT:
Enter the time in seconds:120
02:00
01:59
01:58
01:57
01:56
01:55
01:54
01:53
01:52
01:51
01:50
01:49
01:48
01:47
01:46
01:45
01:44
01:43
01:42
01:41
01:40
01:39
01:38
01:37
01:36
01:35
01:34
01:33
01:32
01:31
01:30
01:29
01:28
01:27
01:26
01:25
01:24
01:23
01:22
01:21
01:20
01:19
01:18
01:17
01:16
01:15
01:14
01:13
01:12
01:11
01:10
01:09
01:08
01:07
01:06
01:05
01:04
01:03
01:02
01:01
01:00
00:59
00:58
00:57
00:56
00:55
00:54
00:53
00:52
00:51
00:50
00:49
00:48
00:47
00:46
00:45
00:44
00:43
00:42
00:41
00:40
00:39
00:38
00:37
00:36
00:35
00:34
00:33
00:32
00:31
00:30
00:29
00:28
00:27
00:26
00:25
00:24
00:23
00:22
00:21
00:20
00:19
00:18
00:17
00:16
00:15
00:14
00:13
00:12
00:11
00:10
00:09
00:08
00:07
00:06
00:05
00:04
00:03
00:02
00:01
finished
