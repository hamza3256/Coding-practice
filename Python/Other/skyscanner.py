def solution(aE, fI, o, d):
  c = o + "-" + d
  v = []
  if fI == []:
    return 0
  for i, fl in enumerate(fI):
    if c == fl[:len(c)]:
        for craft in aE:
            print(craft.split("-")[0])
            print(fl.split("-")[2])
            if fl.split("-")[3] == craft.split("-")[0]:
                v.append(float(fl.split("-")[2]) * float(craft.split("-")[1]))
  if v == []:
    return 0
  return round(min(v), 2)


aE= ["boeing_737-0.101", "boeing_747-0.12", "boeing_787-0.14"]
fI= ["LON-EDI-534-boeing_737", "LON-EDI-534-boeing_787", "-LON-464-embraer_190"]
o="LON"
d= "EDI"
print(solution(aE, fI, o, d))




def solution(aP, cO):
    if aP == []:
      return []
    if len(aP) == 1:
      return aP
    cost = {}
    for i in aP:
      if i == "s1":
        if cO < 500:
          cost["s1"] = ( 1.25 *cO)
        else:
          cost["s1"] = ( 1 * cO)
      elif i == "s2":
        if cO <= 300:
          cost["s2"] =( cO *1.5)
        else:
          cost["s2"] =( 300*1.5 + (cO - 300)*0.5)
      elif i == "b1":
        cost["b1"] =( 0.8 * cO)
      elif i == "h1":
        cost["h1"] =(100 + 0.5*cO)
      elif i == "h2" and cO % 10 == 0:
        cost["h2"] =( (cO // 10) * 9.90)
    print(cost)
    result = []
    cost = {k: v for k, v in sorted(cost.items(), key=lambda item: item[1])}
    print(cost)
    for k, v in cost.items():
        if not check(result, k[0]):
            result.append(min(cost, key=cost.get))
            cost[k] = float('inf')
        if len(result) == 2:
          break
    return result


def check(l, n):

    if not l:
        return 0

    elif l[0][0] == n:
        return True

    elif check(l[1:], n):
        return True
    else:
        return False
