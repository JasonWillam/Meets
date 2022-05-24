# -- coding: utf-8 --
import sys
from source.utils_functions_udop.dirk_utils import yi2san, qu_ping_jun, qpj_0, qpj_1, qpj_2, qpj_3, qpj_rocket_cit

from meets_zhongjianjian import mec_wc

from source.operators_iclsc.initiate import dirk_random_initial_pop_or_external_init_pop as d_r_or_ext_init
from os.path import dirname, realpath


# linux ,
# command line : python meets.py    .....\parameters\para_txts_silingbu.txt
# do not  need line 2, line 3 and line 4,  need line 1
para, instance_of_f_shop, filepath_of_flowshop = yi2san(sys.argv[1]) # line 1

# windows,
# command line : python meets.py
# need line 2, line 3 and line 4, do not  need line 1
#current_file_path = dirname(realpath(__file__)) # line 2
#sys_arg_1_input_para = current_file_path + '\parameters\para_txts_silingbu.txt' # line 3
#para, instance_of_f_shop, filepath_of_flowshop = yi2san(sys_arg_1_input_para) #  line 4

######### tiaoshi by ubuntu of local lenevo bijiben
#current_file_path = dirname(realpath(__file__)) # line 2
#sys_arg_1_input_para = current_file_path + '/parameters/para_txts_silingbu.txt' # line 3
#para, instance_of_f_shop, filepath_of_flowshop = yi2san(sys_arg_1_input_para) #  line 4


pop_init_sanjiangyuan = d_r_or_ext_init(instance_of_f_shop,para[0]['pop_init_size'], [], 0)

# with clustering , short, wc
flag_1_wc = [1, 1, 89]  #ei_cl_tm_flags
flag_2_wc = [1, 1, 8]
flag_3_wc = [1, 1, 9]
flag_4_wc = [1, 1, 89]
flag_s_wc = [flag_1_wc, flag_2_wc, flag_3_wc, flag_4_wc]

stat_t2_wc_list = []
stat_t2e_wc_list = []
run_times = para[2]['run_times']
for i in range(0, run_times):
    pop_i_wc, stat_t2_wc, stat_t2e_wc = mec_wc(instance_of_f_shop, para, filepath_of_flowshop, flag_s_wc, pop_init_sanjiangyuan)
    stat_t2_wc_list.append(stat_t2_wc)
    stat_t2e_wc_list.append(stat_t2e_wc)

stat_t2_wc_average =  qu_ping_jun(stat_t2_wc_list)
stat_t2e_wc_average =  qu_ping_jun(stat_t2e_wc_list)





# no clustering , short, nc
flag_1_nc = [1, 0, 89]  #ei_cl_tm_flags
flag_2_nc = [1, 0, 8]
flag_3_nc = [1, 0, 9]
flag_4_nc = [1, 0, 89]
flag_s_nc = [flag_1_nc, flag_2_nc, flag_3_nc, flag_4_nc]

stat_t2_nc_list = []
stat_t2e_nc_list = []
run_times = para[2]['run_times']
for i in range(0, run_times):
    pop_i_nc, stat_t2_nc, stat_t2e_nc = mec_wc(instance_of_f_shop, para, filepath_of_flowshop, flag_s_nc, pop_init_sanjiangyuan)
    stat_t2_nc_list.append(stat_t2_nc)
    stat_t2e_nc_list.append(stat_t2e_nc)

stat_t2_nc_average =  qu_ping_jun(stat_t2_nc_list)
stat_t2e_nc_average =  qu_ping_jun(stat_t2e_nc_list)

qpj_0(filepath_of_flowshop, para[2], stat_t2_wc_average, stat_t2e_wc_average)
qpj_1(filepath_of_flowshop, para[2], stat_t2_nc_average, stat_t2e_nc_average)

qpj_2(filepath_of_flowshop, para[2], stat_t2_nc_average, stat_t2_wc_average)
qpj_3(filepath_of_flowshop, para[2], stat_t2e_nc_average, stat_t2e_wc_average)

qpj_rocket_cit(filepath_of_flowshop, para[2], stat_t2_wc_average, stat_t2e_wc_average,stat_t2_nc_average, stat_t2e_nc_average)
#import package_name
#print('package_name: {}'.format(package_name.__version__))
pvvvvvv = 'Python: {}'.format(sys.version)
print('花开在眼前  pvvvvvv = ', pvvvvvv)