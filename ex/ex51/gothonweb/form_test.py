import web

urls = (
  '/hello', 'index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()

