"""!
@file geometry.py
@brief This module provides basic geometry operations.
"""

import math

def rectangle_area(length, width):
    """!
    @brief Calcule l'aire d'un rectangle
    @param length La longueur du rectangle
    @param width La largeur du rectangle
    @return L'aire du rectangle
    """
    return length * width

def rectangle_perimeter(length, width):
    """!
    @brief Calcule le périmètre d'un rectangle
    @param length La longueur du rectangle
    @param width La largeur du rectangle
    @return Le périmètre du rectangle
    """
    return 2 * (length + width)

def circle_area(radius):
    """!
    @brief Calcule l'aire d'un cercle
    @param radius Le rayon du cercle
    @return L'aire du cercle
    """
    return math.pi * radius ** 2

def circle_circumference(radius):
    """!
    @brief Calcule la circonférence d'un cercle
    @param radius Le rayon du cercle
    @return La circonférence du cercle
    """
    return 2 * math.pi * radius

