# leetcode

## 如何协作

### 1. 克隆到本地

在 Terminal 

- 克隆开发分支到本地

  ```bash
  # clone repo to ~/Documents/GitHub, or choose any folder you like
  cd ~/Documents/Github 
  git clone -b dev-v0.1.0 https://github.com/Lijiachen1018/leetcode.git
  cd leetcode
  ```

- 从开发分支新建你的开发分支

  ```bash
  # create a new branch of your own, replace <your-branch-name> by a name you like
  # eg. "git branch jiachen dev-v0.1.0"
  git branch <your-branch-name> dev-v0.1.0
  
  # switch between branches, eg. git 
  git checkout <branch-name>
  ```

- 常用操作

  ```bash
  # 查看当前所在分支，文件修改
  git status
  >>> On branch jiachen
      Changes not staged for commit:
          modified:   README.md
  
  # 取消修改
  git checkout -- <file>
  
  # 取消已经 commit 的文件
  git rm --cached <file>
  
  # 取消已经 commit 的文件夹
  git rm -rf --cached <file>
  ```

- 提交修改

  ```bash
  git add .
  git commit -m "Message" # Message 中简单介绍修改的内容，不要用无意义的信息
  git push origin <your-branch-name>
  ```

- 提交 pull Request

## Repo 结构

​	

## 代码规范

### Python

[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

