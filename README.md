# SSH-keeper
Easy access to SSH connections.


##### INSTALL

* `git clone https://github.com/klem4/SSH-keeper.git`
* `cd SSH-keeper/`
* `sudo make`


##### UNINSTALL
* `sudo make clean`


##### ADDING HOSTS
$ s
* Database is empty
$ s sq@10.1.29.4
* No candidates found for sq@10.1.29.4, save and connect ? [y/N] y
Description(empty by default): sphinx-server ss3

now server added with credentails "sq@10.1.29.4" and description "sphinx-server ss3"

##### LIST AND CONNECT TO HOSTS

$ s
1). sq@10.1.29.4(sphinx-server ss3)
Choose: 1
Password:
Last login: Tue May 31 20:30:21 2016 from 10.18.0.26
FreeBSD 9.1-RELEASE-p3 (GENERIC) #0: Mon Apr 29 18:27:25 UTC 2013

Welcome to FreeBSD!

[sq@ss-3 ~]$
[sq@ss-3 ~]$ ^C
[sq@ss-3 ~]$ logout
Connection to 10.1.29.4 closed.
