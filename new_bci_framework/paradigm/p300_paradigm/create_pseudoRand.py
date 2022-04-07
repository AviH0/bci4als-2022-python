import pandas as pd
import random as rd

import numpy as np


def check_no_adj_tar_rep(df):
    # check indices of each type
    check_rep_no = df[df['stim'] == 'no'].index.values
    check_rep_yes = df[df['stim'] == 'yes'].index.values
    index_dist = df[df['stim'] != 'no' and df['stim'] != 'yes'].index.values

    # calculate differences of indices- to check if adjacent index
    dif_no = np.diff(check_rep_no)
    dif_yes = np.diff(check_rep_yes)
    dif_dist = np.diff(index_dist)

    # get indices where the difference is zero
    ind_no_1 = check_rep_no[np.where(dif_no == 1)[0]]
    ind_yes_1 = check_rep_yes[np.where(dif_yes == 1)[0]]
    ind_dist_1 = index_dist[np.where(dif_dist == 1)[0]]

    # get indices of "sandwitch" distractor: distractor between two other distractors
    dif_dist_ind_1 = np.diff(ind_dist_1)
    ind_sand = ind_dist_1[np.where(dif_dist_ind_1 == 1)[0]] + 1

    counter_dist = 0
    if 1 in dif_no:
        for change in range(len(ind_no_1)):
            tar, dist = df.iloc[ind_no_1[change]].copy(), df.iloc[ind_sand[2*counter_dist]].copy()
            df.iloc[ind_no_1[change]], df.iloc[ind_sand[2*counter_dist]] = dist, tar
            counter_dist = counter_dist+1

    if 1 in dif_yes:
        for change_2 in range(len(ind_yes_1)):
            tar, dist = df.iloc[ind_yes_1[change_2]].copy(), df.iloc[ind_sand[2*counter_dist]].copy()
            df.iloc[ind_no_1[change_2]], df.iloc[ind_sand[2*counter_dist]] = dist, tar
            counter_dist = counter_dist + 1

    return df


def create_pseudo_rand(list_stims, num_target_min):
    # at the moment, 4 different distractors which are not 'yes' or 'no'.
    rep_opt_target = [num_target_min, num_target_min + 1, num_target_min + 2]
    rep_target_num = rd.choice(rep_opt_target)
    df = pd.DataFrame(list_stims)

    yes_no = df[(df["stim"] == 'yes') | (df["stim"] == 'no')]
    other_rows = df.iloc[2:7]  # 6 overall: 2 targets and 4 distractors
    target_repeated = pd.concat([yes_no] * rep_target_num, ignore_index=True)
    other_repeated = pd.concat([other_rows] * rep_target_num, ignore_index=True)
    df = pd.concat([target_repeated, other_repeated], ignore_index=True)
    df_rand_ord = df.sample(frac=1, ignore_index=True)

    # Now check that the same target does not repeat straightaway
    df_final = check_no_adj_tar_rep(df_rand_ord)
    # export to excel
    # df_final.to_excel("all_stim_rand_order.xlsx", index = False)

    return df_final.to_dict('records')

# create_pseudo_rand('only_stim_words.xlsx', 1, 2)
# place "r" before the path string to address special character, such as '\'. Don't forget to put the file name
# at the end of the path + '.xlsx'
