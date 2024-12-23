from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Shipin():
    a = request.form.get('Input')
    if a:  # 检查a是否有内容
        return redirect(f'https://www.8090g.cn/?url={a}')  # 使用redirect实现页面跳转
    return render_template('Input.html')

if __name__ == '__main__':
    app.run()
