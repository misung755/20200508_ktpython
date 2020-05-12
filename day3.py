from flask import Flask, request

app = Flask(__name__)
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return "Welcome, Day 3 class"

# 사용자로부터 숫자를 N을 입력 받아서,
# *로 N줄의 트리를 만듭니다.
@app.route('/tree/<num>')
def tree(num):
    if not num.isnumeric():
        return "not number"

    # request.form 어제 배운거 html form으로 부터 받을 때,
    print(request.args.get('order'))

    trees = []
    if request.args.get('order') == 'desc':
        for i in range(int(num)):
            trees.append("*" * (int(num) - i))
    else:
        for i in range(int(num)):
            trees.append("*" * (i + 1))

    return '<br>'.join(trees)

app.run()