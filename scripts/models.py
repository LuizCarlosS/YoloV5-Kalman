from interfaces import ModelInterface
import torch

class YOLOv5(ModelInterface):
    def __init__(self, **params):
        self.param_dict = params

    def load_model(self, base_model = 'yolov5s', device='cpu'):
        self.model = torch.hub.load('ultralytics/yolov5', base_model, device=device)

    def predict(self,):
        pass