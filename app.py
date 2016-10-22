from collections import defaultdict
import web
from jinja2 import Environment
from jinja2.loaders import DictLoader
env = Environment(loader=DictLoader({
'child.html': u'''\

<html>
<head>
    <script src='jquery.js'></script>
    <script src='bootstrap?path=js'></script>
    <link href="bootstrap?path=css" rel="stylesheet" />
</head>

<body>
<script src='align.js'></script>

    Hello world {{name}}
    
    <button class='btn btn-primary'>HELLO</button>
    <div id='divText'>
        Text
    </div>
</body>
</html>

''',

'align.js' : open("align.js").read(),
'jquery.js' : open("jquery.js").read(),
'bootstrap.js': open("bootstrap.min.js").read(),
'bootstrap.css' : open("bootstrap.min.css").read()

}))

#hello
tmpl = env.get_template("child.html")
jsscript = env.get_template("align.js")
jquery = env.get_template("jquery.js")

VERSION = "0.0.1"



urls = (
    r'/', 'Index',
    r'/align.js', 'AlignJS',
    r'/jquery.js','JqueryJS',
    r'/bootstrap','Bootstrap'
    )

app = web.application(urls, globals())

class Index:
	#http://localhost:8080/?id=John
    def GET(self):
		user_data = web.input(id="no data")
		name = user_data.id
		return tmpl.render({"name" : name})

class AlignJS:
    def GET(self):
        return jsscript.render() 
    
class JqueryJS:    
    def GET(self):
        return jquery.render()

class Bootstrap:
    def GET(self):
        _get = web.input(path="")
        if _get.path == "css":
            return env.get_template("bootstrap.css").render()
        elif _get.path == "js":
            return env.get_template("bootstrap.js").render()

application = app.wsgifunc()
if __name__ == "__main__":
    app.run()
