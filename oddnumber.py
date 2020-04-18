def find_it(seq):
    count_dict = {}
    for x in seq:
      if x in count_dict:
          count_dict[x] = count_dict[x] + 1
      else:
          count_dict[x] = 1
    for k,v in count_dict.items():
        if v%2!=0:
          return k

print(find_it([1,3,4,6,2,3,4,4,5]))
