"""
    pattern publish subscribe
    ~~~~~~~~~~~~~~~~~~~~~~~~~

"""


class Provider:

    def __init__(self):
        self.msg_queue = []
        self.subscribers = {}

    def notify(self, msg):
        self.msg_queue.append(msg)

    def subscribe(self, msg, subscriber):
        # 订阅相关频道。
        self.subscribers.setdefault(msg, []).append(subscriber)

    def unsubscribe(self, msg, subscriber):
        # 取消订阅
        self.subscribers[msg].remove(subscriber)

    def update(self):
        for msg in self.msg_queue:
            # 从消息列表中获取消息
            for sub in self.subscribers.get(msg, []):
                # 从订阅者中找到相关方
                # 推送
                sub.run(msg)
        # 清空队列
        self.msg_queue.clear()


class Publisher:

    def __init__(self, msg_center):
        self.provider = msg_center

    def publish(self, msg):
        # 发布者负责发布消息
        self.provider.notify(msg)


class Subscriber:
    """
    订阅者接受不了消息，处理消息。
    """
    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center

    def subscribe(self, msg):
        self.provider.subscribe(msg, self)

    def unsubscribe(self, msg):
        self.provider.unsubscribe(msg, self)

    def run(self, msg):
        print(f'{self.name} got {msg}')


if __name__ == '__main__':
    provider = Provider()

    cctv = Publisher(provider)

    xiaoming = Subscriber('xiaoming', provider)
    huahua = Subscriber('huahua', provider)
    dandan = Subscriber('dandan', provider)

    huahua.subscribe('chiji')
    dandan.subscribe('csgo')
    xiaoming.subscribe('python')
    cctv.publish('csgo')
    provider.update()
