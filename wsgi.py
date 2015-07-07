#!/usr/bin/python
import os
import olla

base = os.environ['OPENSHIFT_REPO_DIR'] + 'dicts/'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

def application(environ, start_response):

    ctype = 'text/plain'
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']

    if path == '/health':
        response_body = "1"
    elif path == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    elif path == '/dicts':
        response_body = olla.dicts(base)
    elif path == '/dict':
        query = environ['QUERY_STRING'].split('&')
        lang = query[0]
        if len(query) >= 3:
            wtypes = query[1]
            wtype = query[2]
            response_body = olla.get_dict(lang, wtypes, wtype, base)
        else:
            response_body = olla.get_dict(lang, wtypes=None,
                                          wtype=None, base=base)

    elif path == '/words':
        ctype = 'text/plain; charset=utf-8'
        query = environ['QUERY_STRING'].split('&')
        lang = query[0]
        response_body = olla.words(lang, base)

    elif path == '/word':
        ctype = 'text/plain; charset=utf-8'
        query = environ['QUERY_STRING'].split('&')

        word = int(query[0])
        dct = query[1:]

        response_body = olla.word(word, dct, base)

    elif path == '/translate':
        if method == 'GET':
            query = environ['QUERY_STRING'].split('&')

            word = int(query[0])
            src = query[1]
            dst = query[2:]

            response_body = olla.translate(word, src, dst, base)
            url = 'http://' + environ['SERVER_NAME']
            if environ['SERVER_PORT'] != '80':
               url += ':' + environ['SERVER_PORT']
        elif method == 'POST':
            try:
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
            except (TypeError, ValueError):
                request_body = "0"
            try:
                response_body = str(request_body)
            except:
                response_body = "error"
    elif path == '/api':        
        url = 'http://' + environ['SERVER_NAME']
        if environ['SERVER_PORT'] != '80':
           url += ':' + environ['SERVER_PORT']

        ctype = 'text/html'
        response_body = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Dictionary operations</title>

<body>
%s/dicts<br/>
%s/words?lang<br/>
%s/word?word_num&lang[&lang...]<br/>
%s/dict?lang[&types&type]<br/>
%s/translate?word&src_lang&dst_lang[&dst_lang...]<br/>
</body>
</html>''' % (url,url,url,url,url,url,url)
    else:
        url = 'http://' + environ['SERVER_NAME']
        if environ['SERVER_PORT'] != '80':
           url += ':' + environ['SERVER_PORT']
            
        types = {
            'html': 'text/html',
            'js': 'application/javascript',
            'css': 'text/css',
            'png': 'image/png',
            'gif': 'image/gif',
        }
        ctype = types.get(path.rsplit(".", 1)[-1], "text/html")
        try:
            f=open(os.environ['OPENSHIFT_REPO_DIR'] + 'webui/' + path,'r')
        except:
            f=open(os.environ['OPENSHIFT_REPO_DIR'] + 'webui/semes_form.html','r')
        response_body = ""
        for s in f.readlines():
           response_body += s


    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
