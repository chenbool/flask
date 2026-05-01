# Flask 网站 Demo

基于 Flask 框架开发的 Web 应用，提供 QQ空间 和 百度贴吧 自动签到 API。

## 技术栈

| 分类 | 技术 |
|------|------|
| Web 框架 | Flask |
| 自动化 | Selenium |
| 浏览器驱动 | ChromeDriver |

## 项目结构

```
flask/
├── app.py              # Flask 主应用
├── chromedriver.exe   # Chrome 驱动
├── README.md          # 项目说明
├── ext/              # 扩展模块
│   ├── qzone.py      # QQ空间签到
│   ├── tieba.py      # 百度贴吧签到
│   └── chromedriver.exe
├── templates/        # 模板目录
│   └── index.html    # 首页模板
└── screenshot/       # 演示截图
```

## 功能接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 首页 |
| `/login` | GET/POST | 登录接口 |
| `/qzone` | POST | QQ空间签到 |
| `/tieba/<username>/<password>/` | GET/POST | 百度贴吧签到 |

## 快速开始

### 1. 环境要求

- Python 3.6+
- Flask
- Selenium
- Chrome 浏览器

### 2. 安装依赖

```bash
pip install flask selenium
```

### 3. 启动服务

```bash
python app.py
```

### 4. 访问应用

浏览器访问：`http://127.0.0.1:5000/`

## API 使用示例

### QQ空间签到

```bash
curl -X POST http://127.0.0.1:5000/qzone \
  -d "qq=your_qq&password=your_password&content=签到内容"
```

### 百度贴吧签到

```bash
curl http://127.0.0.1:5000/tieba/username/password/
```

## 注意事项

1. 需要下载对应版本的 ChromeDriver
2. 请妥善保管账号密码
3. 建议适当添加延迟避免频繁操作
4. 请遵守各平台服务条款
