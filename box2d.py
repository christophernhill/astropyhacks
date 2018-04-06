from astropy.convolution import convolve as ap_convolve
from astropy.convolution import Box2DKernel
box_2D_kernel = Box2DKernel(9)
nan=float('nan')
data=np.where(data==0,nan,data)
data[ :, 0]=nan
data[ :,-1]=nan
data[ 0, :]=nan
data[-1, :]=nan
data2=ap_convolve(data, box_2D_kernel, normalize_kernel=True)

plt.clf()
dd=data-data2
dd=np.ma.masked_invalid(dd)
ddmean=np.mean(dd)
ddstd=np.std(dd)
dd=dd-ddmean
ddcvlo=-ddstd*2.
ddcvhi=+ddstd*2.
ddcvin=(ddcvhi-ddcvlo)/100.

plt.pcolor(dd[:,0:2500].T,np.arange(ddcvlo,ddcvhi,ddcvin),cmap=plt.cm.get_cmap('Blues'))
