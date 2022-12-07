
from utils import ReadSurf,LoadJsonLandmarks,ToDisplay
from pytorch3d.vis.plotly_vis import plot_scene
from icp import vtkICP,InitIcp,vtkMeanTeeth,vtkMiddleTeeth,ICP,vtkMeshTeeth, SelectKey
import numpy as np


def main():
    path = '/home/luciacev/Desktop/Data/ASO_IOS/mag/T1 out all teeth ADJ/P1_T1_IOS_L_out_all_teeth.vtk'
    path_gold = '/home/luciacev/Desktop/Data/ASO_IOS/new_ASO/gold/gold_lower.vtk'
    path_json = '/home/luciacev/Desktop/Data/ALI_IOS/landmark/Training/data_base/data_occlusal/patient/P8/Lower/Lower_P8.json'
    path_json_gold = '/home/luciacev/Desktop/Data/ALI_IOS/landmark/Training/data_base/data_occlusal/patient/P21/Lower/Lower_P21.json'





    methode = [InitIcp()]
    # option = vtkMiddleTeeth([18,20,25])
    option = SelectKey(['LL1O','LR1O','LL6O','LR6O'])
    a = ICP(methode,option=option)

    source = [[0,0,1],[1,0,1],[0,1,2]]
    gold =[[0,0,0],[1,0,0],[0,1,0]]
    dic_gold = {'1':[0,0,0],'2':[0,1,0],'3':[1,0,0]}
    dic_source = {'1':[0,0,1],'2':[0,1,1],'3':[1,0,2]}
    dic = a.run(path_json,path_json_gold)

    mesh = ToDisplay(dic['source'])

    mesh_landmark = ToDisplay(LoadJsonLandmarks(path_json))

    print('output',type(dic['source_Or']))

    mesh_output = ToDisplay(dic['source_Or'])
    mesh_gold = ToDisplay(dic['target'])



    fig = plot_scene({
    "subplot1": {
        "mouth" : mesh,
        "output": mesh_output,
        "gold" : mesh_gold
        }
    })
    fig.show()

    print('done')





if __name__ == '__main__':
    print('start')
    main()