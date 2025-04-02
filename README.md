# IP-Fast-Config
## # Description
If you have a standard configuration in your organization network, this script can help you for type only the variable inputs of your network configuration.

You can modify the dictionary and command variables to match your network standard.

## # Dependences
- pyinstaller

## # Configuration
**DICTIONARY STRUCTURE**
```
- 'NAME':   'Ethernet',     # Name of your network adapter.
- 'IP'  :   '0.0.0.0',      # Computer IP address.
- 'MASK':   '0.0.0.0',      # Subnet mask.
- 'GATE':   '0.0.0.0',      # Gateway address.
- 'DNS1':   '0.0.0.0',      # First DNS address.
- 'DNS2':   '0.0.0.0'       # Secondary DNS address.
```
> [!NOTE]
>
> Check the ***INTERFACE NAME*** of your system. This is the most important parameter for the script. By default, it is usually ***Ethernet***, but if you have **virtual machines** or multiple network adapters, your primary interface may be different. 

> [!IMPORTANT]
>
> For most common ***IPs*** configuration, only change the last field of **IP**.
>
> **EXAMPLE**
>```
> base_config = {
>    'NAME': 'Ethernet',        # Default interface name.
>    'IP': '192.168.0.',        # Leave the last field empty.
>    'MASK': '255.255.255.0',   # Default subnet mask.
>    'GATE': '192.168.0.1',     # Default gateway.
>    'DNS1': '8.8.8.8',         # Google DNS1.
>    'DNS2': '8.4.8.4'          # Google DNS2.
>}
>```
> Before compile.. Configure the ***base_config*** dictionary with your standard configuration.
