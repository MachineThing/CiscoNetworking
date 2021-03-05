formatter = notebook.format.formatter()

formatter.append('p', 'How to configure a MOTD on an IOS device')
formatter.append('c', 'Router&gt;enable')
formatter.append('c', 'Router#conf term')
formatter.append('c', 'Router(config)#banner motd #<b>My awesome MOTD</b>#')
formatter.append('p', 'Now once you log on to the IOS device again, you will see something like this:')
formatter.append('c', 'Press RETURN to get started!<br />')
formatter.append('c', '<b>My awesome MOTD</b><br />')
formatter.append('c', 'Router&gt;')

notebook.generate(
    {
        'cat':'IOS',
        'name':'MOTD',
        'exname':'Motto Of The Day'
    },
    formatter.compile()
    )
