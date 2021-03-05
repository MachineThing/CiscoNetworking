formatter = notebook.format.formatter()

formatter.append('p', 'How to make a RIP route on a router')
formatter.append('p', 'In this example, lets just say you want to make it so people (from an ISP cloud) can access your server (that is located at <b>18.0.0.2</b>) on your router, with RIP routing you can do just that!')
formatter.append('c', 'Router>enable')
formatter.append('c', 'Router#conf term')
formatter.append('c', 'Router(config)#router rip')
formatter.append('p', 'It is highly recommended to use RIPv2, which is newer. We will do that')
formatter.append('c', 'Router(config-router)#version 2')
formatter.append('c', 'Router(config-router)#network <b>18.0.0.0</b>')
formatter.append('p', 'Now outside computers should now be able to connect to the server')

notebook.generate(
    {
        'cat':'Router',
        'name':'RIP',
        'exname':'Routing Information Protocol (v2)'
    },
    formatter.compile()
    )
