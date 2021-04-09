import time
import asyncio

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1, 1, -1))

async def hight_prime_below(x):
    print('Height prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' % (x,y))
            return y
        await asyncio.sleep(0.01)
    return None

async def main():
    t0 = time.time()
    # Instead of waiting each of these functions in turn synchronously, async.io waits & takes the series of coroutines.
    # These coroutines or asynchronous functions get called & executed. And waits until these're all done

    await asyncio.wait([
        hight_prime_below(100000),
        hight_prime_below(10000),
        hight_prime_below(1000),
    ])    

    print('Executed time %.2f ms' % ((time.time() - t0) * 1000))

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())   
#loop.close()