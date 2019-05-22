var http = require('http')

const server = http.createServer(function(req, res) {
	console.log('res: ', res)

	res.writeHead(200, {
		'Content-Type': 'text/html'
	})

	res.end('<h1 style="color: red">Hello world.<h1>')
})

server.listen(8888, function() {
	console.log('Server is listening on 8888.')
})
