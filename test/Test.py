
from time import sleep
import asyncio

class TestClass():

    async def do_stuff(self, number):
        return number + 1

done = False

async def test_fun():
    test = TestClass()

    obj = test.do_stuff(1)

    print(type(obj))
    print(obj)

    print(await obj)
    global done
    done = True

asyncio.run(test_fun())

while(not done):
    sleep(1)
    print("Sleeping")
    