formatter = notebook.format.formatter()

formatter.append('p', 'How to assign a hostname to an IOS device')
formatter.append('c', 'Router>enable')
formatter.append('c', 'Router#conf term')
formatter.append('c', 'Router(config)#hostname <b>routerName</b>')
formatter.append('c', 'routerName(config)#exit')
formatter.append('p', 'The hostname of the router will now be <b>routerName</b>')

notebook.generate(
    {
        'cat':'IOS',
        'name':'Hostname'
    },
    formatter.compile()
    )
