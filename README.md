# IP-Fast-Config
## # Description
If you have a standard configuration in your organization network, this script can help you for type only the variable inputs of your network configuration.

You can change the dictionary and the variables of the commands depending of your network standard.

## # Dependences

## # Configuration
```
- 'NAME':   'Ethernet',     // Name of your network adapter.
- 'IP'  :   '0.0.0.0',      // Computer IP address.
- 'MASK':   '0.0.0.0',      // Subnet mask.
- 'GATE':   '0.0.0.0',      // Gateway address.
- 'DNS1':   '0.0.0.0',      // First DNS address.
- 'DNS2':   '0.0.0.0'       // Secondary DNS address.
```

> [!IMPORTANT]
>
> For the most basic function clean the last number of ***IP***.
> 
> **EXAMPLE**
> If your organization only changes the last numbers of the ***IP ADDRESS***
>*'192.168.0.XXX'* clear the last number in the dictionary just like this:
>
> - 'IP': *'192.168.0.'*
>
> Check the ***INTERFACE NAME*** of your systems this is the most important parameter for the script and the default is ***Ethernet***.
