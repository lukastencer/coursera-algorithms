from arrstack import arrstack

arrs = arrstack()

arrs.show()
arrs.push('wow')
arrs.show()
arrs.push('this')
arrs.show()
arrs.push('is')
arrs.push('some')
arrs.show()
arrs.pop()
arrs.pop()
arrs.push('fish1')
arrs.push('fish2')
arrs.push('fish3')
arrs.push('fish4')
arrs.push('fish5')
arrs.push('fish6')
arrs.push('fish7')
arrs.pop()
arrs.pop()
arrs.pop()
arrs.pop()
arrs.pop()
arrs.pop()

arrs.show()

for elem in arrs:
    print 'iter:', elem