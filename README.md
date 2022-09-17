# vmware-vmx-editor
No more manually operation and common optimization.

## How to use

The code is tested under python 3.9.10.  
Goto `Config\Setting.py`, check out comments and do modify as you wish.

After save config, run:
```
cd vmware-vmx-editor
python main.py FileToEdit.vmx
```
New file should save to `modified_FileToEdit.vmx`.

## What is this

VMWare have some counterintuitive behavior (I'm surprised a VM will run like that).  
Thus one may want to adjust vmx, however they don't very handy if one have many VMs.  
For example, it's hard to tell which value already modified or not.

With `vmware-vmx-editor`, you can make sure a set of config can always present in all vmx.
