# Flask 扩展模块

扩展模块目录，包含 QQ空间 和 百度贴吧 自动化签到类。

## 模块说明

| 文件 | 类名 | 功能 |
|------|------|------|
| `qzone.py` | `Qzone` | QQ空间自动登录和签到 |
| `tieba.py` | `Tieba` | 百度贴吧自动签到 |

## Qzone 类

QQ空间签到类，实现自动登录和签到功能。

### 方法

| 方法 | 说明 |
|------|------|
| `__init__(qq, password, content)` | 构造函数 |
| `login()` | 登录并执行签到 |
| `run()` | 执行签到操作 |

### 使用示例

```python
from ext.qzone import Qzone

qzone = Qzone('QQ号', '密码', '签到内容')
qzone.login()
```

## Tieba 类

百度贴吧签到类，实现自动登录和签到功能。

### 方法

| 方法 | 说明 |
|------|------|
| `__init__(username, password)` | 构造函数 |
| `login()` | 登录并执行签到 |

### 使用示例

```python
from ext.tieba import Tieba

tieba = Tieba('用户名', '密码')
tieba.login()
```

## 依赖

- Python 3.6+
- Selenium
- ChromeDriver

## 演示截图

| 截图1 | 截图2 | 截图3 |
|--------|--------|--------|
| ![截图1](./screenshot/30024167.png) | ![截图2](./screenshot/81001985.png) | ![截图3](./screenshot/81001985@qq.com.png) |
