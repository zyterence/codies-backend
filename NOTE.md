### Tips
##### 1. 阿里云ECS在 root 上运行服务外网无法访问,需要新建用户。在安全组里添加规则，打开8000端口（或其他端口）。

##### 2. 需要通过守护进程运行服务，否则 ssh 连接断开或者关闭 terminal 服务进程也会终止。

##### 3. Tmux 
- 新建会话：`$ tmux new -s <session-name>`
- 分离会话：`$ tmux detach`
- 查看会话：`$ tmux ls`
- 接入会话：`$ tmux attach -t <session-name>`
- 杀死会话：`$ tmux kill-session -t <session-name>`
- 切换会话：`$ tmux switch -t <session-name>`
