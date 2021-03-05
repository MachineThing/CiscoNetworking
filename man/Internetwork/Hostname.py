formatter = notebook.format.formatter()

formatter.append('p', 'How to assign a hostname to an IOS device')
formatter.append('c', 'Router>enable')
formatter.append('c', 'Router#conf term')
formatter.append('c', 'Router(config)#hostname <b>routerName</b>')
formatter.append('c', 'routerName(config)#exit')

notebook.generate(
    {
        'cat':'IOS',
        'name':'Hostname'
    },
    formatter.compile()
    )
