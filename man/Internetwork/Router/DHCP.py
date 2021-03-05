formatter = notebook.format.formatter()

formatter.append('p', 'How to make a DHCP pool on a router')
formatter.append('p', 'In this example, our computer will be connected to <b>GigabitEthernet0/0</b>')
formatter.append('c', 'Router>enable')
formatter.append('c', 'Router#conf term')
formatter.append('c', 'Router(config)#interface <b>GigabitEthernet0/0</b>')
formatter.append('c', 'Router(config-if)#no shutdown')
formatter.append('p', '<b>GigabitEthernet0/0</b> will now be online but our computer cannot communicate with the router just yet as it needs an ip address, we will give the computer an ip address via DHCP.')
formatter.append('c', 'Router(config-if)#ip dhcp excluded-address 192.168.0.1')
formatter.append('c', 'Router(config-if)#ip dhcp pool <b>routerPool</b>')
formatter.append('c', 'Router(dhcp-config)#network 192.168.0.0 255.255.255.0')
formatter.append('c', 'Router(dhcp-config)#dns-server <b>8.8.8.8</b>')
formatter.append('c', 'Router(dhcp-config)#default-router 192.168.0.1')
formatter.append('c', 'Router(dhcp-config)#exit')
formatter.append('p', 'Our computer should now be able to get an ip address via DHCP and can communicate with the router properly')


notebook.generate(
    {
        'cat':'Router',
        'name':'DHCP',
        'exname':'Dynamic Host Configuration Protocol'
    },
    formatter.compile()
    )
