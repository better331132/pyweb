from flask import Flask, g, make_response, Response, request, session, render_template, Markup
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.debug = True 
app.secret_key = 'X1243yRH!mMwf'

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route("/tmpl")
def t():
    tit = Markup("<b>%s</b>")
    k = tit % "Title"
    lst = [ ("만남1", "김건모", False), ("만남2", "노사연", False),("만남3", "깅건모", True), ("만남4", "농사연", False),("만남5", "김건몽", True), ("만남6", "노상연", False)]
    a = ("만남1", "김건모", False, [])
    b = ("만남2", "노사연", False, [a])
    c = ("만남3", "깅건모", True, [b])
    d = ("만남4", "농사연", False, [c])
    e = ("만남5", "김건몽", True, [d])
    f = ("만남6", "노상연", False, [e])
    return render_template('index.html', title=Markup(k), lst=lst, lst2=[a,b,c,d,e,f])

@app.route("/trythis")
def categs():
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1))


@app.route("/trythis/programlanguage/<programlanguage>")
def python(programlanguage):
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    h3 = Markup("<a href='http://localhost:5000/trythis/programlanguage'>programlanguage</a>---<i>%s</i>") % programlanguage
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1), title=Markup(h3))

@app.route("/trythis/framework/<frw>")
def spring(frw):
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    h3 = Markup("<a href='http://localhost:5000/trythis/framework'>framework</a>---<i>%s</i>") % frw
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1), title=Markup(h3))

@app.route("/trythis/etc/<etc>")
def daily(etc):
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    h3 = Markup("<a href='http://localhost:5000/trythis/etc'>etc</a>---<i>%s</i>") % etc
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1), title=Markup(h3))

@app.route("/trythis/framework/flask/<flask>")
def jinja(flask):
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    h3 = Markup("<a href='http://localhost:5000/trythis/framework'>framework</a>---<a href='http://localhost:5000/trythis/framework/flask'>flask</a>---<i>%s</i>") % flask
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1), title=Markup(h3))

@app.route("/trythis/<trythis>")
def programlanguage(trythis):
    D=("파이썬",2,[], "http://localhost:5000/trythis/programlanguage/python" )
    E=("자바",2,[], "http://localhost:5000/trythis/programlanguage/java" )
    G=("스프링",2,[], "http://localhost:5000/trythis/framework/spring" )
    H=("노드js",2,[], "http://localhost:5000/trythis/framework/nodejs" )
    I=("나의 일상",2,[], "http://localhost:5000/trythis/etc/daily" )
    J=("이슈 게시판",2,[], "http://localhost:5000/trythis/etc/issue")
    K=("Jinja",3,[], "http://localhost:5000/trythis/framework/flask/jinja" )
    L=("Genshi, cheetah",3,[], "http://localhost:5000/trythis/framework/flask/genshi" )
    A=("프로그래밍 언어",1,[D,E], "http://localhost:5000/trythis/programlanguage" )
    F=("플라스크",2,[K,L], "http://localhost:5000/trythis/framework/flask" )
    B=("웹 프레임워크",1,[F,G,H], "http://localhost:5000/trythis/framework" )
    C=("기타",1,[I,J], "http://localhost:5000/trythis/etc" )
    h1 = Markup("<b>%s</b>") % "목록"
    h3 = Markup("<i>%s</i>") % trythis
    return render_template('trythis.html', lst=[A,B,C], category=Markup(h1), title=Markup(h3))


# {% for title, name in lst %}
#     <li>{{title}}: {{name}}</li>
# {% endfor %}



@app.route('/setsess')
def setsess():
    session['Token'] = '123X'
    return "Session이 설정되었습니다!"

@app.route('/getsess')
def getsess():
    return session.get('Token')

@app.route('/delsess')
def delsess():
    if session.get('Token'):
        del session['Token']
    return "Session이 삭제되었습니다!"


@app.route('/dat')
def dat():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 날짜 형식: " + str(datestr)

@app.route('/reqenv')
def reqenv():
    print(request.is_xhr, request.endpoint, request.get_json())
    return ('REQUEST_METHOD: %(REQUEST_METHOD)s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME)s <br>'
        'PATH_INFO: %(PATH_INFO)s <br>'
        'QUERY_STRING: %(QUERY_STRING)s <br>'
        'SERVER_NAME: %(SERVER_NAME)s <br>'
        'SERVER_PORT: %(SERVER_PORT)s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL)s <br>'
        'wsgi.version: %(wsgi.version)s <br>'
        'wsgi.url_scheme: %(wsgi.url_scheme)s <br>'
        'wsgi.input: %(wsgi.input)s <br>'
        'wsgi.errors: %(wsgi.errors)s <br>'
        'wsgi.multithread: %(wsgi.multithread)s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess)s <br>'
        'wsgi.run_once: %(wsgi.run_once)s') % request.environ

@app.route('/wc')
def wc():
    res = Response("Set Cookie Complete")
    key = request.args.get('key', 'UserToken', type=str) # get방식이므로 args, (values도 무방)
    val = request.args.get('val', '000000', type=str) # get방식이므로 args, (values도 무방)
    res.set_cookie(key, val)
    return make_response(res)

@app.route('/rc')
def rc():
    key = request.values.get('key', 'UserToken', type=str)
    rcut = request.cookies.get(key, 'default token')
    return rcut

# @app.route('/dt')
# def dt():
#     dtstr = request.values.get('datetime', datetime.datetime(), type=ymd('%Y-%m-%d, %H:%M:%S'))
#     return "우리나라 날짜시간" + str(dtstr)



# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Flask World!!"

@app.route('/res1')
def res():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'), 
					('Content-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)

@app.route('/test/<tid>')
def test3(tid):
    return "tid is %s" % tid

@app.route('/test1', defaults={'page': 'index'})
@app.route('/test1/<page>')
def xxx(page):
    return "page is %s" % page