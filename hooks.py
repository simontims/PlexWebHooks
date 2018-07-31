import web
import json

urls = ('/.*', 'hooks')
app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print data.decode('utf-8')
        print 'Converting data to Python'
        jsonToPython = json.loads(data)
        print 'Done conversion'
        print jsonToPython
        return 'OK'

if __name__ == '__main__':
    app.run()