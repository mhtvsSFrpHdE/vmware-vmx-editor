import sys  # nopep8

import Src.Core as Core
import Config.Setting as Setting

# Read command line parameters
argc = len(sys.argv)
argv = sys.argv
vmxFileName = argv[1]

# Load setting
Core.init(Setting)

# Get exist vmx content
vmxlines = None
with open(vmxFileName, encoding="utf-8") as file:
    vmxlines = file.readlines()

# Line processing
for value in vmxlines:
    if Core.is_encoding(value):
        continue
    if Core.is_config_version(value):
        continue
    if Core.is_virtualHW_version(value):
        continue
    if Core.is_removeList(value, Setting.removeList):
        continue
    if Core.is_targetList(value, Setting.targetList.keys()):
        continue
# Delete managed line from exist vmx
for value in Core.pendingRemove:
    vmxlines.remove(value)

# Create new vmx content
newVmxLines = []
# Fixed and target line is at beginning of file
newVmxLines.append(Core.getFixedBeginningString())
newVmxLines.append(Core.getTargetString())
# Sort rest of line if requested
if Setting.sortRest:
    vmxlines.sort()
# Merge exist vmx to new vmx
newVmxLines.extend(vmxlines)

# Write back
with open("modified_" + vmxFileName, "w", encoding="utf-8") as file:
    vmxlines = file.writelines(newVmxLines)
