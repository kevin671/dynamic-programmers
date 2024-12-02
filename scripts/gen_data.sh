
# Knapsack  ###########################################





# Edit Distance  ###########################################
LEN_OF_FIRST_STRING=100
DATA_DIR="${root_dir}/data/ED/${LEN_OF_FIRST_STRING}"

#python3 tasks/ED/data.py \
#    --file ${DATA_DIR}_random \
#    --length ${LEN_OF_FIRST_STRING} \
#    --train_size 1e6 \
#    --test_size 1e3 \
#    --using 23 \
#    --random_prob 0.4

# Longest Common Subsequence  ###########################################
LEN_OF_FIRST_STRING=100
DATA_DIR="${root_dir}/data/LCS/${LEN_OF_FIRST_STRING}"

python3 tasks/LCS/data.py \
    --file ${DATA_DIR} \
    --length ${LEN_OF_FIRST_STRING} \
    --train_size 1e6 \
    --test_size 1e3 \
    --using 23 \
    --random_prob 0.4