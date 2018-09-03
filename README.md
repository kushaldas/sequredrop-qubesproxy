# SecureDrop Qubes proxy

Warning: This is an unofficial PoC project.


# Setup a SecureDrop development instance behind Tor

Run `make dev` to create a development instance of the SecureDrop development branch
and also run a Tor onion service in the same box so that this tool can access it over
Tor. For the the PoC level, my Tor service is not authenticated.


# Install the code in the Fedora 28 template

For now we will install the dependency SDK and this repo using
rpm built by Kushal Das.

His GPG fingerprint: 

```
A85F F376 759C 994A 8A11  68D8 D821 9C8C 43F6 C5E1
```

The rpms and signed sha256sum details are in [https://kushaldas.in/sdproxy/](https://kushaldas.in/sdproxy/).

In future these will be distributed using a proper *dnf* repository.

Install all of these rpm packaes in the Fedora 28 template. For that first, you will have to download
then in another vm, and then copy them using `qvm-copy` command, and then only you can install them.

Also the install the **tor** package using *dnf*.

```
sudo dnf install tor -y
```


# APPVm requirements

For the development/experiment we will use the following names.

- dproxy: This is the vm which can talk over Tor to the SecureDrop server.
- dclient: The APPvm without network access.

Create the above two vms using Fedora 28 template, remember, *dclient* does
not have any netvm.

# Add the qrexec access policy in the dom0

In the **/etc/qubes-rpc/policy/qubes.SDProxy** file, add the following.

```
$tag:anon-vm $anyvm deny
dclient dproxy allow
```

This tells that the *dclient* appvm is allowed to call this qrexec service
in *dproxy* appvm.


# Configuration in the dproxy server (wtih network access)

For an onion address add the **/etc/qubesproxy.conf** with the onion address as
given below.

```
http://asdfasdfasdf.onion
```

Remember the training slash. Best option is to add the following line in the
*/rw/config/rc.local" file. Reboot the appvm after that.

```
echo "http://asdfasdfasdf.onion" > /etc/qubesproxy.conf
```



# Configuration for the dclinet vm

Add the proxy vm name in the **/etc/sd-proxy-vmname.conf**

```
dproxy
```

Remember the training slash. Best option is to add the following line in the
*/rw/config/rc.local" file. Reboot the appvm after that.

```
echo "dproxy" > /etc/sd-proxy-vmname.conf

# Example usage

Have a look at the *example.py* in this repository for usage example in the **dclient** appvm.
It also requires *python3-pyotp* package to be installed for the example otp usage.
