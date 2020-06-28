from flask import Flask, url_for, render_template, request
#Falsk 객체 할당 <- 모든 것의 시작
app = Flask(__name__)


@app.route('/') # route 주소 할당
def hello_world() : # view 함수 실행
    return '<h1>Hellow World!</h1>' # html 구문 실행, 그냥 text도 가능....

@app.route('/render_html/')
def template_html() :
    return render_template('home.html')

@app.route('/html/')
def view_html_script() :
    my_html = """
    <!doctype html>
    <html>
        <head>
            <title>Hellow HTML</title>
        </head>
        <body>
            <form>
                <p>p안녕하세요~~ <input type="text" id="input_text"></p>
                <a>a안녕하세요!!</a>
                <p>pb안녕하세요~~</p><br>
                <a>ab안녕하세요!! <input type="button" id="input_button"
                value="제출" onclick="alert('제출 완료')"></a><br>
                <a>a안녕하세요!!</a>
            </form>
        </body>
    </html>
    """
    return my_html

@app.route('/<a>/<b>/') # url 동적 할당 <변수> <- 아무거나 가능 
def abc(a, b) : # 동적할당에 쓰인 변수를 가져와서 본문에 쓴다.
    return a + b

@app.route('/pow/<int:num>/') # <타입:변수>, 띄어쓰기 불가 <int : num> <- ERROR
def my_pow(num) : # 동적할당에 쓰인 변수를 가져와서 본문에 쓴다.
    return '%d'%(num * num)

@app.route('/get/') 
def my_get() :
    name = request.args.get('name', 'user01')
    juso = request.args.get('juso', 'seongnam')
    age = request.args.get('age', '24')

    return '<h1>{} - {} - {}</h1>'.format(name, juso, age)

@app.route('/post/', methods=['POST', 'GET'])
def my_post() :
    print(request.method)
    if request.method == 'GET' :
        return render_template('post.html')
    if request.method == 'POST' :
        value = request.form['input_name']
        return render_template('post_output.html', name=value)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='') :
    return render_template('hello.html', name=name)

if __name__ == '__main__' :
    with app.test_request_context() :
        print(url_for('abc', a = '1', b = '2'))
    app.run(port=8022, debug=True)