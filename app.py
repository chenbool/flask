# -*- coding: utf-8 -*-  
from flask import Flask,jsonify,request,render_template
from ext.qzone import Qzone
from ext.tieba import Tieba

app = Flask(__name__)

@app.route('/')
def index():
	# 返回json
    # return jsonify({'id':1})
     return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'

@app.route('/qzone', methods=['POST'])
def qzone():
	try:
		# 获取post提交的参数
		data = request.form.to_dict()
		qzone = Qzone(data['qq'],data['password'],data['content'])
		qzone.login()
	except Exception as e:
		return jsonify({'msg':e})
	finally:
		return jsonify({'msg':'正在运行'})

@app.route('/tieba/<username>/<password>/', methods=['GET', 'POST'])
def tieba(username,password):
	try:
		tieba = Tieba(username,password)
		tieba.login()
	except Exception as e:
		return jsonify({'msg':e})
	finally:
		return jsonify({'msg':'正在运行'})

if __name__ == '__main__':
    app.debug = True
    app.run()