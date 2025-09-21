st1 ={'name': "Nikos", 'grades':[7.0, 8.5, 6.5]}
st2 = st1
st3 = st1.copy()
import copy
st4 = copy.copy(st1)
st5 = copy.deepcopy(st1)
st1['name'] = 'Nikolaos'
st1['grades'].append(9.0)