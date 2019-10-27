from concurrent.futures import ThreadPoolExecutor
import time

def boil_udon():
  print('  うどんを茹でます。')
  time.sleep(3)
  print('  うどんが茹であがりました。')

tpe = ThreadPoolExecutor(max_workers=3)

print('うどんを100個茹でます。')
for _ in range(10):
    tpe.submit(boil_udon)

tpe.shutdown()
print('うどんが100個茹で上がりました。')
