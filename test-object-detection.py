import cv2 
import argparse
import numpy as np
from numpy.typing import NDArray
from typing import Dict, Union, List
import od #importamos la "libreria" que creamos, donde estan las funciones del programa


def run_pipeline(args:argparse)->None: #definimos la funcion principal, donde se llaman las funciones de la libreria od

    # Initialise video capture
    cap = od.initialise_camera(args)

    # Process video
    od.segment_object(cap, args)

    # Close all open windows
    od.close_windows(cap)


if __name__=='__main__': #aqui es donde se ejecuta pipeline con las funciones creadas

    # Get data from CLI
    args = od.parse_cli_data()

    # Run pipeline
    run_pipeline(args)