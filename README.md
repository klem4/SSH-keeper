# SSH-keeper
Easy access to SSH connections.


##### INSTALL

* `git clone https://github.com/klem4/SSH-keeper.git`
* `cd SSH-keeper/`
* `sudo make`


##### UNINSTALL
* `sudo make clean`

##### ADDING HOSTS
```
klem4@work:~$ s
* Database is empty
klem4@work:~$ s sq@10.1.29.4
* No candidates found for sq@10.1.29.4, save and connect ? [y/N] y
Description(empty by default): sphinx ss-3 server
Password:
Last login: Tue May 31 20:32:30 2016 from 10.18.0.26
FreeBSD 9.1-RELEASE-p3 (GENERIC) #0: Mon Apr 29 18:27:25 UTC 2013

Welcome to FreeBSD!

[sq@ss-3 ~]$ logout
Connection to 10.1.29.4 closed.
klem4@work:~$ 
```

