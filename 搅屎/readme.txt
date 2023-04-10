对面脏掉了bash

简单绕过
bash -c "curl http://10.10.10.10/getFlag -o 1.txt" > a.txt

### 想法

1.对面可能是通过改变.bashrc实现的
shell在加载的时候会先执行.bashrc

2.后面拿到的shell可能就是被export污染的
后面拿到的shell通过使用bash -c 都无法绕过，系统环境变量应该是被污染了的
