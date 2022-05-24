# -- coding: utf-8 --
from source.task_0 import meme_solver_task_0 as t0_meme

from source.utils_functions_udop.dirk_utils import visualize_result_of_hv_no_look, visualize_result_of_makespan_no_look, \
                                                   visualize_result_of_vivi_no_look_location1_g, visualize_result_of_tft_no_look


def mec_wc(instance_of_f_shop, para, filepath_of_flowshop, flags, pop_init):
    """ 2 run with  clustering. 1st run, original task 2; 2nd, tranferred. copyright by Dirk21 """

    # task 2,  with clustering, no transferring
    stat_t2n, pop_last_t2n, pop_i = t0_meme(instance_of_f_shop, para[2], flags[0],
                                            pop_init, [[], []], filepath_of_flowshop)  # flag_4 = [1, 0]

    visualize_result_of_makespan_no_look(filepath_of_flowshop, para[2], stat_t2n)
    visualize_result_of_hv_no_look(filepath_of_flowshop, para[2], stat_t2n)

    # subtask 1_0 (belong to task 1), with clustering
    # subtask 1_1 (belong to task 1), with clustering
    stat_t10n, pop_list_t10n = t0_meme(instance_of_f_shop, para[0], flags[1],
                                        pop_i, [[], []], filepath_of_flowshop)  # flag_4 = [1, 0]

    stat_t11n, pop_list_t11n = t0_meme(instance_of_f_shop, para[1], flags[2],
                                       pop_i, [[], []], filepath_of_flowshop)  # flag_4 = [1, 0]

    visualize_result_of_tft_no_look(filepath_of_flowshop, para[0], stat_t10n)
    visualize_result_of_makespan_no_look(filepath_of_flowshop, para[1], stat_t11n)

    # task 2, with clustering, with transferring from task 1
    stat_t2n_eto, pop_last_t2n_eto, pop_i_eto = t0_meme(instance_of_f_shop, para[2], flags[3],
                                                        pop_i, [pop_list_t10n, pop_list_t11n], filepath_of_flowshop)  # flag_4 = [1, 0]

    visualize_result_of_makespan_no_look(filepath_of_flowshop, para[2], stat_t2n_eto)
    visualize_result_of_hv_no_look(filepath_of_flowshop, para[2], stat_t2n_eto)

    # compare task 2s of  original and transferred versions
    visualize_result_of_vivi_no_look_location1_g(filepath_of_flowshop, para[2], stat_t2n, stat_t2n_eto)

    return pop_i, stat_t2n, stat_t2n_eto