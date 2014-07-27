from union_find_percolation import Percolation

print '--------------test percolation UF---------------------'

perc = Percolation(3)
perc.show()

perc.step(5)
perc.show()
perc.step(3)
perc.show()
perc.step(1)
perc.show()
perc.step(2)
perc.show()
perc.step(6)
perc.show()
perc.step(8)
perc.show()