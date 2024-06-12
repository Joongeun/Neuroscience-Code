image = '''Woman8
Woman3
Woman6
Man5
Woman1
Man6
Woman9
Man9
Man4
Woman7
Man8
Man2
Woman2
Woman5
Man1
Man12
Man3
Man7
Woman10
Woman4'''
image += "\n"
vals = '''4
2
1
1
4
3
4
1
3
2
1
1
3
2
2
2
3
1
3
4'''
vals += "\n"
new_vals = []
new_img = []
img = ""
diff = ""
id = []
d = []
i = 0
index = []
for num in vals:
    if num != "\n":
        diff += num
    else:
        new_vals.append(float(diff))
        diff = ""

for char in image:
    if char != "\n":
        img += char
    else:
      print(img)
      try:
          a = str(int(img[-2]))
          id.append(img[0]+a+img[-1])
      except:
          id.append(img[0]+img[-1])
      datum = {img: new_vals[i]}
      d.append(datum)
      img = ""
      i += 1
m_sorted, w_sorted = [{} for i in range(15)],[{} for i in range(15)]

for ind, i in enumerate(id):
  if i[0] == "W":
    w_sorted[int(i[1:])] = d[ind]
  else:
    m_sorted[int(i[1:])] = d[ind]
m_sorted, w_sorted = [i for i in m_sorted if i != {}], [i for i in w_sorted if i != {}]

def print_data(d):
  for i in range(len(d)):
    data = d[i]
    k = list(data.keys())
    v = list(data.values())
    print(str(v[0]))
print_data(m_sorted)
print_data(w_sorted)