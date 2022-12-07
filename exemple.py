
from utils import ReadSurf,LoadJsonLandmarks,ToDisplay
from pytorch3d.vis.plotly_vis import plot_scene
from icp import vtkICP,InitIcp,vtkMeanTeeth,vtkMiddleTeeth,ICP,vtkMeshTeeth, SelectKey
import numpy as np


def main():
    path = '/home/luciacev/Desktop/Data/ASO_IOS/mag/T1 out all teeth ADJ/P1_T1_IOS_L_out_all_teeth.vtk'
    path_gold = '/home/luciacev/Desktop/Data/ASO_IOS/new_ASO/gold/gold_lower.vtk'
   





    methode = [InitIcp()]
    option = vtkMiddleTeeth([18,20,25])

    methodeicp = ICP(methode,option=option)
    dic = methodeicp.run(path,path_gold)

    mesh = ToDisplay(dic['source'])

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