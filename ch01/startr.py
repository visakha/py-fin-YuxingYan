import numpy as np 


def reimp():
  """Reimport this module"""
  import importlib
  importlib.reload('ch01.startr')


def pv_f(fv, r, n):
  """Objective: estimate present value
  fv  : = future value
  r   : = rate of discount
  n   : = num of iterations (usually num of years, num of months etc)
                    fv
  formula : pv =  --------
                   (1 + r) ^ n
          


  """
  pv = 0
  iCount = 0
  for cash in fv:
    pv = pv + cash / (1 + r) ** iCount
    iCount = iCount + 1

  # you can use enumeration too
  pv2 = 0
  for i2, cashFlow in enumerate(fv):
    pv2 = pv2 + cashFlow / (1 + r) ** i2


  return (pv, pv2) 


def np_itr_a() :
  """ create an array using numpy and itrate"""
  cashFlows = np.array([1, 20])
  for cash in cashFlows:
    print(cash + 100)


def calc():
  fv = [-100,-30, 10, 40,50, 45,20]
  rate = 3.5 / 100
  cycles = 100
  
  pv1, pv2 = pv_f(fv, rate, cycles)
  print("Present value at rate=", rate, " where fv=", fv )
  print("      -- is 1:",pv1)
  print("      -- is 2:",pv2)


  pv3, _ = pv_f(fv, rate, cycles)
  print("Present value at rate=", rate, " where fv=", fv )
  print("      -- is 1:",pv3)




