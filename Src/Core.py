fixedBeginning = [None, None, None]
pendingRemove = []
setting = None


def init(pSetting):
    global setting
    setting = pSetting


def is_encoding(input):
    if setting.fixedBeginningList[0] in input:
        pendingRemove.append(input)
        fixedBeginning[0] = input
        return True
    return False


def is_config_version(input):
    if setting.fixedBeginningList[1] in input:
        pendingRemove.append(input)
        fixedBeginning[1] = input
        return True
    return False


def is_virtualHW_version(input):
    if setting.fixedBeginningList[2] in input:
        pendingRemove.append(input)
        fixedBeginning[2] = input
        return True
    return False


def is_targetList(input, targetListKeys):
    for key in targetListKeys:
        if key in input:
            pendingRemove.append(input)
            return True
    return False


def getFixedBeginningString():
    return "".join(fixedBeginning)


def getTargetString():
    stringBuilder = []

    for key in setting.targetList.keys():
        value = setting.targetList[key]
        stringBuilder.append(key)
        stringBuilder.append(" = ")
        stringBuilder.append(value)
        stringBuilder.append("\n")

    return "".join(stringBuilder)
