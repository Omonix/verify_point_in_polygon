import math

def lb_get_vector(xu, yu, xv, yv):
    '''Function that takes 4 args and calculates their vector
        Input : xu : X of second point : float
                yu : Y of second point : float
                xv : X of first point : float
                yv : Y of first point : float
        Output : \'x\' and \'y\' value of the vector : obj'''
    return {'x': xu - xv, 'y': yu - yv}
def lb_get_standard(x, y):
    '''Function that takes 2 args and calculates their vector
        Input : x : X of vector
                y : Y of vector
        Output : standard value of the vector : float'''
    return (x ** 2 + y ** 2) ** ( 1 / 2 )
def lb_get_scalar(xu, yu, xv, yv):
    '''Function that takes 4 args and calculates their vector
        Input : xu : X of second point : float
                yu : Y of second point : float
                xv : X of first point : float
                yv : Y of first point : float
        Output : scalar of 2 vectors : float'''
    return xu * xv + yu * yv
def lb_get_corner(scalar, product):
    '''Function that takes 2 args and calculates their vector
        Input : scalar : scalar of 2 vectors
                product : product of vector's standard
        Output : corner's value : float'''
    return math.acos(scalar / product)

i = 0
j = 0
k = 0
l = 0
total_corner = 0
tab_point = []
tab_vector = []
tab_standard = []
tab_scalar = []
tab_corner = []
side = int(input('Side\'s number : '))
while i < side + 1:
    if i != side:
        tab_point.append({'x': float(input(f'Enter x to point {i + 1} : ')), 'y': float(input(f'Enter y to point {i + 1} : '))})
    else:
        tab_point.append({'x': float(input(f'Enter x to M point : ')), 'y': float(input(f'Enter y to M point : '))})
    i += 1
while j < len(tab_point) - 1:
    tab_vector.append(lb_get_vector(tab_point[j]['x'], tab_point[j]['y'], tab_point[-1]['x'], tab_point[-1]['y']))
    tab_standard.append(lb_get_standard(tab_vector[j]['x'], tab_vector[j]['y']))
    j += 1
while k < len(tab_standard):
    if k == len(tab_standard) - 1:
            tab_scalar.append(lb_get_scalar(tab_vector[k]['x'], tab_vector[k]['y'], tab_vector[0]['x'], tab_vector[0]['y']))
    else:
        tab_scalar.append(lb_get_scalar(tab_vector[k]['x'], tab_vector[k]['y'], tab_vector[k + 1]['x'], tab_vector[k + 1]['y']))
    k += 1
while l < len(tab_scalar):
    if l == len(tab_scalar) - 1:
        tab_corner.append(lb_get_corner(tab_scalar[l], tab_standard[l] * tab_standard[0]))
    else:
        tab_corner.append(lb_get_corner(tab_scalar[l], tab_standard[l] * tab_standard[l + 1]))
    total_corner += tab_corner[l]
    l += 1
if total_corner == math.pi * 2:
    print(f'The point M({tab_point[-1]['x']};{tab_point[-1]['y']}) is in the polygon !')
else:
    print(f'The point M is not in the polygon :(')
