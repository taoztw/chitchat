
# 训练dialogue model
python train.py --epochs 50 --batch_size 16 --raw --seed 1 \
  --train_raw_path \
  --train_tokenized_path \
  --log_path \
  --dialogue_model_output_path \
  --pretrained_model \

