from super_gradients.training import models
from super_gradients.common.object_names import Models
from ultralytics import YOLO

def modelLoad(path):
    if '.pt' in path and '.pth' in path:
        model = models.get(Models.YOLO_NAS_S,num_classes=2, checkpoint_path=path).cuda()
        return model

    #elif 'trt' in path:
    
    else:
        print("Only supported `.pt`, `.pth`, `.trt`")

#pt pth trtを読み込むお
#pt pth→super…