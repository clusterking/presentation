c = ck.cluster.HierarchyCluster(d)
c.set_metric()         # Use default metric (Euclidean)
c.build_hierarchy()    # Build up clustering hierarchy
c.cluster(max_d=0.15)  # "Cut off" hierarchy
c.write()              # Write results to d
