import web
urls = (
    'v1/Scenario/', 'scenario'
)

class scenario:
    def GET(self,name):
        value = web.input()
        scenarios = value.name.split('|')
	for scene in scenarios:	    
	    if value.name == 'fun':
                return ['xiaobiaoza','faint']
            else:
                return 'default'

app = web.application(urls, globals())
application = app.wsgifunc()

