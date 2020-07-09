from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 파일 업로드 용량 제한 단위 : 바이트

#HTML 랜더링
@app.route('/')
def home_page() :
    return render_template('home.html')

#파일 리스트
@app.route('/list')
def list_page() :
    file_list = os.listdir("./uploads")
    html = """<a style="text-align: center; display:block;" href="/">홈페이지</a><br><br>"""
    html += """<a style="text-align: center; display:block;"> file_list: {}</a>""".format(file_list)
    return html

#업로드 HTML 렌더링
@app.route('/upload')
def upload_page() :
    return render_template('upload.html', type='Up')

@app.route('/down')
def download_page() :
    return render_template('upload.html', type='Down')

#파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file() :
    if request.method == 'POST' :
        f = request.files['file']
        #저장한 경로 + 파일명
        f.save('./uploads/' + secure_filename(f.filename))
        print(request)
        return render_template('check.html')

# 서버 실행
if __name__ == '__main__' :
    app.run(port=8080, debug=True)
