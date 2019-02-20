import asyncio


def chain(obj):
    """
    Enables coroutines chain for obj.
    Usage: text = yield from chain(obj).go().click().attr
    Note: Returns not coroutine, but object that can be yield from.
    """
    class Chain:
        _obj = obj
        _queue = []

        # Collect getattr of call to queue:
        def __getattr__(self, name):
            Chain._queue.append({'type': 'getattr', 'name': name})
            return self

        def __call__(self, *args, **kwargs):
            Chain._queue.append({'type': 'call', 'params': [args, kwargs]})
            return self

        # On iter process queue:
        def __iter__(self):
            res = Chain._obj
            while Chain._queue:
                action = Chain._queue.pop(0)
                if action['type'] == 'getattr':
                    res = getattr(res, action['name'])
                elif action['type'] == 'call':
                    args, kwargs = action['params']
                    res = res(*args, **kwargs)
                if asyncio.iscoroutine(res):
                    res = yield from res
            return res
    return Chain()


class Browser:
    @asyncio.coroutine
    def go(self):
        print('go')
        return self

    @asyncio.coroutine
    def click(self):
        print('click')
        return self

    def text(self):
        print('text')
        return 5


@asyncio.coroutine
def main():
    text = yield from chain(Browser()).go().click().go().text()
    print(text)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())