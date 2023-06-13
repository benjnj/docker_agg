from itertools import zip_longest
from parse import get_r_pkgs, get_pip_pkgs

pkgs = ["about","read","retir","combine","easy", "little", "small", "time", "event"]

def grouper(data_list, num, fillval=None):
    args = [iter(data_list)] * num
    if fillval is None:
        return list(zip_longest(*args))
    return list(zip_longest(*args,fillvalue=fillval))

def create_sub_list(full_list,num):
    sub_pkgs = [full_list[i:i+num] for i in range(0,len(full_list),num)]
    return sub_pkgs

def produce_pip_install(full_list,lines):
    pip_info = grouper(full_list,lines)
    for item in pip_info:
        quoted_pkgs = ' '.join(i for i in item if i is not None)
        print(f"RUN pip install {quoted_pkgs}")

def produce_r_install(full_list,lines):
    pip_info = grouper(full_list,lines)
    for item in pip_info:
        quoted_pkgs = ','.join(f'"{i}"' for i in item if i is not None)
        print(f"RUN R --no-save -e 'install.packages(c({quoted_pkgs}),quiet = TRUE, verbose = TRUE)'")

def produce_bio_install(full_list,lines):
    pip_info = grouper(full_list,lines)
    for item in pip_info:
        quoted_pkgs = ','.join(f'"{i}"' for i in item if i is not None)
        print(f"RUN R --no-save -e 'BiocManager::install(c({quoted_pkgs}),quiet = TRUE, verbose = TRUE)'")

def produce_dev_install(full_list,lines=1):
    pip_info = grouper(full_list,lines)
    for item in pip_info:
        quoted_pkgs = ','.join(f'"{i}"' for i in item if i is not None)
        print(f"RUN R --no-save -e 'devtools::install_github(c({quoted_pkgs}),quiet = TRUE, verbose = TRUE)'")

def produce_remote_install(full_list,lines=1):
    pip_info = grouper(full_list,lines)
    for item in pip_info:
        quoted_pkgs = ','.join(f'"{i}"' for i in item if i is not None)
        print(f"RUN R --no-save -e 'remotes::install_github(c({quoted_pkgs}),quiet = TRUE, verbose = TRUE)'")

r_pkgs = get_r_pkgs()
pip_pkgs = get_pip_pkgs()

produce_r_install(r_pkgs["normal_install"],8)
produce_pip_install(pip_pkgs,8)
produce_bio_install(r_pkgs["biocmanager"],10)
produce_dev_install(r_pkgs["dev_install"],10)
produce_remote_install(r_pkgs["remote_install"],10)

# for install in r_pkgs["dev_install"]:
#     print(install)

# for next_install in r_pkgs["remote_install"]:
#     print(next_install)
