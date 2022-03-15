### License
© 2022 Copyright claimant to remain anonymous during evaluation period. All rights reserved. May be used only pursuant to Software Evaluation Terms of Use.  CONFIDENTIAL – MAY CONTAIN TRADE SECRETS

### Installation
We provide instructions how to install dependencies via conda.

Install PyTorch 1.6 and torchvision 0.7:
```
conda install pytorch==1.6.0 torchvision==0.7.0
```

Compile DCN module(requires GCC>=5.3, cuda>=10.0)
```
cd models/dcn
python setup.py build_ext --inplace
```

### Dataset
```
datasets
├── self_ovis_train_data
├── self_ovis_val_test_data
├── self_vis_train_data
├── self_vis_val_test_data
```

### Training

Training of the model requires at least 32g memory GPU, we performed the experiment on 3090 card.

```
python main.py --dataset vis/ovis
```