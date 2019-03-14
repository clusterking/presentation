s = Scanner()
s.set_dfunction(
    bdlnu.dGq2,
    binning=np.linspace(bdlnu.q2min, bdlnu.q2max, 10),
    normalize=True
)
s.set_wpoints_equidist(
    {
        "CVL_bctaunutau": (-0.3, 0.3, 10),
        "CSL_bctaunutau": (-0.3, 0.3, 10),
        "CT_bctaunutau": (-0.4, 0.4, 10)
    },
    scale=5,
    eft='WET',
    basis='flavio'
)
s.run()

s.write("output/scan", "tutorial")
