c = ck.cluster.HierarchyCluster()
c.set_metric()         # Use default metric (Euclidean)
c.set_max_d(1)         # Cut-off value
r = c.run(d)           # Run over data
r.write()              # Write results back to d
