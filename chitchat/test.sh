# 是否采用cuda
# 生成模型位置
# topp nucleus sampling 0-1概率
# topk


python interact.py \
  --no_cuda
  --dialogue_model_path ./dialogue_model \
  --max_history 5 \
  --topp 0.8 \
