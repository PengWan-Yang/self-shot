'''
convert detr pretrained weights to cvpr format
'''
import sys
import torch
import collections

if __name__ == "__main__":
    input_path = sys.argv[1]
    detr_weights = torch.load(input_path)['model']
    cvpr_weights = collections.OrderedDict()

    for k,v in detr_weights.items():
        if k.startswith("detr"):
            k = k.replace("detr","cvpr")
        cvpr_weights[k]=v
    res = {"model":cvpr_weights}
    
    torch.save(res,sys.argv[2])


