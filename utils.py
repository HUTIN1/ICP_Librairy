
import os 
import glob 
import vtk
import numpy as np
import SimpleITK as sitk
import json
from vtk.util.numpy_support import vtk_to_numpy
from torch import tensor
import torch
from random import randint
from math import pi
from pytorch3d.structures import Meshes
from pytorch3d.utils import ico_sphere


def ReadSurf(path):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(path)
    reader.Update()
    surf = reader.GetOutput()

    return surf

def LoadJsonLandmarks(ldmk_path,full_landmark=True,list_landmark=[]):
    """
    Load landmarks from json file
    
    Parameters
    ----------
    img : sitk.Image
        Image to which the landmarks belong
 
    Returns
    -------
    dict
        Dictionary of landmarks
    
    Raises
    ------
    ValueError
        If the json file is not valid
    """

    with open(ldmk_path) as f:
        data = json.load(f)
    
    markups = data["markups"][0]["controlPoints"]
    
    landmarks = {}
    for markup in markups:
        lm_ph_coord = np.array([markup["position"][0],markup["position"][1],markup["position"][2]])
        lm_coord = lm_ph_coord.astype(np.float64)
        landmarks[markup["label"]] = lm_coord
    
    if not full_landmark:
        out={}
        for lm in list_landmark:
            out[lm] = landmarks[lm]
        landmarks = out
    return landmarks







def WriteSurf(surf, output_folder,name,inname):
    name, extension = os.path.splitext(name)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)


    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(os.path.join(output_folder,f"{name}{inname}{extension}"))
    writer.SetInputData(surf)
    writer.Update()


def ReadSurf(path):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(path)
    reader.Update()
    surf = reader.GetOutput()

    return surf





def UpperOrLower(path_filename):
    """tell if the file is for upper jaw of lower

    Args:
        path_filename (str): exemple /home/..../landmark_upper.json

    Returns:
        str: Upper or Lower, for the following exemple if Upper
    """
    out = 'Lower'
    st = '_U_'
    st2= 'upper'
    filename = os.path.basename(path_filename)
    if st in filename or st2 in filename.lower():
        out ='Upper'
    return out




def search(path,extension):
    out =[]
    files = glob.glob(os.path.join(path,extension))
    folders = os.listdir(path)
    for file in files:
        out.append(file)
    for folder  in folders:
        if os.path.isdir(os.path.join(path,folder)):
            out+=search(os.path.join(path,folder),extension)

    return out




def SurfToMesh(surf):

    verts = tensor(vtk_to_numpy(surf.GetPoints().GetData()),dtype= torch.float32)
    faces = tensor(vtk_to_numpy(surf.GetPolys().GetData()).reshape(-1, 4)[:,1:])

    mesh = Meshes(verts=verts.unsqueeze(0),faces=faces.unsqueeze(0))

    return mesh


def ListToMesh(list,radius=0.3):
    list_verts =[]
    list_faces = []
    for point in list:
        sphere = ico_sphere(1)
        list_verts.append(sphere.verts_packed()*radius+tensor(point).unsqueeze(0).unsqueeze(0))
        list_faces.append(sphere.faces_list()[0].unsqueeze(0))


    list_verts = torch.cat(list_verts,dim=0)
    list_faces = torch.cat(list_faces,dim=0)

    mesh = Meshes(verts=list_verts,faces=list_faces)

    return mesh


def ToDisplay(input):
    if isinstance(input,dict):
        mesh = ListToMesh(input.values())

    if isinstance(input,list):
        mesh = ListToMesh(input)

    if isinstance(input,np.ndarray):
        mesh = ListToMesh(input.tolist())
    
    if isinstance(input,vtk.vtkPolyData):
        mesh = SurfToMesh(input)

    return mesh
