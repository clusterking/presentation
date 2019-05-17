import clusterking as ck
       
d = ck.Data()
s = ck.scan.WilsonScanner(scale=5, eft='WET', basis='flavio')

s.set_dfunction(
    dGq2,
    binning=linspace(q2min, q2max, 10),
)

s.set_spoints_equidist({
    "CVL_bctaunutau": (-0.3, 0.3, 10),
    "CSL_bctaunutau": (-0.3, 0.3, 10),
    "CT_bctaunutau": (-0.4, 0.4, 10)
})
      
s.run(d)
