#14. Ввести список А из 10 элементов, найти разность положительных элементов кратных 11, их количество и вывести результаты на экран.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
  A = tuple(map(int, input("Введите кортеж").split()))
  if len(A) != 10:
    print("Неверный размер кортежа")
  else:
      count=0
      c=0
      s=0
      for a in A:
          if a>0 and a%11==0:
              s+=1
              b=(max(A))
              if a<b:
                  count+=a
                  c=b-count
      print("Количество элементов:", s, )
      print("Разность элементов:",c,)


