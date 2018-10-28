import itchat
from itchat.content import *

from information import info


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    pass


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid',
    }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # 对作业的操作
    if 'add' in msg.text:
        name = msg.text.split()[1]

        stack = ''
        for row in msg.text.split('\n')[1:]:
            stack = stack + '\n' + row

        info.stack[name] = stack
        msg.user.send(name + "的技术栈录入成功")

    if 'stack' == msg.text:
        stack = ""
        for cow in info.stack:
            stack = stack + cow
            stack = stack + info.stack[cow]
            stack += "\n\n"

        msg.user.send(stack)

    if 'action' == msg.text:
        message = "为了能启动我们这个班级项目，我们这边需要更加了解同学们的技术方向以及技术路线，以便于我们能够分配任务。" \
                  "所以请同学们发一下自己的技术栈(包括已学的与打算学的技术,可以参考下面这幅图,图中没有的也可以)。" \
                  "\n\n(直接发在群里就好， 让同学们更了解你，方便组队)" \
                  "\n\n格式如下(姓名后换行，技术之间用空格隔开)\n\n add 姓名 \n技术1 技术2 技术3 技术4"
        msg.user.send(message)
        msg.user.send('@img@stack.jpg')


itchat.auto_login(True, enableCmdQR=2)
itchat.run(True)
