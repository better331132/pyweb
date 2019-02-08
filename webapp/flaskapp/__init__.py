from flask import Flask, g, make_response, Response

app = Flask(__name__)
app.debug = True 




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