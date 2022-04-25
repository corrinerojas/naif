\begintext

Example of a furnsh kernel for MRO analysis

\begindata

PATH_VALUES     = ( './mro' ) 
PATH_SYMBOLS    = ( 'KDIR' ) 
KERNELS_TO_LOAD = (
                   '$KDIR/MRO_SCLKSCET.00100.tsc',
                   '$KDIR/mro_sc_psp_220111_220117.bc',
                   '$KDIR/mro_v16.tf',
                   '$KDIR/naif0012.tls',
                   '$KDIR/pck00008.tpc',
                   '$KDIR/spk_psp_rec72557_72552_72917_p-v1.bsp',
                   '$KDIR/spk_psp_rec72579_72575_73362_p-v1.bsp',
                  ) 
