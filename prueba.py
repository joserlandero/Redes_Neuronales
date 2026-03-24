import tensorflow as tf
import torch
import mlx.core as mx

print("--- Iniciando prueba de frameworks --- \n")

# 1. TENSOR EN TENSORFLOW
tensor_tf = tf.constant([1.0, 2.0, 3.0])
print("TensorFlow:\n", tensor_tf, "\n")

# 2. TENSOR EN PYTORCH
tensor_torch = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch:\n", tensor_torch, "\n")

# 3. ARRAY EN MLX (El poder de tu Mac)
array_mlx = mx.array([1.0, 2.0, 3.0])
print("MLX:\n", array_mlx, "\n")

print("¡Todo funciona a la perfección!")