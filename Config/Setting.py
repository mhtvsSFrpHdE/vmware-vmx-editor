# https://gist.github.com/wpivotto/3993502

# bios.bootDelay = "0", milliseconds, if you want select boot device, the one can be useful
# cpuid.coresPerSocket = 1, each virtual CPU has 1 core by default, some guest system doesn't support too much virtual CPUs
# ethernet0.virtualDev = "e1000e", set to "vmxnet3" to get 10 Gbps network device if you do need fast network, but overall resource consume may increase
# firmware = "efi", use new efi boot
# hard-disk.hostBuffer = "disabled", by default disk cache in RAM is enable, but can have serious disk performance impact in certain environment. See https://github.com/mhtvsSFrpHdE/prefetch/issues/6
# mainMem.partialLazyRestore = "FALSE" , do not restore snapshots in background
# mainMem.partialLazySave = "FALSE" , do not take snapshots in background
# mainMem.useNamedFile = "FALSE", doesn't use named-file - use for VMs on USB-disks or other slow disks. On Windows: useNamedFile= "FALSE" causes memory to be backed by the host's swap space
# MemTrimRate = "0" , by disabling MemTrimRate, memory allocation inside the guest is faster because it doesn't take and give memory to the host os upon all requests
# prefvmx.minVmMemPct = "100", fit memory into RAM. Whenever possible, avoid settings lower 100%
# prefvmx.useRecommendedLockedMemSize = "TRUE" , this tells VMWare whether to use a fixed sized memory chunk or balloon and shrink memory as needed
# priority.grabbed = "high" , sets the priority for the VM in grabbed state
# priority.ungrabbed = "normal" , sets the priority for the VM in ungrabbed state
# sched.mem.pshare.enable = "FALSE", by disabling memory sharing your guests will not share common memory blocks. Your VMware product will also stop comparing memory blocks
# uefi.secureBoot.enabled = "FALSE", only effect if turn on efi boot. If true, certain old efi bootable ISO will not work like gparted
targetList = {
    # 'bios.bootDelay': '"0"',
    # 'cpuid.coresPerSocket': '"1"',
    # 'ethernet0.virtualDev': '"e1000e"',
    # 'firmware': '"efi"',
    # 'hard-disk.hostBuffer': '"disabled"',
    'mainMem.partialLazyRestore': '"FALSE"',
    'mainMem.partialLazySave': '"FALSE"',
    'mainMem.useNamedFile': '"FALSE"',
    'MemTrimRate': '"0"',
    'prefvmx.minVmMemPct': '"100"',
    'prefvmx.useRecommendedLockedMemSize': '"TRUE"',
    'priority.grabbed': '"high"',
    'priority.ungrabbed': '"normal"',
    'sched.mem.pshare.enable': '"FALSE"',
    # 'uefi.secureBoot.enabled': '"FALSE"'
}

# Try not to change order of these value
# Because it seems each new vmx always have them on top
fixedBeginningList = [
    ".encoding",
    "config.version",
    "virtualHW.version"
]

# For aesthetics, but may cause potential problems
sortRest = True
