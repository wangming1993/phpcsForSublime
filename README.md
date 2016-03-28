# Sublime Text 3集成 php-cs-fixer

## php-cs-fixer
> https://github.com/FriendsOfPHP/PHP-CS-Fixer

Analyzes some PHP source code and tries to fix coding standards issues (PSR-1 and PSR-2 compatible) http://cs.sensiolabs.org

意思就是可以按照 *PSR-1* 或 *PSR-2* 规范修复你的php代码规范问题

### 安装
1. [下载](http://get.sensiolabs.org/php-cs-fixer.phar)
2. 修改权限, 变成可执行文件

```
sudo mv php-cs-fixer.phar /usr/local/bin/phpcs
sudo chmod +x /usr/local/bin/phpcs
```

### 测试安装

在终端输入:

```
phpcs
```

显示:
```
Usage:
  help [options] [--] [<command_name>]
```

则表明anything OK

## 集成sublime插件

1. 找到你的*sublime text 3* package位置, 可以通过:
`Preferences` > `Browse Packages`, 在打开的文件夹中可以看到当前的文件路径,

```
/home/user/.config/sublime-text-3/Packages/
```
2. 在package目录下面新建一个文件夹, 如: *Mike*,
```
/home/user/.config/sublime-text-3/Packages/Mike
```
3. 拷贝全部文件到 *Mike*

## 特别说明

因为考虑到以前代码并没有完全遵从规范, 所以把文件保存时自动修复代码问题的功能注释掉了, 如果此功能, 可以注释回来:
找到文件: `phpcs.py`, 将第21行的注释取消掉即可.
