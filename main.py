import webapp2
import jinja2
import os

the_jinja_enviroment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_enviroment.get_template('static/html/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
