import web
from operator import index
render= web.template.render("templates")
urls = (
    '/', 'index',
    '/ubuntu','ubuntu',
    '/docker','docker',


)
app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index()

class ubuntu:
    def GET(self):
        return render.ubuntu()

class docker:
    def GET(self):
        return render.docker()



if __name__ == "__main__":
    app.run()