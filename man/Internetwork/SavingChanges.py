formatter = notebook.format.formatter()

formatter.append('p', 'How to save NVRAM')
formatter.append('p', 'Saving NVRAM is important as if your IOS device gets powered down, it will forget all it\'s changes you made to it if you don\'t save it\'s changes to NVRAM')
formatter.append('c', 'Router>enable#')
formatter.append('c', 'Router#copy running-config startup-config')
formatter.append('p', 'Press enter then your changes are now saved into NVRAM!')

notebook.generate(
    {
        'cat':'IOS',
        'name':'MOTD',
        'exname':'Motto Of The Day'
    },
    formatter.compile()
    )
