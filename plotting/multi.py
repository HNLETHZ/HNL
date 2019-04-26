from multiprocessing import Pool
 
def doubler(number):
    return number * 2
 
pool = Pool(processes=3)
result = pool.apply_async(doubler, (25,))
print(result.get())
