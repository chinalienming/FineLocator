#!/bin/bash 

ss_script_dir=$1       # ~/FineLocator/queryexpansion
code_vec_dir=$2        # ~/FineLocator/expRes/vec/code/${proj} 
ss_dir=$3              # ~/FineLocator/expRes/ss/${proj}
proj_id=$4             # ${proj_id}
word2vec_dimension=$5 
PYTHON=$6              # python3.7

rm -f ${ss_dir}/${proj_id}
mkdir -p ${ss_dir}      
cd ${ss_script_dir}
${PYTHON} ss.py --code_vector_dir ${code_vec_dir}/${proj_id} \
                --dim ${word2vec_dimension} \
                --save_path ${ss_dir}/${proj_id}
