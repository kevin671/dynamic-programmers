ROOT_DIR="/work/gg45/g45004/dynamic-programmers"

# Edit Distance  ###########################################
#COMPLEXITY=100 # 60 # 100 
#LEN_OF_FIRST_STRING=${COMPLEXITY}
#DATA_DIR=${ROOT_DIR}"/data/ED/"${LEN_OF_FIRST_STRING}_random
#TASK=${ROOT_DIR}"/tasks/ED"
#MAXLEN=$((2 * COMPLEXITY + 7)) # 207 # 127
#MAXDATA=${MAXLEN}
#NUM_RANGE=$((COMPLEXITY * 3))
#VOCAB_SIZE=$((NUM_RANGE + 31))

# Longest Common Subsequence  ###########################################
COMPLEXITY=60 # 100
DATA_DIR=${ROOT_DIR}"/data/LCS/"${COMPLEXITY}
TASK=${ROOT_DIR}"/tasks/LCS"
OUTPUT_DIR=${ROOT_DIR}"/output/LCS/"${COMPLEXITY}
MAXLEN=$((COMPLEXITY*2 + 10))
MAXDATA=${MAXLEN}
NUM_RANGE=$((COMPLEXITY*2))
VOCAB_SIZE=$((NUM_RANGE + 4))


MODEL="LoopedGPT" # LoopedGPT, TimeDependentLoopedGPT
LAYER=1
LOOP=10

#MODEL="GPT"
#LAYER=12
#LOOP=1

OUTPUT_DIR=${ROOT_DIR}"/output/$(basename "$TASK")_"${COMPLEXITY}"/"${MODEL}"_"${LOOP}
WANDB_NAME="$(basename "$TASK")_"${COMPLEXITY}"_"${MODEL}"_"${LOOP}

torchrun --standalone --nproc_per_node=2 train.py\
 --file ${DATA_DIR}\
 --folder ${TASK}\
 --output_dir ${OUTPUT_DIR}\
 --wandb_name ${WANDB_NAME}\
 --model ${MODEL}\
 --maxlen ${MAXLEN}\
 --maxdata ${MAXDATA}\
 --vocab ${VOCAB_SIZE}\
 --num_range ${NUM_RANGE}\
 --weight_decay 0.01\
 --learning_rate 1e-4\
 --drop 0.0\
 --batch_size 64\
 --epoch 100\
 --warmup 5\
 --dmodel 256\
 --head 4\
 --num_layer ${LAYER}\
 --num_loop ${LOOP}\