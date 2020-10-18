# 用来存放应用于models.py的函数工具


def set_choices(choicesList):
    # 用于将选项生成CharField的choices元组
    # 参数:选项列表
    choicesTuple = list()
    for choice in choicesList:
        singlechoicelist = list()
        singlechoicelist.append(choice)
        singlechoicelist.append(choice)
        choicesTuple.append(tuple(singlechoicelist))
    return tuple(choicesTuple)

set_choices(['通过','否决'])