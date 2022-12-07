## Methodes:
This methodes can take in input list, np.ndarray, dict, vtkPolyData
#### vtkICP  
it is vtk's icp 

#### InitIcp
it is pre orientation to get better result with vtk's icp



## Option :

#### vtkMeanTeeth
    In the init you need to give the teeth's number in list and option you can add the segmentaion's name, then when you call the object with vtkPolyData
    return the Mean of each segmenation's tooth

#### vtkMiddleTeeth
    In the init you need to give the teeth's number in list and option you can add the segmentaion's name, then when you call the object give vtkPolyData
    return the middle of each tooth


#### vtkMeshTeeth
     In the init you need to give the teeth's number in list and option you can add the segmentaion's name, then when you call the object give vtkPolyData
     return all point of each tooth select

#### SelectKey
    In the init you need to give the name of key do you want, and when you call the object give dict
    return dict with all key give in init



## ICP
ICP manage methode, option, the source and target.
Init : give all methodes in the list, and you can an option give above

To launch the methode, use run function of icp. In parameter you can give path of vtk file, or json file, and list, np.ndarray, vtkPolyData, dict (dont work very well).
And run return dic with this key : source, matrix, source_Or (source Oriented), target, source_int (source after option), source_icp




## ToDisplay
ToDisplay:  Transform list, dict, np.ndarray, vtkPolyData to Mesh


## Exemple
You can watch my main, to understand the logic of my librairy
