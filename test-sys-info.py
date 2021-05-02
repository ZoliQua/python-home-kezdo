#
# This code writes the current version of the python into the console
#

import sys
print("The current version of this Python run:")
print (sys.version)
print("The current detailed version is:")
print (sys.version_info)

cols = ["type", "main_condition", "condition_value", "sub_condition", "sub_condition_value", "pfs_0", "pfs_0_months_mean", "pfs_0_months_std", "pfs_1", "pfs_1_months_mean",
						 "pfs_1_months_std", "pfs_1_perc", "os_0", "os_0_months_mean", "os_0_months_std", "os_1", "os_1_months_mean",
						 "os_1_months_std", "os_1_perc", "dss_0", "dss_0_PFS_months_mean", "dss_0_PFS_months_std", "dss_1", "dss_1_PFS_months_mean",
						 "dss_1_PFS_months_std", "dss_1_perc"]

print(len(cols))